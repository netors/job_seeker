// Shared JavaScript functionality for AI-Powered Job Search System documentation

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive features
    initializeNavigation();
    initializeScrollAnimations();
    initializeCodeCopyButtons();
    initializeSearchFunctionality();
    initializeThemeToggle();
    initializeScrollToTop();

    console.log('AI Job Search documentation loaded successfully');
});

/**
 * Navigation functionality
 */
function initializeNavigation() {
    // Mobile navigation toggle
    const navToggle = document.createElement('div');
    navToggle.className = 'nav-toggle';
    navToggle.innerHTML = '☰';

    const navMenu = document.querySelector('.nav-menu');
    const navContainer = document.querySelector('.nav-container');

    if (navMenu && navContainer) {
        navContainer.appendChild(navToggle);

        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('nav-menu-open');
            navToggle.classList.toggle('nav-toggle-open');
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navContainer.contains(e.target)) {
                navMenu.classList.remove('nav-menu-open');
                navToggle.classList.remove('nav-toggle-open');
            }
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Highlight current page in navigation
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
}

/**
 * Scroll animations for elements entering viewport
 */
function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animatedSelectors = [
        '.content-block',
        '.agent-card',
        '.feature-card',
        '.task-step',
        '.output-file',
        '.quick-step',
        '.api-section'
    ];

    animatedSelectors.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    });
}

/**
 * Copy code blocks to clipboard
 */
function initializeCodeCopyButtons() {
    document.querySelectorAll('pre').forEach(pre => {
        // Create copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.innerHTML = '📋 Copy';
        copyButton.setAttribute('aria-label', 'Copy code to clipboard');

        // Position button
        pre.style.position = 'relative';
        copyButton.style.position = 'absolute';
        copyButton.style.top = '10px';
        copyButton.style.right = '10px';
        copyButton.style.background = 'rgba(255, 255, 255, 0.9)';
        copyButton.style.border = 'none';
        copyButton.style.borderRadius = '4px';
        copyButton.style.padding = '4px 8px';
        copyButton.style.fontSize = '0.8rem';
        copyButton.style.cursor = 'pointer';
        copyButton.style.transition = 'all 0.2s ease';

        pre.appendChild(copyButton);

        copyButton.addEventListener('click', async function() {
            const code = pre.textContent.replace(/📋 Copy/, '').trim();

            try {
                await navigator.clipboard.writeText(code);
                copyButton.innerHTML = '✅ Copied!';
                copyButton.style.background = '#27ae60';
                copyButton.style.color = 'white';

                setTimeout(() => {
                    copyButton.innerHTML = '📋 Copy';
                    copyButton.style.background = 'rgba(255, 255, 255, 0.9)';
                    copyButton.style.color = 'initial';
                }, 2000);
            } catch (err) {
                copyButton.innerHTML = '❌ Failed';
                setTimeout(() => {
                    copyButton.innerHTML = '📋 Copy';
                }, 2000);
            }
        });

        // Hide button on mobile to prevent interface issues
        if (window.innerWidth < 768) {
            copyButton.style.display = 'none';
        }
    });
}

/**
 * Search functionality for documentation
 */
function initializeSearchFunctionality() {
    // Create search container
    const searchContainer = document.createElement('div');
    searchContainer.className = 'search-container';
    searchContainer.innerHTML = `
        <input type="text" id="doc-search" placeholder="Search documentation..." />
        <div id="search-results" class="search-results"></div>
    `;

    // Add search to navigation
    const navMenu = document.querySelector('.nav-menu');
    if (navMenu) {
        navMenu.parentNode.insertBefore(searchContainer, navMenu);
    }

    const searchInput = document.getElementById('doc-search');
    const searchResults = document.getElementById('search-results');

    if (searchInput && searchResults) {
        let searchTimeout;

        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const query = this.value.trim().toLowerCase();

            if (query.length < 2) {
                searchResults.style.display = 'none';
                return;
            }

            searchTimeout = setTimeout(() => {
                performSearch(query, searchResults);
            }, 300);
        });

        // Hide search results when clicking outside
        document.addEventListener('click', function(e) {
            if (!searchContainer.contains(e.target)) {
                searchResults.style.display = 'none';
            }
        });
    }
}

/**
 * Perform search across page content
 */
function performSearch(query, resultsContainer) {
    const searchableElements = document.querySelectorAll('h2, h3, h4, p, li, .endpoint h4');
    const results = [];

    searchableElements.forEach(element => {
        const text = element.textContent.toLowerCase();
        if (text.includes(query)) {
            const heading = findNearestHeading(element);
            results.push({
                element: element,
                heading: heading ? heading.textContent : 'Documentation',
                text: element.textContent.substring(0, 150) + '...',
                relevance: calculateRelevance(text, query)
            });
        }
    });

    // Sort by relevance
    results.sort((a, b) => b.relevance - a.relevance);

    // Display results
    if (results.length > 0) {
        resultsContainer.innerHTML = results.slice(0, 5).map(result => `
            <div class="search-result-item" data-element-id="${getElementId(result.element)}">
                <div class="search-result-heading">${result.heading}</div>
                <div class="search-result-text">${highlightQuery(result.text, query)}</div>
            </div>
        `).join('');

        resultsContainer.style.display = 'block';

        // Add click handlers to search results
        resultsContainer.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', function() {
                const elementId = this.dataset.elementId;
                const targetElement = document.querySelector(`[data-search-id="${elementId}"]`);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth' });
                    resultsContainer.style.display = 'none';
                }
            });
        });
    } else {
        resultsContainer.innerHTML = '<div class="search-no-results">No results found</div>';
        resultsContainer.style.display = 'block';
    }
}

/**
 * Helper functions for search
 */
function findNearestHeading(element) {
    let current = element;
    while (current && current !== document.body) {
        if (current.matches('h1, h2, h3, h4, h5, h6')) {
            return current;
        }
        current = current.previousElementSibling || current.parentElement;
    }
    return null;
}

function calculateRelevance(text, query) {
    const queryWords = query.split(' ');
    let score = 0;

    queryWords.forEach(word => {
        const regex = new RegExp(word, 'gi');
        const matches = text.match(regex);
        if (matches) {
            score += matches.length;
        }
    });

    return score;
}

function getElementId(element) {
    if (!element.dataset.searchId) {
        element.dataset.searchId = 'search-' + Math.random().toString(36).substr(2, 9);
    }
    return element.dataset.searchId;
}

function highlightQuery(text, query) {
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

/**
 * Theme toggle functionality
 */
function initializeThemeToggle() {
    // Create theme toggle button
    const themeToggle = document.createElement('button');
    themeToggle.className = 'theme-toggle';
    themeToggle.innerHTML = '🌙';
    themeToggle.setAttribute('aria-label', 'Toggle dark mode');
    themeToggle.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: rgba(255, 255, 255, 0.9);
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 1.2rem;
        cursor: pointer;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    `;

    document.body.appendChild(themeToggle);

    // Check for saved theme preference
    const savedTheme = localStorage.getItem('ai-job-search-theme');
    if (savedTheme) {
        document.body.classList.toggle('dark-theme', savedTheme === 'dark');
        themeToggle.innerHTML = savedTheme === 'dark' ? '☀️' : '🌙';
    }

    themeToggle.addEventListener('click', function() {
        const isDark = document.body.classList.toggle('dark-theme');
        this.innerHTML = isDark ? '☀️' : '🌙';
        localStorage.setItem('ai-job-search-theme', isDark ? 'dark' : 'light');
    });
}

/**
 * Scroll to top functionality
 */
function initializeScrollToTop() {
    const scrollButton = document.createElement('button');
    scrollButton.className = 'scroll-to-top';
    scrollButton.innerHTML = '↑';
    scrollButton.setAttribute('aria-label', 'Scroll to top');
    scrollButton.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999;
        background: #3498db;
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 1.5rem;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    `;

    document.body.appendChild(scrollButton);

    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollButton.style.opacity = '1';
            scrollButton.style.visibility = 'visible';
        } else {
            scrollButton.style.opacity = '0';
            scrollButton.style.visibility = 'hidden';
        }
    });

    scrollButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Utility functions
 */

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Check if element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Format code blocks for better display
function formatCodeBlocks() {
    document.querySelectorAll('pre code').forEach(block => {
        // Add syntax highlighting class if not present
        if (!block.className) {
            const text = block.textContent;
            if (text.includes('python') || text.includes('pip') || text.includes('def ')) {
                block.className = 'language-python';
            } else if (text.includes('git ') || text.includes('npm ')) {
                block.className = 'language-bash';
            } else if (text.includes('{') && text.includes('}')) {
                block.className = 'language-json';
            }
        }
    });
}

// Add responsive handling for tables
function makeTablesResponsive() {
    document.querySelectorAll('table').forEach(table => {
        if (!table.parentElement.classList.contains('table-responsive')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'table-responsive';
            wrapper.style.overflowX = 'auto';
            table.parentNode.insertBefore(wrapper, table);
            wrapper.appendChild(table);
        }
    });
}

// Initialize additional features on load
document.addEventListener('DOMContentLoaded', function() {
    formatCodeBlocks();
    makeTablesResponsive();
});

// Handle window resize for responsive features
window.addEventListener('resize', debounce(function() {
    // Recalculate any layout-dependent features
    makeTablesResponsive();
}, 250));

// Analytics and usage tracking (privacy-respecting)
function trackPageView() {
    // Only track if user hasn't opted out
    if (!localStorage.getItem('ai-job-search-analytics-opt-out')) {
        const pageData = {
            page: window.location.pathname,
            timestamp: new Date().toISOString(),
            userAgent: navigator.userAgent.substring(0, 100), // Truncated for privacy
            referrer: document.referrer ? new URL(document.referrer).hostname : 'direct'
        };

        // Store locally for now (could be extended to send to analytics service)
        console.log('Page view:', pageData);
    }
}

// Call analytics on page load
document.addEventListener('DOMContentLoaded', trackPageView);