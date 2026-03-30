const AtlasState = {
    l: null, 
    r: null,

    init() {
        // Find the first language button available on the page to use as default
        const firstBtn = document.querySelector('.lang-btn');
        if (firstBtn) {
            // Extract 'cpp' from 'btn-cpp'
            const id = firstBtn.id.replace('btn-', '');
            this.l = id;
        }
        this.updateUI();
    },

    select(id, side) {
        if (side === 'l') {
            if (this.r === id) { this.swap(); return; }
            if (this.l === id) {
                // Promotion: if clicking active primary, move secondary to primary
                if (this.r) { this.l = this.r; this.r = null; }
            } else {
                this.l = id;
            }
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
        // Update Slots
        const sL = document.getElementById('slot-l');
        const sR = document.getElementById('slot-r');
        if (sL) sL.innerText = this.l ? this.l.toUpperCase() : "Select Lang";
        if (sR) {
            sR.innerText = this.r ? this.r.toUpperCase() : "";
            sR.style.display = this.r ? 'flex' : 'none';
        }

        const swapBtn = document.getElementById('swap-btn');
        if (swapBtn) swapBtn.style.visibility = (this.l && this.r) ? 'visible' : 'hidden';

        document.body.classList.toggle('is-comparing', !!(this.l && this.r));

        // Sync Button Highlights
        document.querySelectorAll('.lang-btn').forEach(btn => {
            const id = btn.id.replace('btn-', '');
            btn.classList.remove('active-l', 'active-r');
            if (id === this.l) btn.classList.add('active-l');
            if (id === this.r) btn.classList.add('active-r');
        });

        // Sync Content Display
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
            } else {
                el.style.display = 'none';
            }
        });
    }
};