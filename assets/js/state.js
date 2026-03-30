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

        // 1. Body Class for Grid Layout
        document.body.classList.toggle('is-comparing', isComparing);

        // 2. Header Slot Visuals
        const slotL = document.getElementById('slot-l');
        const slotR = document.getElementById('slot-r');

        if (slotL) {
            slotL.innerText = this.primary ? this.primary.toUpperCase() : "Primary Slot";
            slotL.className = `slot ${this.primary ? 'active-l' : ''}`;
        }
        if (slotR) {
            slotR.innerText = this.secondary ? this.secondary.toUpperCase() : "Secondary Slot";
            slotR.className = `slot ${this.secondary ? 'active-r' : ''}`;
        }

        // 3. Language Picker Button Highlights
        document.querySelectorAll('.lang-btn').forEach(btn => {
            const id = btn.dataset.lang;
            btn.classList.remove('active-l', 'active-r');
            if (id === this.primary) btn.classList.add('active-l');
            if (id === this.secondary) btn.classList.add('active-r');
        });

        // 4. Content Visibility (Tables & Code Blocks)
        document.querySelectorAll('[data-column-lang]').forEach(el => {
            const lang = el.dataset.columnLang;

            // Logic: 
            // - If nothing is selected: Show everything (Preview Mode)
            // - If selection exists: Show only what is in Slot L or Slot R
            if (!hasSelection) {
                el.style.display = (el.tagName === 'TD' || el.tagName === 'TH') ? 'table-cell' : 'block';
            } else {
                const isVisible = (lang === this.primary || lang === this.secondary);
                
                if (isVisible) {
                    el.style.display = (el.tagName === 'TD' || el.tagName === 'TH') ? 'table-cell' : 'block';
                } else {
                    el.style.display = 'none';
                }
            }
        });

        // 5. Swap Button Visibility
        const swapBtn = document.getElementById('swap-btn');
        if (swapBtn) {
            swapBtn.style.visibility = isComparing ? 'visible' : 'hidden';
        }
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