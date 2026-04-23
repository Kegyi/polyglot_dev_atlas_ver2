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
        let matched = false;
        const title = normalize(item.title);
        const desc = normalize(item.description);
        const excerpt = normalize(item.excerpt);
        const searchText = normalize(item.search_text);
        const tags = Array.isArray(item.tags) ? normalize(item.tags.join(' ')) : '';
        const terms = q.split(/\s+/).filter(Boolean);

        if (!terms.length) return 0;

        terms.forEach((term) => {
            if (title.startsWith(term)) {
                score += 70;
                matched = true;
            } else if (title.includes(term)) {
                score += 45;
                matched = true;
            }

            if (desc.includes(term)) {
                score += 18;
                matched = true;
            }
            if (excerpt.includes(term)) {
                score += 12;
                matched = true;
            }
            if (searchText.includes(term)) {
                score += 10;
                matched = true;
            }
            if (tags.includes(term)) {
                score += 10;
                matched = true;
            }
        });

        if (!matched) {
            return 0;
        }

        if (terms.length > 1 && title.includes(q)) {
            score += 20;
        }

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
            // If this is a block-level result, append the block ID as an anchor fragment
            let resultUrl = getAssetPrefix() + item.url;
            if (item.block_id) {
                resultUrl += '#' + item.block_id;
            }
            return (
                '<a class="search-result" href="' + resultUrl + '">' +
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

    function toSafeKey(segment) {
        return String(segment || '').replace(/[^a-zA-Z0-9_-]/g, '-');
    }

    function parseTargetPath(href) {
        try {
            const url = new URL(href, window.location.href);
            const parts = url.pathname.split('/').filter(Boolean);
            const modeIndex = parts.findIndex(p => ['atlas', 'course', 'meta'].includes(p.toLowerCase()));
            if (modeIndex < 0) return null;

            const mode = parts[modeIndex].toLowerCase();
            const tail = parts.slice(modeIndex + 1);
            if (!tail.length) return { mode, folders: [] };

            // Drop terminal file name (e.g. index.html, foo.html)
            const folders = tail.slice(0, -1);
            return { mode, folders };
        } catch (e) {
            return null;
        }
    }

    function seedCollectionStateForSearchTarget(href) {
        const parsed = parseTargetPath(href);
        if (!parsed) return;

        const { mode, folders } = parsed;

        try {
            // Reset stale open state for target mode.
            for (let i = localStorage.length - 1; i >= 0; i--) {
                const key = localStorage.key(i);
                if (!key) continue;
                if (key.indexOf(`${mode}-collection-`) === 0 && key.endsWith('-open')) {
                    localStorage.removeItem(key);
                }
            }

            // Legacy showcases flag should only be present for the showcases path.
            localStorage.removeItem(`${mode}-showcases-open`);

            const safeFolders = folders.map(toSafeKey).filter(Boolean);
            for (let i = 0; i < safeFolders.length; i++) {
                const fullKey = safeFolders.slice(0, i + 1).join('-');
                localStorage.setItem(`${mode}-collection-${fullKey}-open`, '1');
            }

            if (mode === 'meta' && safeFolders[0] === 'showcases') {
                localStorage.setItem(`${mode}-showcases-open`, '1');
            }
        } catch (e) {
            // Best-effort state seed only.
        }
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

    function handleResultNavigation(linkEl) {
        const href = linkEl.getAttribute('href') || '';
        if (!href) return false;

        try {
            const target = new URL(href, window.location.href);
            const samePage =
                target.pathname === window.location.pathname &&
                target.search === window.location.search;

            if (!samePage) return false;

            const hash = target.hash || '';
            if (!hash) return false;

            const topicId = decodeURIComponent(hash.slice(1));
            if (!topicId) return false;

            if (window.app && typeof window.app.focusTopic === 'function') {
                window.app.focusTopic(topicId);
                if (window.history && typeof window.history.replaceState === 'function') {
                    window.history.replaceState(null, '', window.location.pathname + window.location.search + hash);
                }
                return true;
            }
        } catch (e) {
            return false;
        }

        return false;
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

        panel.addEventListener('click', (e) => {
            const link = e.target.closest('a.search-result');
            if (!link) return;
            seedCollectionStateForSearchTarget(link.getAttribute('href') || '');

            const handledInPage = handleResultNavigation(link);
            closeResults();
            input.blur();

            if (handledInPage) {
                e.preventDefault();
                return;
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
