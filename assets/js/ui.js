/**
 * UI Utilities for theme, palette, and sidebar management.
 */

function toggleTheme() {
    const current = document.body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', next);
    // Save preference
    localStorage.setItem('atlas-theme', next);
    // Toggle HLJS theme CSS if present
    try {
        const hljsDark = document.getElementById('hljs-theme-dark');
        const hljsLight = document.getElementById('hljs-theme-light');
        if (hljsDark && hljsLight) {
            if (next === 'light') {
                hljsDark.disabled = true;
                hljsLight.disabled = false;
            } else {
                hljsDark.disabled = false;
                hljsLight.disabled = true;
            }
        }
    } catch (e) { console.warn('hljs theme toggle error', e); }

    // Re-run highlight to ensure styles apply
    if (window.hljs && typeof hljs.highlightAll === 'function') {
        try { hljs.highlightAll(); } catch (e) { console.warn('hljs.highlightAll failed', e); }
    }
}

function setPalette(p, el) {
    document.body.setAttribute('data-palette', p);
    document.querySelectorAll('.palette-dot').forEach(d => d.classList.remove('active'));
    if (el) el.classList.add('active');
    localStorage.setItem('atlas-palette', p);
}

function toggleSolution(btn) {
    const sol = btn.nextElementSibling;
    const isHidden = sol.style.display === 'none' || sol.style.display === '';
    sol.style.display = isHidden ? 'block' : 'none';
    btn.innerText = isHidden ? 'Hide Solution' : 'Show Solution';
}

// Initialize on Load
document.addEventListener('DOMContentLoaded', () => {
    // Initialize State first so it can update localStorage if needed
    console.log('ui.js: localStorage before AtlasState.init', {
        'atlas-theme': localStorage.getItem('atlas-theme'),
        'atlas-primary': localStorage.getItem('atlas-primary'),
        'atlas-secondary': localStorage.getItem('atlas-secondary')
    });
    if (window.AtlasState) AtlasState.init();
    console.log('ui.js: localStorage after AtlasState.init', {
        'atlas-theme': localStorage.getItem('atlas-theme'),
        'atlas-primary': localStorage.getItem('atlas-primary'),
        'atlas-secondary': localStorage.getItem('atlas-secondary')
    });

    // Load saved preferences (read after AtlasState.init so any writes are visible)
    const savedTheme = localStorage.getItem('atlas-theme') || 'dark';
    const savedPalette = localStorage.getItem('atlas-palette') || 'zinc';

    document.body.setAttribute('data-theme', savedTheme);
    document.body.setAttribute('data-palette', savedPalette);

    // Highlight the correct palette dot
    const activeDot = document.querySelector(`.dot-${savedPalette}`);
    if (activeDot) activeDot.classList.add('active');

    // Mode toggle: set active button based on current URL
    function updateModeToggle() {
        const atlasBtn = document.getElementById('btn-atlas');
        const courseBtn = document.getElementById('btn-course');
        if (!atlasBtn || !courseBtn) return;

        atlasBtn.classList.remove('active');
        courseBtn.classList.remove('active');

        const href = window.location.pathname + window.location.search + window.location.hash;
        if (href.includes('/course/') || href.includes('/course_') || href.includes('course_dashboard')) {
            courseBtn.classList.add('active');
        } else {
            atlasBtn.classList.add('active');
        }
    }

    updateModeToggle();

    // Update immediately on click so UI responds before navigation
    const atlasBtn = document.getElementById('btn-atlas');
    const courseBtn = document.getElementById('btn-course');
    if (atlasBtn) atlasBtn.addEventListener('click', () => { atlasBtn.classList.add('active'); courseBtn && courseBtn.classList.remove('active'); });
    if (courseBtn) courseBtn.addEventListener('click', () => { courseBtn.classList.add('active'); atlasBtn && atlasBtn.classList.remove('active'); });

    // Toggle HLJS theme links according to current theme
    try {
        const hljsDark = document.getElementById('hljs-theme-dark');
        const hljsLight = document.getElementById('hljs-theme-light');
        if (hljsDark && hljsLight) {
            if (savedTheme === 'light') {
                hljsDark.disabled = true;
                hljsLight.disabled = false;
            } else {
                hljsDark.disabled = false;
                hljsLight.disabled = true;
            }
        }
    } catch (e) {
        console.warn('HLJS theme toggle failed', e);
    }

    // Initialize highlight.js if present
    if (window.hljs && typeof hljs.highlightAll === 'function') {
        try { hljs.highlightAll(); } catch (e) { console.warn('hljs.highlightAll failed', e); }
    }
});