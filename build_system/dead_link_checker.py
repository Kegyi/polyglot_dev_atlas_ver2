"""
Polyglot Atlas - Dead Link Checker
Validates external URLs in content pages for availability and correct status codes.
Usage: python build_system/dead_link_checker.py [--verbose] [--timeout SECONDS]
"""

import os
import json
import re
import sys
import argparse
import urllib.request
import urllib.error
from urllib.parse import urlparse
from typing import Dict, List, Tuple, Set
from collections import defaultdict


class DeadLinkChecker:
    """Validates HTTP/HTTPS URLs in Atlas content."""
    
    def __init__(self, timeout=10, verbose=False):
        self.timeout = timeout
        self.verbose = verbose
        self.checked_urls: Set[str] = set()  # Cache to avoid re-checking same URL
        self.results: Dict[str, Dict] = defaultdict(lambda: {'status': None, 'reason': ''})
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.content_dir = os.path.join(self.base_dir, 'content')
        self.pages_dir = os.path.join(self.content_dir, 'pages')
    
    def _extract_urls_from_text(self, text: str) -> List[str]:
        """Extract URLs from markdown-style and plain URLs in text."""
        if not isinstance(text, str):
            return []
        
        urls = []
        
        # Match markdown links: [text](url)
        markdown_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        for match in re.finditer(markdown_pattern, text):
            url = match.group(2)
            if url.startswith(('http://', 'https://')):
                urls.append(url)
        
        # Match plain HTTP/HTTPS URLs
        url_pattern = r'https?://[^\s<>"\)}\]]*'
        for match in re.finditer(url_pattern, text):
            url = match.group(0)
            # Clean up trailing punctuation that's likely not part of URL
            url = re.sub(r'[.,;:\)\]\}]+$', '', url)
            if url not in urls:
                urls.append(url)
        
        return urls
    
    def _extract_urls_from_item(self, item: dict) -> List[str]:
        """Extract URLs from a content block item."""
        urls = []
        
        if not isinstance(item, dict):
            return urls
        
        # Check various text fields
        for field in ['text', 'content', 'description', 'url', 'href', 'link']:
            if field in item and isinstance(item[field], str):
                urls.extend(self._extract_urls_from_text(item[field]))
        
        # Check nested content recursively
        if 'content' in item and isinstance(item['content'], list):
            for sub_item in item['content']:
                urls.extend(self._extract_urls_from_item(sub_item))
        
        # Check blocks array
        if 'blocks' in item and isinstance(item['blocks'], list):
            for block in item['blocks']:
                urls.extend(self._extract_urls_from_item(block))
        
        return urls
    
    def _extract_urls_from_page(self, page_data: dict) -> List[str]:
        """Extract all URLs from a page JSON."""
        urls = []
        
        if not isinstance(page_data, dict):
            return urls
        
        # Check various fields
        for field in ['description', 'url']:
            if field in page_data and isinstance(page_data[field], str):
                urls.extend(self._extract_urls_from_text(page_data[field]))
        
        # Process content array
        if 'content' in page_data and isinstance(page_data['content'], list):
            for item in page_data['content']:
                urls.extend(self._extract_urls_from_item(item))
        
        return urls
    
    def validate_url(self, url: str) -> Tuple[bool, str]:
        """
        Validate a single URL.
        Returns: (is_valid, reason/status_message)
        """
        if url in self.checked_urls:
            cached_result = self.results[url]
            return cached_result['status'] == 'OK', cached_result['reason']
        
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Polyglot Atlas Link Checker)'}
            )
            
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                status = response.status
                if 200 <= status < 300:
                    self.results[url] = {'status': 'OK', 'reason': f'HTTP {status}'}
                    self.checked_urls.add(url)
                    return True, f'HTTP {status}'
                else:
                    reason = f'HTTP {status} (unexpected success code)'
                    self.results[url] = {'status': 'WARN', 'reason': reason}
                    self.checked_urls.add(url)
                    return False, reason
        
        except urllib.error.HTTPError as e:
            reason = f'HTTP {e.code} ({e.reason})'
            self.results[url] = {'status': 'ERROR', 'reason': reason}
            self.checked_urls.add(url)
            return False, reason
        
        except urllib.error.URLError as e:
            reason = f'Connection error: {e.reason}'
            self.results[url] = {'status': 'ERROR', 'reason': reason}
            self.checked_urls.add(url)
            return False, reason
        
        except Exception as e:
            reason = f'Error: {str(e)}'
            self.results[url] = {'status': 'ERROR', 'reason': reason}
            self.checked_urls.add(url)
            return False, reason
    
    def scan_pages(self) -> Dict[str, List[Dict]]:
        """Scan all pages and validate URLs. Returns results by page."""
        page_results = defaultdict(list)
        
        if not os.path.exists(self.pages_dir):
            print(f"Pages directory not found: {self.pages_dir}")
            return page_results
        
        # Walk through all .json files
        for root, dirs, files in os.walk(self.pages_dir):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.pages_dir)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            page_data = json.load(f)
                        
                        urls = self._extract_urls_from_page(page_data)
                        
                        for url in urls:
                            is_valid, reason = self.validate_url(url)
                            page_results[rel_path].append({
                                'url': url,
                                'valid': is_valid,
                                'reason': reason
                            })
                            
                            if self.verbose:
                                status = '✓' if is_valid else '✗'
                                print(f"  {status} {url} ({reason})")
                    
                    except json.JSONDecodeError as e:
                        print(f"ERROR parsing {rel_path}: {e}")
                    except Exception as e:
                        print(f"ERROR processing {rel_path}: {e}")
        
        return page_results
    
    def print_report(self, results: Dict[str, List[Dict]]) -> Tuple[int, int, int]:
        """Print a formatted report and return (valid_count, error_count, total_count)."""
        valid_count = 0
        error_count = 0
        
        print("\n" + "=" * 70)
        print("DEAD LINK CHECK REPORT")
        print("=" * 70)
        
        pages_with_errors = []
        
        for page_path in sorted(results.keys()):
            links = results[page_path]
            page_valid = sum(1 for link in links if link['valid'])
            page_errors = len(links) - page_valid
            
            if page_errors > 0:
                pages_with_errors.append((page_path, links))
        
        if not pages_with_errors:
            print(f"\n✓ All external links are valid!")
            valid_count = sum(sum(1 for link in links if link['valid']) for links in results.values())
            print(f"  Total links checked: {valid_count}")
        else:
            print(f"\n✗ Found issues in {len(pages_with_errors)} page(s):\n")
            
            for page_path, links in pages_with_errors:
                page_errors = [link for link in links if not link['valid']]
                print(f"  {page_path}")
                for link in page_errors:
                    print(f"    ✗ {link['url']}")
                    print(f"      → {link['reason']}")
                print()
            
            error_count = sum(sum(1 for link in links if not link['valid']) for links in results.values())
            valid_count = sum(sum(1 for link in links if link['valid']) for links in results.values())
        
        total_count = valid_count + error_count
        
        print("=" * 70)
        print(f"Summary: {valid_count} valid, {error_count} broken (Total: {total_count})")
        print("=" * 70)
        
        return valid_count, error_count, total_count


def main():
    parser = argparse.ArgumentParser(
        description="Dead Link Checker - Validates external URLs in Atlas content"
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output for each URL checked'
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=10,
        help='HTTP request timeout in seconds (default: 10)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Exit with code 1 if any broken links found'
    )
    
    args = parser.parse_args()
    
    checker = DeadLinkChecker(timeout=args.timeout, verbose=args.verbose)
    
    if args.verbose:
        print(f"Scanning pages in: {checker.pages_dir}\n")
    
    results = checker.scan_pages()
    valid_count, error_count, total_count = checker.print_report(results)
    
    if args.strict and error_count > 0:
        sys.exit(1)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
