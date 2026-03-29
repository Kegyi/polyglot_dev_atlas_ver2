// Toggle between Atlas and Course modes
function switchMode(mode) {
    const atlasSidebar = document.getElementById('sidebar-atlas');
    const courseSidebar = document.getElementById('sidebar-course');
    const body = document.body;

    if (mode === 'course') {
        atlasSidebar.style.display = 'none';
        courseSidebar.style.display = 'block';
        body.classList.add('mode-course'); // Use this for CSS theme changes
    } else {
        atlasSidebar.style.display = 'block';
        courseSidebar.style.display = 'none';
        body.classList.remove('mode-course');
    }
}

// Highlight the Topic Sidebar based on scroll position
window.addEventListener('scroll', () => {
    let current = "";
    const blocks = document.querySelectorAll(".page-block");
    
    blocks.forEach(block => {
        const sectionTop = block.offsetTop;
        if (pageYOffset >= sectionTop - 150) {
            current = block.getAttribute("id");
        }
    });

    document.querySelectorAll(".topic-link").forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href").includes(current)) {
            link.classList.add("active");
        }
    });
});

// Update the Body class when comparison state changes
function updateComparisonLayout() {
    const isComparing = (AtlasState.primary && AtlasState.secondary);
    if (isComparing) {
        document.body.classList.add('is-comparing');
    } else {
        document.body.classList.remove('is-comparing');
    }
}

// Call this inside AtlasState.syncUI()

// Theme Toggle Logic
const ThemeManager = {
    init() {
        const savedTheme = localStorage.getItem('atlas-theme') || 'theme-dark';
        document.body.className = savedTheme;
        this.updateIcon();
    },
    toggle() {
        const isDark = document.body.classList.contains('theme-dark');
        const newTheme = isDark ? 'theme-light' : 'theme-dark';
        document.body.className = newTheme;
        localStorage.setItem('atlas-theme', newTheme);
        this.updateIcon();
    },
    updateIcon() {
        const btn = document.getElementById('theme-toggle');
        if (btn) btn.innerText = document.body.classList.contains('theme-light') ? '🌙' : '☀️';
    }
};

// Course Mode Logic
function toggleCourseMode() {
    const isCourse = document.body.classList.toggle('mode-course');
    const atlasSidebar = document.getElementById('sidebar-atlas');
    const courseSidebar = document.getElementById('sidebar-course');
    
    atlasSidebar.style.display = isCourse ? 'none' : 'block';
    courseSidebar.style.display = isCourse ? 'block' : 'none';
}

document.addEventListener('DOMContentLoaded', () => ThemeManager.init());