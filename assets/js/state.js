const AtlasState = {
    l: null, 
    r: null,

    init() {
        // 1. Try to load from memory first
        this.l = localStorage.getItem('atlas_primary');
        this.r = localStorage.getItem('atlas_secondary');

        // 2. Fallback: If no memory, pick the first button available
        if (!this.l) {
            const firstBtn = document.querySelector('.lang-btn');
            if (firstBtn) this.l = firstBtn.id.replace('btn-', '');
        }
        
        this.updateUI();
    },

    select(id, side) {
        if (side === 'l') {
            if (this.r === id) { this.swap(); return; }
            if (this.l === id) {
                if (this.r) { this.l = this.r; this.r = null; }
            } else { this.l = id; }
        } else {
            if (this.l === id) { this.swap(); return; }
            this.r = (this.r === id) ? null : id;
        }
        this.updateUI();
    },

    swap() {
        if (this.r && this.l) {
            [this.l, this.r] = [this.r, this.l];
            this.updateUI();
        }
    },

    updateUI() {
        // Save to memory for the next page load
        if (this.l) localStorage.setItem('atlas_primary', this.l);
        else localStorage.removeItem('atlas_primary');
        
        if (this.r) localStorage.setItem('atlas_secondary', this.r);
        else localStorage.removeItem('atlas_secondary');

        // --- Visual Sync ---
        const sL = document.getElementById('slot-l');
        const sR = document.getElementById('slot-r');
        if (sL) sL.innerText = this.l ? this.l.toUpperCase() : "Primary";
        if (sR) {
            sR.innerText = this.r ? this.r.toUpperCase() : "";
            sR.style.display = this.r ? 'flex' : 'none';
        }

        const swapBtn = document.getElementById('swap-btn');
        if (swapBtn) swapBtn.style.visibility = (this.l && this.r) ? 'visible' : 'hidden';

        document.body.classList.toggle('is-comparing', !!(this.l && this.r));

        document.querySelectorAll('.lang-btn').forEach(btn => {
            const id = btn.id.replace('btn-', '');
            btn.classList.remove('active-l', 'active-r');
            if (id === this.l) btn.classList.add('active-l');
            if (id === this.r) btn.classList.add('active-r');
        });

        document.querySelectorAll('.code-card, [data-lang]').forEach(el => {
            const lang = el.getAttribute('data-lang');
            const isVisible = (lang === this.l || lang === this.r);
            el.classList.remove('visible', 'order-1', 'order-2');
            if (lang === this.l) {
                el.classList.add('visible', 'order-1');
                el.style.display = (el.tagName.startsWith('T')) ? 'flex' : 'flex';
            } else if (lang === this.r) {
                el.classList.add('visible', 'order-2');
                el.style.display = (el.tagName.startsWith('T')) ? 'flex' : 'flex';
            } else { el.style.display = 'none'; }
        });
    }
};