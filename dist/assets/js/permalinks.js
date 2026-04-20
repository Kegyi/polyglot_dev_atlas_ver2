/*
 * Permalink UX
 * - Clicking permalink copies full URL
 * - Prevents parent header toggle side effects
 * - Highlights hash target on load/hashchange
 */

(function () {
    const FLASH_CLASS = 'hash-target-flash';
    const COPIED_CLASS = 'permalink-copied';

    function buildAbsoluteHashUrl(hash) {
        const base = window.location.href.split('#')[0];
        return base + hash;
    }

    function flashTargetByHash(hash) {
        if (!hash || hash.length < 2) return;
        const id = decodeURIComponent(hash.slice(1));
        const target = document.getElementById(id);
        if (!target) return;

        target.classList.remove(FLASH_CLASS);
        // Force reflow so repeated hash changes retrigger animation.
        void target.offsetWidth;
        target.classList.add(FLASH_CLASS);

        setTimeout(() => {
            target.classList.remove(FLASH_CLASS);
        }, 1800);
    }

    async function copyText(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(text);
            return true;
        }

        // Fallback for older environments.
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'fixed';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        let ok = false;
        try {
            ok = document.execCommand('copy');
        } catch (e) {
            ok = false;
        }
        document.body.removeChild(ta);
        return ok;
    }

    function markCopied(anchor) {
        anchor.classList.add(COPIED_CLASS);
        const original = anchor.getAttribute('aria-label') || 'Link to section';
        anchor.setAttribute('aria-label', 'Copied link');
        setTimeout(() => {
            anchor.classList.remove(COPIED_CLASS);
            anchor.setAttribute('aria-label', original);
        }, 900);
    }

    function setupPermalinkClicks() {
        document.addEventListener('click', async (e) => {
            const anchor = e.target.closest('.topic-permalink, .inline-permalink');
            if (!anchor) return;

            const href = anchor.getAttribute('href') || '';
            if (!href.startsWith('#')) return;

            e.preventDefault();
            e.stopPropagation();

            const fullUrl = buildAbsoluteHashUrl(href);
            const copied = await copyText(fullUrl);
            if (copied) {
                markCopied(anchor);
            }

            if (window.location.hash !== href) {
                history.replaceState(null, '', href);
            }
            flashTargetByHash(href);
        });
    }

    function init() {
        setupPermalinkClicks();
        if (window.location.hash) {
            setTimeout(() => flashTargetByHash(window.location.hash), 120);
        }
    }

    window.addEventListener('hashchange', () => {
        flashTargetByHash(window.location.hash);
    });

    document.addEventListener('DOMContentLoaded', init);
})();
