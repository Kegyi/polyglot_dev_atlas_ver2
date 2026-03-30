/**
 * UI Utilities for theme, palette, and sidebar management.
 */

function toggleTheme() {
    const current = document.body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', next);
    // Save preference
    localStorage.setItem('atlas-theme', next);
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
    // Load saved preferences
    const savedTheme = localStorage.getItem('atlas-theme') || 'dark';
    const savedPalette = localStorage.getItem('atlas-palette') || 'zinc';
    
    document.body.setAttribute('data-theme', savedTheme);
    document.body.setAttribute('data-palette', savedPalette);
    
    // Highlight the correct palette dot
    const activeDot = document.querySelector(`.dot-${savedPalette}`);
    if (activeDot) activeDot.classList.add('active');

    // Initialize State
    if (window.AtlasState) AtlasState.init();
});