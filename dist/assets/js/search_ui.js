/*
 * Client-side search UI for Polyglot Atlas.
 * Uses dist/content/search-index.json generated at build time.
 */

(function () {
    const state = {
        loaded: false,
        loading: false,
        index: [],
        filtered: [],
    };

    function getAssetPrefix() {
        const mainCss = document.querySelector('link[href*="assets/css/main.css"]');
        if (!mainCss) return './';
        const href = mainCss.getAttribute('href') || '';
        const marker = 'assets/css/main.css';
        const idx = href.indexOf(marker);
        if (idx === -1) return './';
        return href.slice(0, idx);
    }

    function getSearchIndexUrl() {
        return getAssetPrefix() + 'content/search-index.json';
    }

    async function loadSearchIndex() {
        if (state.loaded || state.loading) return;
        state.loading = true;
        try {
            const res = await fetch(getSearchIndexUrl(), { cache: 'no-store' });
            if (!res.ok) throw new Error('Failed to load search index');
            const data = await res.json();
            state.index = Array.isArray(data) ? data : [];
            state.loaded = true;
        } catch (err) {
            state.index = [];
            state.loaded = true;
        } finally {
            state.loading = false;
        }
    }

    function normalize(s) {
        return String(s || '').toLowerCase().trim();
    }

    function scoreItem(item, q, currentMode) {
        let score = 0;
        const title = normalize(item.title);
        const desc = normalize(item.description);
        const excerpt = normalize(item.excerpt);
        const tags = Array.isArray(item.tags) ? normalize(item.tags.join(' ')) : '';

        if (title.startsWith(q)) score += 70;
        else if (title.includes(q)) score += 45;

        if (desc.includes(q)) score += 18;
        if (excerpt.includes(q)) score += 12;
        if (tags.includes(q)) score += 10;

        if (item.mode === currentMode) score += 8;

        return score;
    }

    function search(query) {
        const q = normalize(query);
        if (!q) return [];

        const modeClass = Array.from(document.body.classList).find(c => c.startsWith('mode-')) || 'mode-atlas';
        const currentMode = modeClass.replace('mode-', '');

        return state.index
            .map(item => ({ item, score: scoreItem(item, q, currentMode) }))
            .filter(x => x.score > 0 && x.item.url)
            .sort((a, b) => b.score - a.score)
            .slice(0, 12)
            .map(x => x.item);
    }

    function renderResults(items) {
        const panel = document.getElementById('atlas-search-results');
        if (!panel) return;

        if (!items.length) {
            panel.innerHTML = '<div class="search-empty">No results</div>';
            panel.hidden = false;
            return;
        }

        panel.innerHTML = items.map(item => {
            const excerpt = String(item.excerpt || '').slice(0, 180);
            return (
                '<a class="search-result" href="' + getAssetPrefix() + item.url + '">' +
                    '<div class="search-result-title">' + escapeHtml(item.title || item.id || 'Untitled') + '</div>' +
                    '<div class="search-result-meta">' + escapeHtml(item.mode || '') + '</div>' +
                    '<div class="search-result-excerpt">' + escapeHtml(excerpt) + '</div>' +
                '</a>'
            );
        }).join('');

        panel.hidden = false;
    }

    function escapeHtml(s) {
        return String(s || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    async function handleInput(e) {
        const input = e.target;
        const query = input.value || '';
        await loadSearchIndex();
        const results = search(query);
        renderResults(results);
    }

    function closeResults() {
        const panel = document.getElementById('atlas-search-results');
        if (!panel) return;
        panel.hidden = true;
    }

    function focusSearch() {
        const input = document.getElementById('atlas-search-input');
        if (!input) return;
        input.focus();
        input.select();
    }

    function setupSearchUI() {
        const input = document.getElementById('atlas-search-input');
        const panel = document.getElementById('atlas-search-results');
        if (!input || !panel) return;

        input.addEventListener('input', handleInput);
        input.addEventListener('focus', async () => {
            await loadSearchIndex();
            if (input.value.trim()) {
                renderResults(search(input.value));
            }
        });

        document.addEventListener('click', (e) => {
            const root = document.querySelector('.atlas-search');
            if (!root) return;
            if (!root.contains(e.target)) closeResults();
        });

        document.addEventListener('keydown', (e) => {
            const tag = (document.activeElement && document.activeElement.tagName) || '';
            const inEditable = tag === 'INPUT' || tag === 'TEXTAREA' || document.activeElement?.isContentEditable;

            if (e.key === '/' && !inEditable) {
                e.preventDefault();
                focusSearch();
                return;
            }

            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
                e.preventDefault();
                focusSearch();
                return;
            }

            if (e.key === 'Escape' && document.activeElement === input) {
                input.blur();
                closeResults();
            }
        });
    }

    document.addEventListener('DOMContentLoaded', setupSearchUI);
})();
