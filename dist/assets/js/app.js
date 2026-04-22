/**
 * Polyglot Atlas - General UI Controller (Phase 3)
 * Handles Theme, Palette, Global Design Style, Sidebars, View Modes, 
 * Topic Navigation, Scroll-Spy, and Mode-Specific Page Persistence.
 */

const app = {
    icons: {
        theme: {
            dark: '<svg viewBox="0 0 24 24" width="18" height="18" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
            light: '<svg viewBox="0 0 24 24" width="18" height="18" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>',
            'high-contrast': '<svg viewBox="0 0 24 24" width="18" height="18" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><rect x="2" y="2" width="20" height="20" rx="2" ry="2" fill="white"/><circle cx="8" cy="8" r="3" fill="black"/><circle cx="16" cy="16" r="3" fill="black"/><path d="M8 16 L16 8" stroke="black" stroke-width="2"/></svg>'
        },
        style: {
            sharp: '<svg viewBox="0 0 24 24" width="14" height="14" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>',
            round: '<svg viewBox="0 0 24 24" width="14" height="14" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><circle cx="12" cy="12" r="8"/></svg>',
            airy: '<svg viewBox="0 0 24 24" width="14" height="14" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><path d="M19 17H6a4 4 0 1 1 .5-7.9A6 6 0 1 1 19 17z"/></svg>'
        }
    },
    /**
     * Cycles through Dark → Light → High-Contrast → Dark.
     * Updates both Theme CSS and HLJS theme dynamically.
     */
    toggleTheme: function() {
        const html = document.documentElement;
        const current = html.getAttribute('data-theme') || 'dark';
        
        // Cycle: dark → light → high-contrast → dark
        const themeOrder = ['dark', 'light', 'high-contrast'];
        const currentIdx = themeOrder.indexOf(current);
        const nextIdx = (currentIdx + 1) % themeOrder.length;
        const target = themeOrder[nextIdx];
        
        // Update data attribute
        html.setAttribute('data-theme', target);
        localStorage.setItem('atlas-theme', target);
        this.updateIcons(target);

        // Update Theme CSS file
        const themeLink = document.getElementById('theme-css');
        if (themeLink) {
            const prefix = window.assetPrefix || './';
            themeLink.href = `${prefix}assets/css/themes/${target}.css`;
        }

        // Update HLJS theme (only dark/light modes have HLJS alternatives)
        const hljsLink = document.getElementById('hljs-theme');
        if (hljsLink) {
            const hljsFile = target === 'dark' ? 'atom-one-dark.min.css' : (target === 'light' ? 'github.min.css' : 'atom-one-dark.min.css');
            const prefix = window.assetPrefix || './';
            hljsLink.href = `${prefix}assets/hljs/${hljsFile}`;
        }
    },

    updateIcons: function(theme) {
        const btn = document.getElementById('theme-toggle');
        if (btn) btn.innerHTML = this.icons.theme[theme] || this.icons.theme.dark;
    },

    /**
     * Changes the Color Palette (Zinc, Ocean, Sunset).
     */
    setPalette: function(pal) {
        document.documentElement.setAttribute('data-palette', pal);
        localStorage.setItem('atlas-palette', pal);
    },

    /**
     * PHASE 3: GLOBAL DESIGN SYSTEM
     * Changes the geometric personality (Sharp, Round, Airy).
     */
    setGlobalStyle: function(style) {
        document.documentElement.setAttribute('data-global-style', style);
        localStorage.setItem('atlas-global-style', style);
    },

    /**
     * Collapses or Expands Sidebars.
     */
    toggleSidebar: function(side) {
        const el = document.getElementById(`sidebar-${side}`);
        if (!el) return;
        
        const isCollapsed = el.classList.toggle('collapsed');
        const handle = el.querySelector('.sidebar-handle');
        
        if (handle) {
            if (side === 'left') {
                handle.innerText = isCollapsed ? '▶' : '◀';
            } else {
                handle.innerText = isCollapsed ? '◀' : '▶';
            }
        }
    },

    /**
     * SIDEBAR DENSITY (Detailed vs Compact).
     */
    toggleSidebarDensity: function() {
        const html = document.documentElement;
        const current = html.getAttribute('data-sidebar-density') || 'high';
        const target = current === 'high' ? 'minimal' : 'high';
        
        html.setAttribute('data-sidebar-density', target);
        localStorage.setItem('atlas-sidebar-density', target);
        this.updateDensityUI(target);
    },

    updateDensityUI: function(density) {
        const btn = document.getElementById('density-toggle-btn');
        if (btn) btn.innerText = density === 'high' ? 'Detailed' : 'Compact';
    },

    /**
     * VIEW MODE: All (scrolling) vs Focus (single topic).
     */
    toggleViewMode: function() {
        const html = document.documentElement;
        const current = html.getAttribute('data-view-mode') || 'all';
        const target = current === 'all' ? 'focused' : 'all';
        
        html.setAttribute('data-view-mode', target);
        localStorage.setItem('atlas-view-mode', target);
        this.updateViewModeUI(target);
        
        const activeLink = document.querySelector('#toc li.active');
        if (activeLink) {
            this.focusTopic(activeLink.dataset.topicId);
        } else {
            // No active sidebar link — pick the most-visible topic in the
            // content area so focused mode chooses the main section the user
            // is looking at (not a tiny sliver at the top).
            const most = this.getMostVisibleTopic();
            if (most) {
                this.focusTopic(most.id);
            } else {
                const firstTopic = document.querySelector('.topic-section');
                if (firstTopic) this.focusTopic(firstTopic.id);
            }
        }
    },

    getMostVisibleTopic: function() {
        const contentArea = document.getElementById('content') || document.documentElement;
        const cRect = contentArea.getBoundingClientRect();
        const topics = Array.from(document.querySelectorAll('.topic-section'));
        if (!topics.length) return null;

        let best = null;
        let bestVisible = -1;

        topics.forEach(t => {
            const r = t.getBoundingClientRect();
            const top = Math.max(r.top, cRect.top);
            const bottom = Math.min(r.bottom, cRect.bottom);
            const visibleHeight = Math.max(0, bottom - top);
            if (visibleHeight > bestVisible) {
                bestVisible = visibleHeight;
                best = t;
            }
        });

        return best;
    },

    getCurrentMode: function() {
        // body contains classes like 'mode-meta' or 'mode-atlas'
        const cls = Array.from(document.body.classList).find(c => c.startsWith('mode-'));
        if (cls) return cls.replace('mode-', '');
        // fallback from path
        const p = window.location.pathname || '';
        if (p.indexOf('/meta/') !== -1 || p.indexOf('/meta') === 0) return 'meta';
        if (p.indexOf('/course/') !== -1 || p.indexOf('/course') === 0) return 'course';
        return 'atlas';
    },

    isProjectMode: function() {
        const p = (window.location.pathname || '').toLowerCase();
        return document.body.classList.contains('home-view') ||
            (this.getCurrentMode() === 'atlas' && /\/index\.html$/.test(p) && p.indexOf('/atlas/') === -1);
    },

    getDisplayedMode: function() {
        return this.isProjectMode() ? 'project' : this.getCurrentMode();
    },

    getModeLabel: function(mode) {
        if (mode === 'project') return 'PROJECT';
        if (mode === 'course') return 'COURSE';
        if (mode === 'meta') return 'META';
        return 'ATLAS';
    },

    updateModeTitle: function(mode) {
        const logo = document.getElementById('app-mode-title');
        if (!logo) return;
        const label = this.getModeLabel(mode || this.getDisplayedMode());
        logo.innerHTML = `POLYGLOT <span class="accent">${label}</span>`;
    },

    getModeRootPrefix: function() {
        const script = document.querySelector('script[src*="assets/js/app.js"]');
        if (!script) return './';
        const src = script.getAttribute('src') || './assets/js/app.js';
        const marker = 'assets/js/app.js';
        const idx = src.indexOf(marker);
        if (idx === -1) return './';
        return src.substring(0, idx) || './';
    },

    getModeLinkDefs: function() {
        const modeSwitcherLinks = Array.from(document.querySelectorAll('.mode-switcher .mode-switcher-link'));
        if (modeSwitcherLinks.length > 0) {
            return modeSwitcherLinks
                .map(link => {
                    const label = (link.textContent || '').trim();
                    if (!label) return null;
                    return { label, href: link.getAttribute('href') || '#' };
                })
                .filter(Boolean);
        }

        const prefix = this.getModeRootPrefix();
        return [
            { label: 'Project', href: `${prefix}index.html` },
            { label: 'Atlas', href: `${prefix}atlas/index.html` },
            { label: 'Course', href: `${prefix}course/index.html` },
            { label: 'Meta', href: `${prefix}meta/index.html` }
        ];
    },

    bindModeTitleSync: function(root) {
        if (!root) return;
        root.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                const label = (link.textContent || '').trim().toLowerCase();
                this.updateModeTitle(label || this.getDisplayedMode());
            });
        });
    },

    ensureModeSwitcher: function() {
        const modeSwitcher = document.querySelector('.mode-switcher');
        if (!modeSwitcher) return;

        const summary = modeSwitcher.querySelector('.mode-switcher-trigger') || modeSwitcher.querySelector('summary');
        if (summary && !summary.innerHTML.trim()) {
            summary.innerHTML = '<span class="chevron">▼</span>';
        }

        let menu = modeSwitcher.querySelector('.mode-switcher-menu');
        if (!menu) {
            menu = document.createElement('div');
            menu.className = 'mode-switcher-menu';
            modeSwitcher.appendChild(menu);
        }

        if (menu.querySelectorAll('.mode-switcher-link').length === 0) {
            const current = this.getDisplayedMode();
            const defs = this.getModeLinkDefs();
            menu.innerHTML = defs.map(def => {
                const lower = def.label.toLowerCase();
                const active = lower === current ? ' active' : '';
                return `<a href="${def.href}" class="mode-switcher-link${active}" onclick="app.prepareModeSwitch()">${def.label}</a>`;
            }).join('');
        }

        modeSwitcher.style.display = '';
        this.bindModeTitleSync(menu);
        this.positionModeMenuUnderModeLabel();
    },

    positionModeMenuUnderModeLabel: function() {
        const logo = document.getElementById('app-mode-title');
        const accent = document.querySelector('#app-mode-title .accent');
        const modeSwitcher = document.querySelector('.mode-switcher');
        if (!logo || !accent || !modeSwitcher) return;

        const accentRect = accent.getBoundingClientRect();
        const switcherRect = modeSwitcher.getBoundingClientRect();
        const left = Math.round(accentRect.left - switcherRect.left);
        modeSwitcher.style.setProperty('--mode-menu-left', `${left}px`);
    },

    setupProjectSidebarModes: function() {
        if (!this.isProjectMode()) return;
        const tocMain = document.getElementById('toc-main');
        if (!tocMain) return;
        if (tocMain.querySelector('.nav-mode-group')) return;

        const defs = this.getModeLinkDefs();
        const modeItems = defs.map(def => {
            const lower = def.label.toLowerCase();
            const active = lower === 'project' ? ' class="active"' : '';
            return `<li${active}><a href="${def.href}" onclick="app.prepareModeSwitch()">${def.label}</a></li>`;
        }).join('');

        const html = `<li class="nav-mode-group"><span>Modes</span></li>${modeItems}`;
        tocMain.insertAdjacentHTML('afterbegin', html);
    },

    hideTopModeLinks: function() {
        const homeModesNav = document.getElementById('home-modes-nav');
        if (homeModesNav) {
            homeModesNav.style.display = 'none';
        }
    },

    updateViewModeUI: function(mode) {
        const btn = document.getElementById('view-mode-btn');
        if (btn) btn.innerText = mode === 'all' ? 'All' : 'Focus';
    },

    /**
     * Showcases navigation helpers: swap main nav for showcases list and back.
     */
    openShowcases: function(options) {
        const main = document.getElementById('toc-main');
        const shows = document.getElementById('toc-showcases');
        if (!shows || !main) return;
        const noNavigate = !!(options && options.noNavigate);
        // store scroll position to restore later
        main.dataset._scroll = main.scrollTop || 0;
        main.style.display = 'none';
        shows.style.display = '';
        document.documentElement.classList.add('showcases-open');
        // If the user is not already inside the showcases subpath, open the
        // showcases intro/index page by navigating to its link so the submenu
        // shows content immediately. Otherwise just focus the first content link.
        const firstContentLink = shows.querySelector('li:not(.nav-back) a');
        if (firstContentLink) {
            // If we're not already on a showcases page, navigate to the intro
            // (the first content link is an appropriate default).
            try {
                const isOnShowcases = window.location.pathname.indexOf('/meta/showcases/') !== -1;
                if (!isOnShowcases && !noNavigate) {
                    const mode = this.getCurrentMode();
                    const prevKey = `${mode}-showcases-prev-path`;
                    if (!localStorage.getItem(prevKey)) {
                        localStorage.setItem(prevKey, window.location.pathname + window.location.search + window.location.hash);
                    }
                    // Persist the 'open' state so the destination page renders with
                    // the showcases list visible (anti-flash uses this flag).
                    try { localStorage.setItem(`${mode}-showcases-open`, '1'); } catch (e) {}
                    // Blur the toggle so the browser focus ring doesn't stick on it
                    try { const toggle = document.querySelector('.nav-item.nav-showcases a'); if (toggle) toggle.blur(); } catch (e) {}
                    // Navigate to the intro/index for showcases
                    window.location.href = firstContentLink.getAttribute('href');
                    return;
                }
            } catch (e) {}
            // If we're already inside the showcases path, prefer focusing the
            // currently active showcase link (so the intro doesn't get the
            // persistent focus ring). Fall back to the first content link.
            try {
                const activeLink = shows.querySelector('li.active a');
                if (activeLink) activeLink.focus();
                else firstContentLink.focus();
            } catch (e) { try { firstContentLink.focus(); } catch (e) {} }
        }
        // persist showcases-open state so navigation remains in showcases
        const mode = this.getCurrentMode();
        try { localStorage.setItem(`${mode}-showcases-open`, '1'); } catch (e) {}
        // remember the page we came from so Back can return to it (per-mode)
        try {
            const prevKey = `${mode}-showcases-prev-path`;
            if (!localStorage.getItem(prevKey)) {
                localStorage.setItem(prevKey, window.location.pathname + window.location.search + window.location.hash);
            }
            // also store which topic was active if any
            const active = document.querySelector('#toc li.active');
            if (active && active.dataset && active.dataset.topicId) {
                localStorage.setItem(`${mode}-showcases-prev-topic`, active.dataset.topicId);
            }
        } catch (e) {}
    },

    /**
     * Generic collection open/close helpers. Collections are emitted by the
     * builder for any immediate subfolder under a documentation mode (e.g.
     * meta/showcases). The builder creates a hidden list with id
     * `toc-collection-{mode}-{key}` and a toggle that calls these helpers.
     */
    openCollection: function(mode, key, options) {
        try {
            const main = document.getElementById('toc-main');
            const shows = document.getElementById(`toc-collection-${mode}-${key}`);
            if (!shows || !main) return;
            const noNavigate = !!(options && options.noNavigate);
            // Clear any other open flags for this mode so only one collection
            // is considered 'open' at a time. This prevents multiple lists
            // from competing and avoids stale state when navigating.
            try {
                for (let i = localStorage.length - 1; i >= 0; i--) {
                    const k = localStorage.key(i);
                    if (!k) continue;
                    if (k.indexOf(`${mode}-collection-`) === 0 && k.endsWith('-open') && k !== `${mode}-collection-${key}-open`) {
                        try { localStorage.removeItem(k); } catch (e) {}
                    }
                }
            } catch (e) {}

            // Mark ancestor collections as open so state persists for parents
            try {
                const segs = key.split('-');
                for (let i = 1; i < segs.length; i++) {
                    const anc = segs.slice(0, i).join('-');
                    try { localStorage.setItem(`${mode}-collection-${anc}-open`, '1'); } catch (e) {}
                }
            } catch (e) {}

            // Hide whichever list is currently visible (main or another collection)
            const collections = Array.from(document.querySelectorAll('.nav-collection-list'));
            let visible = collections.find(el => window.getComputedStyle(el).display !== 'none');
            if (visible) {
                visible.dataset._scroll = visible.scrollTop || 0;
                visible.style.display = 'none';
            } else {
                main.dataset._scroll = main.scrollTop || 0;
                main.style.display = 'none';
            }

            // Ensure any injected blocking style is removed for a clean replace
            try {
                const gen = document.querySelector('style[data-generated="collection-open-style"]');
                if (gen) gen.remove();
                document.documentElement.removeAttribute('data-collection-open');
            } catch (e) {}

            shows.style.display = '';
            document.documentElement.classList.add('showcases-open');

            const firstContentLink = shows.querySelector('li:not(.nav-back) a');
            if (firstContentLink) {
                const keyPath = key.split('-').join('/');
                const isOnCollection = window.location.pathname.indexOf(`/${mode}/${keyPath}/`) !== -1;
                if (!isOnCollection && !noNavigate) {
                    const prevKey = `${mode}-collection-${key}-prev-path`;
                    // Always refresh the origin path so Back returns to the
                    // most recent page that opened this collection.
                    localStorage.setItem(prevKey, window.location.pathname + window.location.search + window.location.hash);
                    try { localStorage.setItem(`${mode}-collection-${key}-open`, '1'); } catch (e) {}
                    // Mark that this collection was opened via navigation so Back
                    // can return the user to the prior page instead of just closing
                    // the submenu. This flag is only set when we performed a
                    // navigation into the collection.
                    try { localStorage.setItem(`${mode}-collection-${key}-opened-via-nav`, '1'); } catch (e) {}
                    try { const toggle = document.querySelector(`.nav-item.nav-collection.nav-${key} a`); if (toggle) toggle.blur(); } catch (e) {}
                    window.location.href = firstContentLink.getAttribute('href');
                    return;
                }
            }

            try { localStorage.setItem(`${mode}-collection-${key}-open`, '1'); } catch (e) {}
            try {
                const prevKey = `${mode}-collection-${key}-prev-path`;
                if (!localStorage.getItem(prevKey)) {
                    localStorage.setItem(prevKey, window.location.pathname + window.location.search + window.location.hash);
                }
                const active = document.querySelector('#toc li.active');
                if (active && active.dataset && active.dataset.topicId) {
                    localStorage.setItem(`${mode}-collection-${key}-prev-topic`, active.dataset.topicId);
                }
            } catch (e) {}
        } catch (e) {}
    },

    closeCollection: function(mode, key) {
        try {
            const main = document.getElementById('toc-main');
            const shows = document.getElementById(`toc-collection-${mode}-${key}`);
            if (!shows || !main) return;
            const prevKey = `${mode}-collection-${key}-prev-path`;
            const prev = localStorage.getItem(prevKey);
            if (prev && prev !== (window.location.pathname + window.location.search + window.location.hash)) {
                localStorage.removeItem(prevKey);
                localStorage.removeItem(`${mode}-collection-${key}-prev-topic`);
                localStorage.removeItem(`${mode}-collection-${key}-open`);
                window.location.href = prev;
                return;
            }

            // If this collection is nested, show its parent collection instead
            // of returning immediately to the main list.
            // Decide whether this close should navigate back to the stored
            // previous page. Only do that when this collection was opened via
            // navigation from another page.
            const openedViaNavKey = `${mode}-collection-${key}-opened-via-nav`;
            const openedViaNav = localStorage.getItem(openedViaNavKey) === '1';

            // Clear the explicit open flag for this collection
            try { localStorage.removeItem(`${mode}-collection-${key}-open`); } catch (e) {}

            // If opened via navigation and we have a prev path, return to it.
            if (openedViaNav) {
                try { localStorage.removeItem(openedViaNavKey); } catch (e) {}
                if (prev && prev !== (window.location.pathname + window.location.search + window.location.hash)) {
                    localStorage.removeItem(prevKey);
                    localStorage.removeItem(`${mode}-collection-${key}-prev-topic`);
                    window.location.href = prev;
                    return;
                }
            }

            // Not navigating back: close this collection and show nearest parent
            shows.style.display = 'none';
            // Remove any injected blocking style for this collection
            try {
                const gen = document.querySelector('style[data-generated="collection-open-style"]');
                if (gen) gen.remove();
                document.documentElement.removeAttribute('data-collection-open');
            } catch (e) {}

            // Find nearest ancestor submenu by progressively truncating key
            const segs = key.split('-');
            while (segs.length > 0) {
                segs.pop();
                if (segs.length === 0) break;
                const candidate = segs.join('-');
                const parentList = document.getElementById(`toc-collection-${mode}-${candidate}`);
                if (parentList) {
                    try { localStorage.setItem(`${mode}-collection-${candidate}-open`, '1'); } catch (e) {}
                    parentList.style.display = '';
                    return;
                }
            }

            // No parent found; restore main menu
            main.style.display = '';
            document.documentElement.classList.remove('showcases-open');
            // If there is a global collection-open marker, remove it so the
            // CSS rule hiding #toc-main no longer applies.
            document.documentElement.classList.remove('collection-open');
            const scroll = parseInt(main.dataset._scroll || 0, 10);
            main.scrollTop = scroll;
        } catch (e) {}
    },

    closeCollectionUI: function(mode, key) {
        try {
            const shows = document.getElementById(`toc-collection-${mode}-${key}`);
            const main = document.getElementById('toc-main');
            if (!shows || !main) return;
            shows.style.display = 'none';
            const parentKey = key.indexOf('-') !== -1 ? key.substring(0, key.lastIndexOf('-')) : null;
            if (parentKey) {
                const parentList = document.getElementById(`toc-collection-${mode}-${parentKey}`);
                if (parentList) {
                    parentList.style.display = '';
                    return;
                }
            }
            // Clean up any injected style
            try {
                const gen = document.querySelector('style[data-generated="collection-open-style"]');
                if (gen) gen.remove();
                document.documentElement.removeAttribute('data-collection-open');
            } catch (e) {}
            main.style.display = '';
            document.documentElement.classList.remove('showcases-open');
            document.documentElement.classList.remove('collection-open');
        } catch (e) {}
    },

    closeShowcases: function() {
        const main = document.getElementById('toc-main');
        const shows = document.getElementById('toc-showcases');
        if (!shows || !main) return;
        const mode = this.getCurrentMode();
        try {
            const prevKey = `${mode}-showcases-prev-path`;
            const prev = localStorage.getItem(prevKey);
            if (prev && prev !== (window.location.pathname + window.location.search + window.location.hash)) {
                // clear the saved per-mode prev and open flag, then navigate back
                localStorage.removeItem(prevKey);
                localStorage.removeItem(`${mode}-showcases-prev-topic`);
                localStorage.removeItem(`${mode}-showcases-open`);
                window.location.href = prev;
                return;
            }
        } catch (e) {}

        shows.style.display = 'none';
        main.style.display = '';
        document.documentElement.classList.remove('showcases-open');
        // restore scroll
        const scroll = parseInt(main.dataset._scroll || 0, 10);
        main.scrollTop = scroll;
        try { localStorage.removeItem(`${mode}-showcases-open`); } catch (e) {}
    },

    /**
     * Close showcases UI without clearing per-mode stored preferences.
     * Used when switching modes so we don't delete the mode's saved state.
     */
    closeShowcasesUI: function() {
        try {
            const shows = document.getElementById('toc-showcases');
            const main = document.getElementById('toc-main');
            if (!shows || !main) return;
            shows.style.display = 'none';
            main.style.display = '';
            document.documentElement.classList.remove('showcases-open');
        } catch (e) {}
    },

    /**
     * Prepare for a mode switch without touching the DOM. This is used by
     * the mode switcher links so we don't flip the visible sidebar state
     * locally (which causes a brief flash) — the destination page will
     * restore its own state from localStorage on load.
     */
    prepareModeSwitch: function() {
        try {
            const mode = this.getCurrentMode();
            // Do not modify the DOM; only ensure we don't accidently leave
            // stale per-mode flags that would cause the wrong nav to render.
            // We purposely *do not* remove `${mode}-showcases-open` here so
            // the destination mode can restore its own state. Keep this
            // function minimal to avoid visual flashes.
        } catch (e) {}
    },

    /**
     * Clear any Showcases-related persisted state. Call on mode switches
     * so opening Showcases in one mode doesn't leak into other modes.
     */
    clearShowcasesState: function() {
        try {
            localStorage.removeItem('atlas-showcases-open');
            localStorage.removeItem('atlas-showcases-prev-path');
            localStorage.removeItem('atlas-showcases-prev-topic');
        } catch (e) {}
        // Ensure UI is closed if present
        try {
            const shows = document.getElementById('toc-showcases');
            const main = document.getElementById('toc-main');
            if (shows && main) {
                shows.style.display = 'none';
                main.style.display = '';
                document.documentElement.classList.remove('showcases-open');
            }
        } catch (e) {}
    },

    /**
     * Collapses/Expands specific content block bodies.
     */
    toggleTopic: function(id) {
        const el = document.getElementById(id);
        if (!el) return;
        
        const isNowCollapsed = el.classList.toggle('is-collapsed');
        const body = el.querySelector(':scope > .topic-body');
        
        if (body) {
            if (isNowCollapsed) {
                body.classList.add('collapsed');
            } else {
                body.classList.remove('collapsed');
            }
        }
    },

    /**
     * Highlights the sidebar item and handles group auto-expansion.
     */
    syncSidebarActiveState: function(id) {
        document.querySelectorAll('#toc li').forEach(li => li.classList.remove('active'));
        
        const sidebarLink = document.querySelector(`#toc li[data-topic-id="${id}"]`);
        if (sidebarLink) {
            sidebarLink.classList.add('active');
            const parentGroup = sidebarLink.closest('.toc-group');
            if (parentGroup) parentGroup.classList.add('active');
        }
    },

    /**
     * Navigates to a topic, expanding parents if needed.
     */
    focusTopic: function(id) {
        const el = document.getElementById(id);
        if (!el) return;

        document.querySelectorAll('.topic-section').forEach(s => {
            s.classList.remove('active', 'parent-active');
        });

        el.classList.add('active');

        let parent = el.parentElement;
        while (parent && parent !== document.body) {
            if (parent.classList.contains('topic-section')) {
                parent.classList.add('parent-active');
                parent.classList.remove('is-collapsed');
                const pBody = parent.querySelector(':scope > .topic-body');
                if (pBody) pBody.classList.remove('collapsed');
            }
            parent = parent.parentElement;
        }

        el.classList.remove('is-collapsed');
        const targetBody = el.querySelector(':scope > .topic-body');
        if (targetBody) targetBody.classList.remove('collapsed');

        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        el.classList.add('highlight-flash');
        setTimeout(() => el.classList.remove('highlight-flash'), 2000);
        
        if (document.documentElement.getAttribute('data-view-mode') === 'focused') {
            this.syncSidebarActiveState(id);
        }
    },

    /**
     * Intersection Observer for sidebar sync.
     */
    setupScrollSpy: function() {
        const contentArea = document.getElementById('content');
        if (!contentArea) return;

        const self = this;

        const options = {
            root: contentArea,
            // Use a negative bottom margin so the element is considered 'in view'
            // when it rises into the top portion of the content area. Keep it
            // moderate so small slivers don't trigger selection.
            rootMargin: '0px 0px -50% 0px',
            // Multiple thresholds let us know how much of the element is visible
            threshold: [0, 0.25, 0.5, 0.75, 1]
        };

        const observer = new IntersectionObserver((entries) => {
            if (document.documentElement.getAttribute('data-view-mode') === 'focused') return;

            // If the user is scrolled to very near the top, prefer the first
            // topic — IntersectionObserver can report a tiny sliver of the
            // next section as intersecting which leads to the wrong active item.
            if (contentArea.scrollTop <= 8) {
                const first = document.querySelector('.topic-section');
                if (first && first.id) {
                    self.syncSidebarActiveState(first.id);
                }
                return;
            }

            // From all intersecting entries, choose the one with the largest
            // intersectionRatio (most visible) — this avoids selecting a tiny
            // sliver at the top when the next topic is predominantly on-screen.
            const visible = entries.filter(e => e.isIntersecting);
            if (!visible || visible.length === 0) return;

            let best = visible[0];
            for (let i = 1; i < visible.length; i++) {
                if ((visible[i].intersectionRatio || 0) > (best.intersectionRatio || 0)) {
                    best = visible[i];
                }
            }
            if (best && best.target && best.target.id) {
                self.syncSidebarActiveState(best.target.id);
            }
        }, options);

        // Helper: when content isn't scrollable or when at the very top, ensure
        // the first topic is marked active.
        const updateActiveOnTopOrNot = () => {
            if (contentArea.scrollHeight <= contentArea.clientHeight || contentArea.scrollTop <= 8) {
                const first = document.querySelector('.topic-section');
                if (first && first.id) {
                    self.syncSidebarActiveState(first.id);
                    return true;
                }
            }
            return false;
        };

        // Initial check: non-scrollable pages or already-at-top state.
        updateActiveOnTopOrNot();

        // Keep checks on scroll/resize so the sidebar stays correct when the
        // user reaches the top or the viewport changes size.
        contentArea.addEventListener('scroll', () => updateActiveOnTopOrNot());
        window.addEventListener('resize', () => updateActiveOnTopOrNot());

        document.querySelectorAll('.topic-section').forEach(section => observer.observe(section));
    },

    /**
     * Saves last visited path per mode.
     */
    saveCurrentPageState: function() {
        const path = window.location.pathname;
        if (document.body.classList.contains('home-view')) {
            return;
        }
        if (document.body.classList.contains('mode-atlas')) {
            localStorage.setItem('atlas-last-path', path);
        } else if (document.body.classList.contains('mode-course')) {
            localStorage.setItem('course-last-path', path);
        } else if (document.body.classList.contains('mode-meta')) {
            // Persist last visited page for Meta mode
            localStorage.setItem('meta-last-path', path);
        }
    },

    /**
     * Intercepts mode switches to use last visited paths.
     */
    setupPersistentModeSwitcher: function() {
        // Sidebar mode links should always open mode index pages.
        // Keep last-path restoration only for any legacy header toggles.
        const modeSelectors = document.querySelectorAll('.mode-toggles .toggle');
        modeSelectors.forEach(btn => {
            const text = btn.innerText.toLowerCase();
            const mode = text.trim(); // e.g., 'atlas', 'course', 'meta'
            const lastPath = localStorage.getItem(`${mode}-last-path`);
            if (lastPath && btn.href) {
                // Update the href to the last visited path for this mode
                btn.href = lastPath;
            }
        });
        
        // Wire up logo click to toggle mode switcher details.
        const logo = document.querySelector('.logo-with-modes .logo');
        const modeSwitcher = document.querySelector('.mode-switcher');
        if (logo && modeSwitcher) {
            logo.addEventListener('click', (e) => {
                e.preventDefault();
                modeSwitcher.open = !modeSwitcher.open;
            });

            window.addEventListener('resize', () => this.positionModeMenuUnderModeLabel());
        }
    },

    /**
     * App Initialization.
     */
    init: function() {
        // Theme and View attributes are handled in <head> blocking script.
        const theme = document.documentElement.getAttribute('data-theme') || 'dark';
        const view = document.documentElement.getAttribute('data-view-mode') || 'all';
        const density = localStorage.getItem('atlas-sidebar-density') || 'high';

        this.updateIcons(theme);
        this.updateViewModeUI(view);
        this.updateDensityUI(density);

        // Render style-picker icons
        document.querySelectorAll('.style-dot').forEach(btn => {
            const s = btn.dataset.style;
            if (s && this.icons.style[s]) btn.innerHTML = this.icons.style[s];
        });

        if (window.hljs) {
            hljs.configure({ ignoreUnescapedHTML: true });
        }

        this.setupScrollSpy();
        this.saveCurrentPageState();
        this.updateModeTitle(this.getDisplayedMode());
        this.ensureModeSwitcher();
        this.setupProjectSidebarModes();
        this.hideTopModeLinks();
        this.setupPersistentModeSwitcher();

        // If the user had the Showcases nav open, restore it on page load so
        // selecting a showcase keeps the navigation in the Showcases view.
        try {
            const mode = this.getCurrentMode();
            if (localStorage.getItem(`${mode}-showcases-open`) === '1') {
                setTimeout(() => this.openShowcases({ noNavigate: true }), 100);
            }
            // Restore any generic collection submenus that were left open.
            // The builder emits lists with ids like `toc-collection-{mode}-{key}`.
            try {
                document.querySelectorAll('[id^="toc-collection-"]').forEach(el => {
                    const id = el.id; // toc-collection-{mode}-{key}
                    const parts = id.split('-');
                    // parts: ['toc','collection','{mode}','{key}'] (key may contain additional dashes)
                    if (parts.length >= 4) {
                        const cmode = parts[2];
                        const ckey = parts.slice(3).join('-');
                        if (localStorage.getItem(`${cmode}-collection-${ckey}-open`) === '1') {
                            setTimeout(() => this.openCollection(cmode, ckey, { noNavigate: true }), 120);
                        }
                    }
                });
            } catch (e) {}
        } catch (e) {}

        if (window.location.hash) {
            const hashId = window.location.hash.substring(1);
            setTimeout(() => this.focusTopic(hashId), 500);
        }
    }
};

// Start App
document.addEventListener('DOMContentLoaded', () => {
    app.init();
    
    // Register Service Worker for PWA offline support
    if ('serviceWorker' in navigator) {
        const assetPrefix = document.documentElement.getAttribute('data-asset-prefix') || './';
        navigator.serviceWorker.register(`${assetPrefix}assets/js/service_worker.js`)
            .then(registration => {
                console.log('[PWA] Service Worker registered:', registration);
                
                // Check for updates periodically
                setInterval(() => {
                    registration.update().catch(error => 
                        console.error('[PWA] Update check failed:', error)
                    );
                }, 60000); // Check every minute
            })
            .catch(error => console.error('[PWA] Service Worker registration failed:', error));
    }
});

// Global exposure
window.app = app;