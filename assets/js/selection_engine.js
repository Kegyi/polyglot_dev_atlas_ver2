/**
 * Polyglot Atlas - Selection Engine
 * Handles logic for Single/Double view, mouse selection matrix, drag support,
 * and persistent state via root attributes for zero-flicker rendering.
 */

const AtlasState = {
    viewMode: 'single',      // 'single' | 'double'
    primaryLang: null,       // Slot 1
    secondaryLang: null,     // Slot 2
    languages: [],           // List of all lang IDs on page
    dragButton: null         // Tracking 0 (Left) or 2 (Right)
};

document.addEventListener('DOMContentLoaded', () => {
    initSelectionEngine();
});

/**
 * Loads state from LocalStorage and sets up the environment.
 */
function initSelectionEngine() {
    const langBtns = document.querySelectorAll('.lang-btn');
    if (langBtns.length === 0) return;

    // 1. Map available languages from the DOM
    AtlasState.languages = Array.from(langBtns).map(btn => btn.dataset.langId);
    
    // 2. Load Persistent State (Keys match base.html script)
    const savedView = localStorage.getItem('atlas-selection-mode');
    const savedPrimary = localStorage.getItem('atlas-primary-lang');
    const savedSecondary = localStorage.getItem('atlas-secondary-lang');

    // Restore View Mode
    AtlasState.viewMode = savedView || 'single';

    // Restore Primary (Verify existence)
    if (savedPrimary && AtlasState.languages.includes(savedPrimary)) {
        AtlasState.primaryLang = savedPrimary;
    } else {
        AtlasState.primaryLang = AtlasState.languages[0];
    }

    // Restore Secondary
    if (savedSecondary && AtlasState.languages.includes(savedSecondary) && savedSecondary !== AtlasState.primaryLang) {
        AtlasState.secondaryLang = savedSecondary;
    } else {
        AtlasState.secondaryLang = null;
    }

    // Logical fallback: Double mode requires two languages
    if (AtlasState.viewMode === 'double' && !AtlasState.secondaryLang) {
        const idx = AtlasState.languages.indexOf(AtlasState.primaryLang);
        AtlasState.secondaryLang = AtlasState.languages[(idx + 1) % AtlasState.languages.length];
    }

    // 3. Attach Event Listeners
    setupGlobalEvents();
    setupLanguageButtonEvents(langBtns);
    
    // 4. Initial Sync (Sets Root Attributes for CSS logic)
    updateUI();
}

function setupGlobalEvents() {
    document.getElementById('view-single-btn')?.addEventListener('click', () => setViewMode('single'));
    document.getElementById('view-double-btn')?.addEventListener('click', () => setViewMode('double'));
    document.getElementById('swap-btn')?.addEventListener('click', swapLanguages);

    window.addEventListener('mouseup', () => { AtlasState.dragButton = null; });
    
    // Prevent text selection during button dragging
    document.querySelector('.lang-selector-list')?.addEventListener('mousedown', (e) => {
        if (e.target.closest('.lang-btn')) e.preventDefault();
    });
}

function setupLanguageButtonEvents(btns) {
    btns.forEach(btn => {
        const langId = btn.dataset.langId;

        btn.addEventListener('mousedown', (e) => {
            AtlasState.dragButton = e.button; 
        });

        btn.addEventListener('click', (e) => {
            e.preventDefault();
            handleSelection(langId, 'left');
        });

        btn.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            handleSelection(langId, 'right');
        });

        btn.addEventListener('mouseenter', (e) => {
            // Drag support: 1 = Left mouse button bitmask, 2 = Right
            if (AtlasState.dragButton === 0 && (e.buttons & 1)) {
                handleSelection(langId, 'left');
            } else if (AtlasState.dragButton === 2 && (e.buttons & 2)) {
                handleSelection(langId, 'right');
            }
        });
    });
}

/**
 * Core Selection Matrix Logic
 */
function handleSelection(id, actionType) {
    const isP = (id === AtlasState.primaryLang);
    const isS = (id === AtlasState.secondaryLang);

    if (AtlasState.viewMode === 'single') {
        if (actionType === 'left') {
            AtlasState.primaryLang = id;
        } else if (actionType === 'right' && !isP) {
            AtlasState.secondaryLang = id;
            AtlasState.viewMode = 'double';
        }
    } 
    else {
        if (actionType === 'left') {
            if (isP) {
                // Left Click/Drag Active Primary: Secondary -> Primary, Single Mode
                AtlasState.primaryLang = AtlasState.secondaryLang;
                AtlasState.secondaryLang = null;
                AtlasState.viewMode = 'single';
            } else if (isS) {
                swapLanguages();
            } else {
                AtlasState.primaryLang = id;
            }
        } 
        else if (actionType === 'right') {
            if (isP) {
                swapLanguages();
            } else if (isS) {
                // Right Click/Drag Active Secondary: back to Single
                AtlasState.secondaryLang = null;
                AtlasState.viewMode = 'single';
            } else {
                AtlasState.secondaryLang = id;
            }
        }
    }
    updateUI();
}

function setViewMode(mode) {
    AtlasState.viewMode = mode;
    if (mode === 'double' && !AtlasState.secondaryLang) {
        const idx = AtlasState.languages.indexOf(AtlasState.primaryLang);
        AtlasState.secondaryLang = AtlasState.languages[(idx + 1) % AtlasState.languages.length];
    }
    updateUI();
}

function swapLanguages() {
    if (!AtlasState.secondaryLang) return;
    const temp = AtlasState.primaryLang;
    AtlasState.primaryLang = AtlasState.secondaryLang;
    AtlasState.secondaryLang = temp;
    updateUI();
}

/**
 * The "Sync Master"
 * Updates LocalStorage and Root Attributes so CSS can respond instantly.
 */
function updateUI() {
    const doc = document.documentElement;

    // 1. Update Persistent Storage
    localStorage.setItem('atlas-selection-mode', AtlasState.viewMode);
    localStorage.setItem('atlas-primary-lang', AtlasState.primaryLang);
    if (AtlasState.secondaryLang) {
        localStorage.setItem('atlas-secondary-lang', AtlasState.secondaryLang);
    } else {
        localStorage.removeItem('atlas-secondary-lang');
    }

    // 2. Sync Root Attributes (Drives the CSS Zero-Flicker Logic)
    doc.setAttribute('data-selection-mode', AtlasState.viewMode);
    doc.setAttribute('data-primary', AtlasState.primaryLang);
    doc.setAttribute('data-secondary', AtlasState.secondaryLang || "");

    // 3. Navbar Visual States
    document.getElementById('view-single-btn')?.classList.toggle('active', AtlasState.viewMode === 'single');
    document.getElementById('view-double-btn')?.classList.toggle('active', AtlasState.viewMode === 'double');

    // 4. Refresh Content Blocks Display & Highlights
    refreshContentBlocks();
}

function refreshContentBlocks() {
    const containers = document.querySelectorAll('.code-comparison-grid');
    
    containers.forEach(container => {
        // Refresh visibility is handled by CSS attributes, but JS triggers Highlighting
        const blocks = container.querySelectorAll('.code-block');
        blocks.forEach(block => {
            const lang = block.dataset.lang;
            const isPrimary = (lang === AtlasState.primaryLang);
            const isSecondary = (AtlasState.viewMode === 'double' && lang === AtlasState.secondaryLang);
            
            if (isPrimary || isSecondary) {
                // If block is now visible, check if we need to highlight it
                if (window.hljs) {
                    const codeEl = block.querySelector('code');
                    if (codeEl && !codeEl.classList.contains('hljs')) {
                        window.hljs.highlightElement(codeEl);
                    }
                }
                // Maintain slot order: Primary (1) | Secondary (2)
                block.style.order = isPrimary ? "1" : "2";
            }
        });
    });
}