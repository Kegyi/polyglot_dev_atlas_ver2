/*
 * Polyglot Atlas - Phase 2 Render Helpers
 * Adds client-side behavior for:
 * - sheet transpose toggles
 * - code line-range highlighting
 * - lightweight diff-mode presentation
 * - fragment alignment across visible language columns
 */

(function () {
    function parseRanges(raw) {
        if (!raw) return [];
        return String(raw)
            .split(',')
            .map(s => s.trim())
            .filter(Boolean)
            .flatMap(token => {
                if (token.includes('-')) {
                    const [a, b] = token.split('-').map(n => parseInt(n, 10));
                    if (!Number.isFinite(a) || !Number.isFinite(b)) return [];
                    const start = Math.min(a, b);
                    const end = Math.max(a, b);
                    const out = [];
                    for (let i = start; i <= end; i++) out.push(i);
                    return out;
                }
                const n = parseInt(token, 10);
                return Number.isFinite(n) ? [n] : [];
            });
    }

    function transposeMatrix(rows) {
        if (!rows.length) return rows;
        const width = Math.max.apply(null, rows.map(r => r.length));
        const padded = rows.map(r => {
            const copy = r.slice();
            while (copy.length < width) copy.push('');
            return copy;
        });

        const out = [];
        for (let c = 0; c < width; c++) {
            const row = [];
            for (let r = 0; r < padded.length; r++) {
                row.push(padded[r][c]);
            }
            out.push(row);
        }
        return out;
    }

    function tableToArray(table) {
        const rows = Array.from(table.querySelectorAll('tr'));
        return rows.map(tr => Array.from(tr.children).map(td => td.innerHTML));
    }

    function arrayToTable(table, matrix, useHeader) {
        const tbody = table.querySelector('tbody') || document.createElement('tbody');
        tbody.innerHTML = '';

        matrix.forEach((row, rowIndex) => {
            const tr = document.createElement('tr');
            row.forEach(cell => {
                const tag = useHeader && rowIndex === 0 ? 'th' : 'td';
                const node = document.createElement(tag);
                node.innerHTML = cell;
                tr.appendChild(node);
            });
            tbody.appendChild(tr);
        });

        if (!table.querySelector('tbody')) table.appendChild(tbody);
    }

    function applySheetCardLabels(table) {
        const rows = Array.from(table.querySelectorAll('tr'));
        if (!rows.length) return;

        let headers = [];
        const firstRow = rows[0];
        const firstCells = Array.from(firstRow.children || []);
        const hasHeader = firstCells.length && firstCells.every(c => c.tagName.toLowerCase() === 'th');

        rows.forEach(r => r.classList.remove('is-header-row'));

        if (hasHeader) {
            firstRow.classList.add('is-header-row');
            headers = firstCells.map(c => (c.textContent || '').trim());
        }

        rows.forEach((row, rowIndex) => {
            if (hasHeader && rowIndex === 0) return;
            const cells = Array.from(row.querySelectorAll('td'));
            cells.forEach((cell, cellIndex) => {
                const label = headers[cellIndex] || ('Column ' + (cellIndex + 1));
                cell.setAttribute('data-label', label);
            });
        });
    }

    function setupSheetTranspose() {
        document.querySelectorAll('.sheet-block').forEach(block => {
            const btn = block.querySelector('.sheet-transpose-btn');
            const table = block.querySelector('.sheet-table');
            if (!table) return;

            applySheetCardLabels(table);

            if (!btn) return;

            btn.addEventListener('click', () => {
                const matrix = tableToArray(table);
                const transposed = transposeMatrix(matrix);
                const hasHeader = block.getAttribute('data-auto-header') === 'true';
                arrayToTable(table, transposed, hasHeader);
                applySheetCardLabels(table);
                block.classList.toggle('is-transposed');
            });
        });
    }

    function applyCodeLineHighlights(root) {
        const wrappers = (root || document).querySelectorAll('.collapsible-code[data-highlight-ranges]');

        wrappers.forEach(wrapper => {
            const ranges = parseRanges(wrapper.getAttribute('data-highlight-ranges'));
            if (!ranges.length) return;

            wrapper.querySelectorAll('.code-block code').forEach(codeEl => {
                const raw = codeEl.textContent || '';
                const lines = raw.split('\n');
                const rendered = lines.map((line, idx) => {
                    const n = idx + 1;
                    const safe = line
                        .replace(/&/g, '&amp;')
                        .replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;');
                    if (ranges.includes(n)) {
                        return '<span class="line-highlight">' + safe + '</span>';
                    }
                    return safe;
                }).join('\n');

                codeEl.innerHTML = rendered;
                codeEl.classList.remove('hljs');
                if (window.hljs) window.hljs.highlightElement(codeEl);
            });
        });
    }

    function markDiffMode() {
        document.querySelectorAll('.collapsible-code[data-diff-mode="true"]').forEach(wrapper => {
            wrapper.classList.add('diff-mode');
            const blocks = wrapper.querySelectorAll('.code-block');
            blocks.forEach((block, index) => {
                block.setAttribute('data-diff-slot', index === 0 ? 'before' : 'after');
            });
        });
    }

    function alignFragmentGroups() {
        const visibleSelector = '.code-block[style*="order"], .code-block';
        const groups = new Map();

        document.querySelectorAll('.collapsible-code[data-fragment-key]').forEach(wrapper => {
            const key = wrapper.getAttribute('data-fragment-key');
            if (!key) return;
            if (!groups.has(key)) groups.set(key, []);

            wrapper.querySelectorAll(visibleSelector).forEach(block => {
                if (window.getComputedStyle(block).display !== 'none') {
                    groups.get(key).push(block);
                }
            });
        });

        groups.forEach(blocks => {
            let maxH = 0;
            blocks.forEach(b => {
                b.style.minHeight = '';
                maxH = Math.max(maxH, b.offsetHeight);
            });
            if (maxH > 0) {
                blocks.forEach(b => { b.style.minHeight = maxH + 'px'; });
            }
        });
    }

    function runPhase2RenderPass() {
        setupSheetTranspose();
        applyCodeLineHighlights(document);
        markDiffMode();
        alignFragmentGroups();
    }

    document.addEventListener('DOMContentLoaded', runPhase2RenderPass);
    document.addEventListener('atlas:selection-updated', () => {
        alignFragmentGroups();
    });
    document.addEventListener('atlas:filter-updated', () => {
        alignFragmentGroups();
    });
})();
