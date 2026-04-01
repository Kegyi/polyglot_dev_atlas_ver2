/**
 * Polyglot i18n Engine
 * Handles fetching JSON locales and injecting them into the DOM.
 */

export class I18nEngine {
    constructor() {
        this.translations = {};
        this.currentLang = 'en';
    }

    /**
     * Loads a language JSON file and applies it to the page.
     * @param {string} lang - The language code (e.g., 'en', 'hu').
     */
    async load(lang) {
        this.currentLang = lang;
        
        try {
            // Path is relative to the generated HTML file's location.
            // Our builder ensures content/locales is available in the dist root.
            const response = await fetch(`./content/locales/${lang}.json`);
            
            if (!response.ok) {
                throw new Error(`Could not load locale: ${lang}`);
            }

            this.translations = await response.json();
            
            // Apply the translations to the DOM
            this.translatePage();
            
            return true;
        } catch (error) {
            console.error("i18n Engine Error:", error);
            // Return true anyway to allow the 'revealPage' logic in main.js to proceed
            return false;
        }
    }

    /**
     * Scans the DOM for [data-i18n] attributes and replaces content.
     */
    translatePage() {
        const elements = document.querySelectorAll('[data-i18n]');
        
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            const translation = this.getNestedValue(this.translations, key);

            if (translation) {
                this.applyTranslation(el, translation);
            }
        });

        // Sync HTML lang attribute
        document.documentElement.setAttribute('lang', this.currentLang);
    }

    /**
     * Determines how to apply the translation based on element type.
     */
    applyTranslation(el, text) {
        // Handle Input/Textarea Placeholders
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
            el.placeholder = text;
        } 
        // Handle Image Alt text
        else if (el.tagName === 'IMG') {
            el.alt = text;
        }
        // Handle Standard Elements (Supports HTML for formatting)
        else {
            el.innerHTML = text;
        }
    }

    /**
     * Resolves nested JSON keys (e.g., "comparison.loops.title")
     */
    getNestedValue(obj, path) {
        return path.split('.').reduce((prev, curr) => {
            return prev ? prev[curr] : null;
        }, obj);
    }
}

// Export a singleton instance
export const i18n = new I18nEngine();