/**
 * Polyglot Dev Atlas - Main Runtime Logic
 * Handles UI state: Sidebars, Palettes, Language Selection, and Comparison View.
 */

import { i18n } from './i18n.js';

const STATE_KEYS = {
    theme: 'theme',
    palette: 'palette',
    sidebarL: 'sidebar-l',
    sidebarR: 'sidebar-r',
    viewMode: 'view-mode',
    langL: 'selected-lang-l',
    langR: 'selected-lang-r'
};

/**
 * Initialize Application
 */
async function init() {
    try {
        // 1. Sync UI markers with the state set by the blocking head script
        syncActivePaletteIndicator();
        syncLanguagePills();

        // 2. Setup Runtime Event Listeners
        setupEventListeners();

        // 2.5 Apply view mode state early so initial render reflects saved preference
        applyViewModeState();

        // 3. Load Translations & Reveal Page
        const savedLang = localStorage.getItem('app-lang') || 'en';
        await i18n.load(savedLang);

        revealPage();
    } catch (err) {
        console.error("Initialization error:", err);
        revealPage();
    }
}

function setupEventListeners() {
    // Programming Language Selector Pills
    document.querySelectorAll('.lang-pill').forEach(pill => {
        pill.addEventListener('click', () => handleLanguageSelection(pill));
    });

    // Mode Switcher tracking
    document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.documentElement.classList.add('is-loading');
        });
    });

    // View mode toggle in the topic sidebar (if present)
    const vm = document.getElementById('viewModeToggle');
    if (vm) vm.addEventListener('click', () => {
        // delegate to app.toggleViewMode
        window.app.toggleViewMode();
    });
}

/**
 * Sidebar Toggle Logic (Left/Right)
 */
window.app = window.app || {};
window.app.toggleSidebar = function(side) {
    const html = document.documentElement;
    const attr = `data-sidebar-${side}`;
    const storageKey = side === 'l' ? STATE_KEYS.sidebarL : STATE_KEYS.sidebarR;
    
    const isVisible = html.getAttribute(attr) === 'visible';
    const nextState = isVisible ? 'hidden' : 'visible';
    
    html.setAttribute(attr, nextState);
    localStorage.setItem(storageKey, nextState);

    // Update edge toggle arrow text
    const btn = document.querySelector(`.toggle-${side}`);
    if (side === 'l') {
        btn.innerText = nextState === 'visible' ? '◀' : '▶';
    } else {
        btn.innerText = nextState === 'visible' ? '▶' : '◀';
    }
};

/**
 * Color Palette Logic
 */
window.app.setPalette = function(palette, el) {
    document.documentElement.setAttribute('data-palette', palette);
    localStorage.setItem(STATE_KEYS.palette, palette);
    
    document.querySelectorAll('.pal-indicator').forEach(i => i.classList.remove('active'));
    if (el) el.classList.add('active');
};

/**
 * Theme Toggle (Light/Dark) Logic
 */
window.app.toggleTheme = function() {
    const html = document.documentElement;
    const current = html.getAttribute('data-theme');
    const target = current === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', target);
    localStorage.setItem(STATE_KEYS.theme, target);
    
    const icon = document.getElementById('themeIcon');
    if (icon) icon.innerText = target === 'dark' ? '☼' : '☾';
};

function syncActivePaletteIndicator() {
    const activePal = document.documentElement.getAttribute('data-palette');
    const selector = `.p-${activePal.substring(0, 3)}`;
    const el = document.querySelector(selector);
    if (el) el.classList.add('active');
}

/**
 * Programming Language Selection & Comparison View Logic
 */
function handleLanguageSelection(pill) {
    const langId = pill.getAttribute('data-lang-id');
    let left = localStorage.getItem(STATE_KEYS.langL);
    let right = localStorage.getItem(STATE_KEYS.langR);

    if (langId === left) {
        left = null; // Deselect
    } else if (langId === right) {
        right = null; // Deselect
    } else {
        // Selection queue: Fill left first, then right
        if (!left) {
            left = langId;
        } else if (!right) {
            right = langId;
        } else {
            // Both slots full: Shift left out and replace right
            left = right;
            right = langId;
        }
    }

    localStorage.setItem(STATE_KEYS.langL, left || "");
    localStorage.setItem(STATE_KEYS.langR, right || "");
    
    syncLanguagePills();
    updateComparisonUI(left, right);
}

function syncLanguagePills() {
    const left = localStorage.getItem(STATE_KEYS.langL);
    const right = localStorage.getItem(STATE_KEYS.langR);

    document.querySelectorAll('.lang-pill').forEach(pill => {
        const id = pill.getAttribute('data-lang-id');
        pill.classList.remove('sel-l', 'sel-r');
        if (id === left) pill.classList.add('sel-l');
        else if (id === right) pill.classList.add('sel-r');
    });
}

window.app.swapLanguages = function() {
    const left = localStorage.getItem(STATE_KEYS.langL);
    const right = localStorage.getItem(STATE_KEYS.langR);
    
    localStorage.setItem(STATE_KEYS.langL, right || "");
    localStorage.setItem(STATE_KEYS.langR, left || "");
    
    syncLanguagePills();
    updateComparisonUI(right, left);
};

function updateComparisonUI(left, right) {
    // Toggle card visibility and coloring
    document.querySelectorAll('.code-card').forEach(card => {
        const lang = card.getAttribute('data-lang');
        card.style.display = 'none';
        card.classList.remove('card-l', 'card-r');

        if (lang === left) {
            card.style.display = 'block';
            card.classList.add('card-l');
        }
        if (lang === right) {
            card.style.display = 'block';
            card.classList.add('card-r');
        }
    });

    // Adjust grid columns: 1fr for single, 1fr 1fr for comparison
    const grids = document.querySelectorAll('.comparison-grid');
    grids.forEach(g => {
        if (left && right) {
            g.style.gridTemplateColumns = '1fr 1fr';
        } else {
            g.style.gridTemplateColumns = '1fr';
        }
    });
}

/**
 * View Modes (Focused vs Show All) & Navigation
 */
window.app.toggleViewMode = function() {
    const html = document.documentElement;
    const isFocused = html.getAttribute('data-view-mode') === 'focused';
    const nextMode = isFocused ? 'all' : 'focused';
    html.setAttribute('data-view-mode', nextMode);
    localStorage.setItem(STATE_KEYS.viewMode, nextMode);
    applyViewModeState();
};

function applyViewModeState() {
    const html = document.documentElement;
    const mode = html.getAttribute('data-view-mode') || 'all';
    const vmBtn = document.getElementById('viewModeToggle');
    if (vmBtn) vmBtn.innerText = mode === 'focused' ? 'Focused' : 'All';

    if (mode === 'focused') {
        // find currently active sidebar item, else pick first topic-section
        const activeLi = document.querySelector('#toc li.active') || document.querySelector('#toc li[data-topic-id]');
        if (activeLi) {
            const tid = activeLi.getAttribute('data-topic-id');
            if (tid) {
                // focusTopic will handle showing only the focused section
                window.app.focusTopic(tid);
                return;
            }
        }
        // fallback: hide all topics (bodies will be collapsed)
        document.querySelectorAll('.topic-section').forEach(s => {
            s.classList.remove('active');
            const b = s.querySelector('.topic-body');
            if (b) { b.classList.add('collapsed'); b.style.display = 'none'; }
        });
    } else {
        // show all topics
        document.querySelectorAll('.topic-section').forEach(s => {
            s.classList.add('active');
            const b = s.querySelector('.topic-body');
            if (b) { b.classList.remove('collapsed'); b.style.display = ''; }
        });
    }
}

window.app.focusTopic = function(id) {
    const html = document.documentElement;
    const isFocused = html.getAttribute('data-view-mode') === 'focused';
    
    // Sidebar active state
    document.querySelectorAll('#toc li').forEach(li => li.classList.remove('active'));
    const sel = document.querySelector(`#toc li[data-topic-id="${id}"]`);
    if (sel) sel.classList.add('active');

    const target = document.getElementById(id);
    if (!target) return;

    if (isFocused) {
        // Clear previous active flags
        document.querySelectorAll('.topic-section').forEach(s => s.classList.remove('active'));

        // Activate the target and ensure its body is visible
        target.classList.add('active');
        target.classList.remove('is-collapsed');
        const tb = target.querySelector('.topic-body');
        if (tb) { tb.classList.remove('collapsed'); tb.style.display = 'block'; }

        // Also expand any ancestor topic-sections so nested topics are visible
        let node = target.parentElement;
        while (node) {
            if (node.classList && node.classList.contains('topic-section')) {
                node.classList.add('active');
                node.classList.remove('is-collapsed');
                const ab = node.querySelector('.topic-body');
                if (ab) { ab.classList.remove('collapsed'); ab.style.display = 'block'; }
            }
            node = node.parentElement;
        }

        // Ensure descendant topic-sections inside the selected topic are also visible
        target.querySelectorAll('.topic-section').forEach(desc => {
            desc.classList.add('active');
            desc.classList.remove('is-collapsed');
            const db = desc.querySelector('.topic-body');
            if (db) { db.classList.remove('collapsed'); db.style.display = 'block'; }
        });

        document.getElementById('main-scroll-area').scrollTo(0, 0);
    } else {
        // Highlighting animation in 'all' mode
        target.classList.add('highlight');
        target.scrollIntoView({ behavior: 'smooth' });
        setTimeout(() => target.classList.remove('highlight'), 2000);
    }
};

/**
 * Convenience Toggle (Header click)
 */
window.app.toggleTopic = function(id) {
    const sec = document.getElementById(id);
    if (!sec) return;
    sec.querySelector('.topic-body').classList.toggle('collapsed');
    sec.classList.toggle('is-collapsed');
};

/**
 * Final Reveal of the Page
 */
function revealPage() {
    const left = localStorage.getItem(STATE_KEYS.langL);
    const right = localStorage.getItem(STATE_KEYS.langR);
    updateComparisonUI(left, right);
    
    setTimeout(() => {
        document.documentElement.classList.remove('is-loading');
    }, 50);
}

// Execution
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}