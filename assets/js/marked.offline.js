/*
 * Offline markdown parser shim.
 * Exposes a minimal `marked`-compatible API used by markdown_renderer.js.
 */
(function(global) {
    'use strict';

    const options = {
        breaks: true,
        gfm: true
    };

    const escapeHtml = (text) => {
        return String(text)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    };

    const parseInline = (text) => {
        let out = escapeHtml(text);

        // Links: [text](url)
        out = out.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+"([^"]+)")?\)/g, (m, label, href, title) => {
            const safeHref = href.replace(/"/g, '%22');
            const titleAttr = title ? ` title="${escapeHtml(title)}"` : '';
            return `<a href="${safeHref}"${titleAttr}>${label}</a>`;
        });

        // Inline code
        out = out.replace(/`([^`]+)`/g, (m, code) => `<code>${escapeHtml(code)}</code>`);

        // Bold and italic
        out = out.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
        out = out.replace(/\*([^*]+)\*/g, '<em>$1</em>');

        return out;
    };

    const parse = (markdown) => {
        const lines = String(markdown || '').replace(/\r\n/g, '\n').split('\n');
        const html = [];

        let i = 0;
        let inCode = false;
        let codeLang = '';
        let codeLines = [];

        let paragraphLines = [];
        let listType = null; // 'ul' | 'ol'

        const flushParagraph = () => {
            if (!paragraphLines.length) return;
            const text = paragraphLines.join(options.breaks ? '<br>' : ' ');
            html.push(`<p>${parseInline(text)}</p>`);
            paragraphLines = [];
        };

        const flushList = () => {
            if (!listType) return;
            html.push(`</${listType}>`);
            listType = null;
        };

        while (i < lines.length) {
            const line = lines[i];

            if (inCode) {
                if (/^```/.test(line)) {
                    const langClass = codeLang ? ` class="language-${escapeHtml(codeLang)}"` : '';
                    html.push(`<pre><code${langClass}>${escapeHtml(codeLines.join('\n'))}</code></pre>`);
                    inCode = false;
                    codeLang = '';
                    codeLines = [];
                } else {
                    codeLines.push(line);
                }
                i += 1;
                continue;
            }

            const codeStart = line.match(/^```\s*([a-zA-Z0-9_+-]*)\s*$/);
            if (codeStart) {
                flushParagraph();
                flushList();
                inCode = true;
                codeLang = codeStart[1] || '';
                i += 1;
                continue;
            }

            if (/^\s*$/.test(line)) {
                flushParagraph();
                flushList();
                i += 1;
                continue;
            }

            const heading = line.match(/^(#{1,6})\s+(.*)$/);
            if (heading) {
                flushParagraph();
                flushList();
                const level = heading[1].length;
                html.push(`<h${level}>${parseInline(heading[2].trim())}</h${level}>`);
                i += 1;
                continue;
            }

            if (/^(-{3,}|\*{3,}|_{3,})\s*$/.test(line.trim())) {
                flushParagraph();
                flushList();
                html.push('<hr>');
                i += 1;
                continue;
            }

            const blockquote = line.match(/^>\s?(.*)$/);
            if (blockquote) {
                flushParagraph();
                flushList();
                html.push(`<blockquote><p>${parseInline(blockquote[1])}</p></blockquote>`);
                i += 1;
                continue;
            }

            const ul = line.match(/^\s*[-*+]\s+(.*)$/);
            if (ul) {
                flushParagraph();
                if (listType !== 'ul') {
                    flushList();
                    listType = 'ul';
                    html.push('<ul>');
                }
                html.push(`<li>${parseInline(ul[1].trim())}</li>`);
                i += 1;
                continue;
            }

            const ol = line.match(/^\s*\d+\.\s+(.*)$/);
            if (ol) {
                flushParagraph();
                if (listType !== 'ol') {
                    flushList();
                    listType = 'ol';
                    html.push('<ol>');
                }
                html.push(`<li>${parseInline(ol[1].trim())}</li>`);
                i += 1;
                continue;
            }

            if (listType) {
                flushList();
            }
            paragraphLines.push(line.trim());
            i += 1;
        }

        if (inCode) {
            const langClass = codeLang ? ` class="language-${escapeHtml(codeLang)}"` : '';
            html.push(`<pre><code${langClass}>${escapeHtml(codeLines.join('\n'))}</code></pre>`);
        }

        flushParagraph();
        flushList();

        return html.join('\n');
    };

    const markedShim = {
        parse,
        use(newOptions) {
            if (newOptions && typeof newOptions === 'object') {
                Object.assign(options, newOptions);
            }
        },
        setOptions(newOptions) {
            if (newOptions && typeof newOptions === 'object') {
                Object.assign(options, newOptions);
            }
        }
    };

    global.marked = markedShim;
})(window);
