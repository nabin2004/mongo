async function loadNav() {
    try {
        const response = await fetch('pages/nav.html');
        if (response.ok) {
            const navHtml = await response.text();
            document.getElementById('nav-container').innerHTML = navHtml;
        } else {
            console.error('Failed to load navigation');
        }
    } catch (error) {
        console.error('Error loading navigation:', error);
    }
}

async function loadPage(pageName) {
    try {
        const response = await fetch(`pages/${pageName}`);
        if (response.ok) {
            const pageHtml = await response.text();
            document.getElementById('content-container').innerHTML = pageHtml;
            // Re-highlight syntax since content was added dynamically
            if (window.Prism) {
                Prism.highlightAllUnder(document.getElementById('content-container'));
            }
            // Update active state in nav
            updateActiveNav(pageName);
        } else {
            document.getElementById('content-container').innerHTML = '<article><p>Error loading content.</p></article>';
        }
    } catch (error) {
        console.error('Error loading page:', error);
        document.getElementById('content-container').innerHTML = '<article><p>Error loading content.</p></article>';
    }
}

function updateActiveNav(pageName) {
    const links = document.querySelectorAll('#nav-container a');
    links.forEach(link => {
        if (link.getAttribute('onclick').includes(pageName)) {
            link.classList.add('active');
            link.style.fontWeight = 'bold';
        } else {
            link.classList.remove('active');
            link.style.fontWeight = 'normal';
        }
    });
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    loadNav();
    loadPage('home.html');
});
