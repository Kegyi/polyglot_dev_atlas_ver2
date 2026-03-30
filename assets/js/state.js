const AtlasState = {
    primary: null,   // Left Slot
    secondary: null, // Right Slot

    setPrimary(langId) {
        if (this.secondary === langId) {
            this.swap(); // Swap if selecting same lang for opposite slot
        } else {
            this.primary = (this.primary === langId) ? null : langId;
        }
        this.syncUI();
    },

    setSecondary(langId) {
        if (this.primary === langId) {
            this.swap();
        } else {
            this.secondary = (this.secondary === langId) ? null : langId;
        }
        this.syncUI();
    },

    swap() {
        [this.primary, this.secondary] = [this.secondary, this.primary];
        this.syncUI();
    },

    syncUI() {
        const isComparing = (this.primary && this.secondary);
        const hasSelection = (this.primary || this.secondary);

        // Toggle the 'is-comparing' class on body for CSS Grid
        document.body.classList.toggle('is-comparing', isComparing);

        // Update button highlights
        document.querySelectorAll('.lang-btn').forEach(btn => {
            const id = btn.dataset.lang;
            btn.classList.remove('active-l', 'active-r');
            if (id === this.primary) btn.classList.add('active-l');
            if (id === this.secondary) btn.classList.add('active-r');
        });

        // Handle Column Visibility
        document.querySelectorAll('[data-column-lang]').forEach(col => {
            const lang = col.dataset.columnLang;
            
            // IF no selection: Show Everything (Initial Preview)
            // IF selection: Show only the selected ones
            if (!hasSelection) {
                col.style.display = 'block'; 
                if (col.tagName === 'TD' || col.tagName === 'TH') col.style.display = 'table-cell';
            } else {
                const isVisible = (lang === this.primary || lang === this.secondary);
                col.style.display = isVisible ? 'block' : 'none';
                if ((col.tagName === 'TD' || col.tagName === 'TH') && isVisible) {
                    col.style.display = 'table-cell';
                }
            }
        });
    }
};

// Initialize listeners
document.addEventListener('DOMContentLoaded', () => {
    const picker = document.getElementById('language-picker');
    
    // Handle Clicks
    picker.addEventListener('click', (e) => {
        const btn = e.target.closest('.lang-btn');
        if (!btn) return;
        AtlasState.setPrimary(btn.dataset.lang);
    });

    // Handle Right-Clicks
    picker.addEventListener('contextmenu', (e) => {
        const btn = e.target.closest('.lang-btn');
        if (!btn) return;
        e.preventDefault(); // Stop default context menu
        AtlasState.setSecondary(btn.dataset.lang);
    });
});