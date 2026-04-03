/**
 * Polyglot Atlas - General UI Controller (Phase 3)
 * Handles Theme, Palette, Global Design Style, Sidebars, View Modes, 
 * Topic Navigation, Scroll-Spy, and Mode-Specific Page Persistence.
 */

const app = {
    icons: {
        theme: {
            dark: '<svg viewBox="0 0 24 24" width="18" height="18" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
            light: '<svg viewBox="0 0 24 24" width="18" height="18" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
        },
        style: {
            sharp: '<svg viewBox="0 0 24 24" width="14" height="14" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>',
            round: '<svg viewBox="0 0 24 24" width="14" height="14" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><circle cx="12" cy="12" r="8"/></svg>',
            airy: '<svg viewBox="0 0 24 24" width="14" height="14" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><path d="M19 17H6a4 4 0 1 1 .5-7.9A6 6 0 1 1 19 17z"/></svg>'
        }
    },
    /**
     * Toggles between Dark and Light mode.
     * Updates HLJS theme CSS path dynamically.
     */
    toggleTheme: function() {
        const html = document.documentElement;
        const target = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        
        html.setAttribute('data-theme', target);
        localStorage.setItem('atlas-theme', target);
        this.updateIcons(target);

        const hljsLink = document.getElementById('hljs-theme');
        if (hljsLink) {
            const currentHref = hljsLink.href;
            const newFile = target === 'dark' ? 'atom-one-dark.min.css' : 'github.min.css';
            const pathParts = hljsLink.href.split('/');
            pathParts[pathParts.length - 1] = newFile;
            hljsLink.href = pathParts.join('/');
        }
    },

    updateIcons: function(theme) {
        const btn = document.getElementById('theme-toggle');
        if (btn) btn.innerHTML = theme === 'dark' ? this.icons.theme.dark : this.icons.theme.light;
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

    updateViewModeUI: function(mode) {
        const btn = document.getElementById('view-mode-btn');
        if (btn) btn.innerText = mode === 'all' ? 'All' : 'Focus';
    },

    /**
     * Showcases navigation helpers: swap main nav for showcases list and back.
     */
    openShowcases: function() {
        const main = document.getElementById('toc-main');
        const shows = document.getElementById('toc-showcases');
        if (!shows || !main) return;
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
                if (!isOnShowcases) {
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
        const modeBtns = document.querySelectorAll('.mode-toggles .toggle');
        modeBtns.forEach(btn => {
            const text = btn.innerText.toLowerCase(); 
            const lastPath = localStorage.getItem(`${text}-last-path`);
            if (lastPath) {
                btn.setAttribute('href', lastPath);
            } else {
                // No stored selection: persist the current target as the default for this mode
                // This makes the top page the default choice for future mode switches.
                const target = btn.getAttribute('href');
                if (target) localStorage.setItem(`${text}-last-path`, target);
            }
        });
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
        this.setupPersistentModeSwitcher();

        // If the user had the Showcases nav open, restore it on page load so
        // selecting a showcase keeps the navigation in the Showcases view.
        try {
            const mode = this.getCurrentMode();
            if (localStorage.getItem(`${mode}-showcases-open`) === '1') {
                setTimeout(() => this.openShowcases(), 100);
            }
        } catch (e) {}

        if (window.location.hash) {
            const hashId = window.location.hash.substring(1);
            setTimeout(() => this.focusTopic(hashId), 500);
        }
    }
};

// Start App
document.addEventListener('DOMContentLoaded', () => app.init());

// Global exposure
window.app = app;