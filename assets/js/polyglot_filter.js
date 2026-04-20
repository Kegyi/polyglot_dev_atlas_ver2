/*
 * Polyglot Filter
 * Multi-select language filter for comparison blocks.
 */

(function () {
    const KEY = 'atlas-filter-langs';

    const state = {
        languages: [],
        selected: new Set(),
    };

    function getLanguages() {
        return Array.from(document.querySelectorAll('.lang-btn'))
            .map(btn => btn.dataset.langId)
            .filter(Boolean);
    }

    function loadState() {
        const raw = localStorage.getItem(KEY) || '';
        const parsed = raw.split(',').map(s => s.trim()).filter(Boolean);
        if (!parsed.length) {
            state.languages.forEach(l => state.selected.add(l));
            return;
        }

        parsed.forEach(l => {
            if (state.languages.includes(l)) state.selected.add(l);
        });

        if (!state.selected.size) {
            state.languages.forEach(l => state.selected.add(l));
        }
    }

    function persistState() {
        const all = state.selected.size === state.languages.length;
        if (all) {
            localStorage.removeItem(KEY);
            document.documentElement.setAttribute('data-filter-langs', '');
            return;
        }
        const value = state.languages.filter(l => state.selected.has(l)).join(',');
        localStorage.setItem(KEY, value);
        document.documentElement.setAttribute('data-filter-langs', value);
    }

    function isVisibleLanguage(lang) {
        return state.selected.has(lang);
    }

    function applyFilterToBlocks() {
        document.querySelectorAll('.code-block[data-lang]').forEach(block => {
            const lang = block.dataset.lang;
            const hide = !isVisibleLanguage(lang);
            block.classList.toggle('is-filtered-out', hide);
        });

        document.querySelectorAll('.lang-btn').forEach(btn => {
            const lang = btn.dataset.langId;
            btn.classList.toggle('filter-muted', !isVisibleLanguage(lang));
        });
    }

    function dispatchUpdate() {
        document.dispatchEvent(new CustomEvent('atlas:filter-updated', {
            detail: {
                selected: state.languages.filter(l => state.selected.has(l))
            }
        }));
    }

    function updateToggleLabel() {
        const btn = document.getElementById('polyglot-filter-toggle');
        if (!btn) return;
        if (state.selected.size === state.languages.length) {
            btn.textContent = 'Filter: All';
        } else {
            btn.textContent = 'Filter: ' + state.selected.size;
        }
    }

    function renderOptions() {
        const root = document.getElementById('polyglot-filter-options');
        if (!root) return;

        root.innerHTML = state.languages.map(lang => {
            const checked = state.selected.has(lang) ? 'checked' : '';
            return '<label class="polyglot-filter-option">'
                + '<input type="checkbox" data-lang="' + lang + '" ' + checked + '>'
                + '<span>' + lang.toUpperCase() + '</span>'
                + '</label>';
        }).join('');

        root.querySelectorAll('input[type="checkbox"]').forEach(input => {
            input.addEventListener('change', () => {
                const lang = input.getAttribute('data-lang');
                if (!lang) return;

                if (input.checked) state.selected.add(lang);
                else state.selected.delete(lang);

                // Keep at least one language selected.
                if (!state.selected.size) {
                    state.selected.add(lang);
                    input.checked = true;
                }

                persistState();
                updateToggleLabel();
                applyFilterToBlocks();
                dispatchUpdate();
            });
        });
    }

    function setAll() {
        state.selected.clear();
        state.languages.forEach(l => state.selected.add(l));
        persistState();
        renderOptions();
        updateToggleLabel();
        applyFilterToBlocks();
        dispatchUpdate();
    }

    function setCurrentSelection() {
        const html = document.documentElement;
        const mode = html.getAttribute('data-selection-mode') || 'single';
        const primary = html.getAttribute('data-primary') || '';
        const secondary = html.getAttribute('data-secondary') || '';

        const next = new Set();
        if (primary && state.languages.includes(primary)) next.add(primary);
        if (mode === 'double' && secondary && state.languages.includes(secondary)) next.add(secondary);
        if (!next.size) {
            setAll();
            return;
        }

        state.selected = next;
        persistState();
        renderOptions();
        updateToggleLabel();
        applyFilterToBlocks();
        dispatchUpdate();
    }

    function setupPanel() {
        const wrap = document.querySelector('.polyglot-filter');
        const toggle = document.getElementById('polyglot-filter-toggle');
        const panel = document.getElementById('polyglot-filter-panel');
        const useCurrent = document.getElementById('polyglot-filter-current');
        const allBtn = document.getElementById('polyglot-filter-all');
        if (!wrap || !toggle || !panel) return;

        toggle.addEventListener('click', () => {
            panel.hidden = !panel.hidden;
            wrap.classList.toggle('open', !panel.hidden);
        });

        document.addEventListener('click', (e) => {
            if (!wrap.contains(e.target)) {
                panel.hidden = true;
                wrap.classList.remove('open');
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                panel.hidden = true;
                wrap.classList.remove('open');
            }
        });

        useCurrent?.addEventListener('click', setCurrentSelection);
        allBtn?.addEventListener('click', setAll);
    }

    function init() {
        state.languages = getLanguages();
        if (!state.languages.length) return;

        loadState();
        persistState();
        renderOptions();
        updateToggleLabel();
        applyFilterToBlocks();
        setupPanel();

        document.addEventListener('atlas:selection-updated', () => {
            // Keep filtered rendering correct when visible language slots change.
            applyFilterToBlocks();
        });
    }

    document.addEventListener('DOMContentLoaded', init);
    window.PolyglotFilter = {
        apply: applyFilterToBlocks,
        setAll,
        setCurrentSelection,
    };
})();
