/**
 * Markdown Renderer Module
 * 
 * Provides functionality to fetch and render markdown files into HTML content.
 * Uses the `marked` library for markdown parsing.
 * 
 * Usage:
 *   - In JSON content: { "type": "markdown", "file": "path/to/file.md" }
 */

const MarkdownRenderer = (function() {
    'use strict';

    let markedConfigured = false;

    // Configure marked with stable options.
    const setupMarked = () => {
        if (markedConfigured) {
            return;
        }

        if (typeof marked === 'undefined') {
            console.warn('marked.js library not loaded');
            return;
        }

        // Support modern marked API (use) and older builds (setOptions).
        if (typeof marked.use === 'function') {
            marked.use({
                breaks: true,
                gfm: true
            });
        } else if (typeof marked.setOptions === 'function') {
            marked.setOptions({
                breaks: true,
                gfm: true
            });
        }

        markedConfigured = true;
    };

    // Escape HTML to prevent XSS
    const escapeHtml = (text) => {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, char => map[char]);
    };

    /**
     * Fetch and render a markdown file
     * @param {string} filePath - Relative path to the markdown file
     * @param {HTMLElement} container - Target container to render the markdown into
     * @param {Object} options - Optional configuration
     * @returns {Promise<void>}
     */
    const renderMarkdownFile = async (filePath, container, options = {}) => {
        if (!container) {
            console.error('MarkdownRenderer: No container provided');
            return;
        }

        // Show loading state
        const loadingClass = options.loadingClass || 'markdown-loading';
        container.classList.add(loadingClass);

        try {
            // Fetch the markdown file
            const assetPrefix = window.assetPrefix || '';
            const cleanPrefix = assetPrefix.endsWith('/') ? assetPrefix : `${assetPrefix}/`;
            const cleanPath = filePath.startsWith('/') ? filePath.slice(1) : filePath;
            const url = `${cleanPrefix}${cleanPath}`;

            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Failed to fetch markdown: ${response.status} ${response.statusText}`);
            }

            const markdown = await response.text();

            // Render markdown to HTML
            setupMarked();
            const html = marked.parse(markdown);

            // Insert HTML into container
            container.innerHTML = html;
            container.classList.add('markdown-content');
            container.classList.remove(loadingClass);

            // Apply syntax highlighting to code blocks
            if (typeof hljs !== 'undefined') {
                container.querySelectorAll('pre code').forEach(block => {
                    hljs.highlightElement(block);
                });
            }
        } catch (error) {
            console.error('MarkdownRenderer error:', error);
            container.innerHTML = `<div class="markdown-error">Failed to load markdown: ${escapeHtml(error.message)}</div>`;
            container.classList.remove(loadingClass);
            container.classList.add('markdown-error');
        }
    };

    /**
     * Render markdown content directly (not from a file)
     * @param {string} markdown - Markdown content string
     * @param {HTMLElement} container - Target container to render into
     * @param {Object} options - Optional configuration
     * @returns {void}
     */
    const renderMarkdownContent = (markdown, container, options = {}) => {
        if (!container) {
            console.error('MarkdownRenderer: No container provided');
            return;
        }

        try {
            setupMarked();
            const html = marked.parse(markdown);
            container.innerHTML = html;
            container.classList.add('markdown-content');

            // Apply syntax highlighting
            if (typeof hljs !== 'undefined') {
                container.querySelectorAll('pre code').forEach(block => {
                    hljs.highlightElement(block);
                });
            }
        } catch (error) {
            console.error('MarkdownRenderer error:', error);
            container.innerHTML = `<div class="markdown-error">Failed to render markdown: ${escapeHtml(error.message)}</div>`;
            container.classList.add('markdown-error');
        }
    };

    /**
     * Process all markdown elements in the page
     * Looks for elements with data-markdown-file attribute
     */
    const processMarkdownElements = async (root = document) => {
        const scanRoot = root && typeof root.querySelectorAll === 'function' ? root : document;
        const elements = scanRoot.querySelectorAll('[data-markdown-file]');
        const promises = [];

        for (const el of elements) {
            const filePath = el.getAttribute('data-markdown-file');
            if (filePath) {
                promises.push(renderMarkdownFile(filePath, el));
            }
        }

        await Promise.all(promises);
    };

    /**
     * Initialize markdown renderer on page load
     */
    const init = () => {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                processMarkdownElements(document);
            });
        } else {
            processMarkdownElements(document);
        }
    };

    // Public API
    return {
        renderMarkdownFile,
        renderMarkdownContent,
        processMarkdownElements,
        init
    };
})();

// Auto-initialize on page load
MarkdownRenderer.init();
