// Initialize Swiper
var swiper = new Swiper(".mySwiper", {
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 5000,
    },
    loop: true,
});

// Mobile Navigation
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    hamburger.innerHTML = navLinks.classList.contains('active') ? 
        '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        hamburger.innerHTML = '<i class="fas fa-bars"></i>';
    });
});

// Theme Switching
const themeDots = document.querySelectorAll('.theme-dot');
const themeToggle = document.querySelector('.theme-toggle');

themeToggle.addEventListener('click', () => {
    document.querySelector('.theme-switcher').classList.toggle('active');
});

themeDots.forEach(dot => {
    dot.addEventListener('click', function() {
        const theme = this.dataset.theme;
        document.documentElement.className = theme + '-theme';
        
        // Save theme to localStorage
        localStorage.setItem('theme', theme);
    });
});

// Load saved theme
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    document.documentElement.className = savedTheme + '-theme';
}

// Mouse Following Animation
const cursor = document.querySelector('.cursor');
const cursorFollower = document.querySelector('.cursor-follower');

document.addEventListener('mousemove', (e) => {
    cursor.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0)`;
    
    // Add a small delay to the follower for a trailing effect
    setTimeout(() => {
        cursorFollower.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0)`;
    }, 50);
});

// Interactive cursor effects
document.querySelectorAll('a, button, .project-card, .skill-card').forEach(element => {
    element.addEventListener('mouseenter', () => {
        cursor.style.transform = 'scale(1.5)';
        cursor.style.borderColor = 'var(--accent)';
        cursorFollower.style.width = '20px';
        cursorFollower.style.height = '20px';
    });
    
    element.addEventListener('mouseleave', () => {
        cursor.style.transform = 'scale(1)';
        cursor.style.borderColor = 'var(--primary)';
        cursorFollower.style.width = '10px';
        cursorFollower.style.height = '10px';
    });
});

// Scroll to Top Button
const scrollButton = document.querySelector('.scroll-to-top');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 500) {
        scrollButton.classList.add('show');
    } else {
        scrollButton.classList.remove('show');
    }
});

scrollButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Floating Hire Me Button
const floatingHireBtn = document.querySelector('.floating-hire-btn');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        floatingHireBtn.classList.add('show');
    } else {
        floatingHireBtn.classList.remove('show');
    }
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                hamburger.innerHTML = '<i class="fas fa-bars"></i>';
            }
        }
    });
});

// Hire me buttons functionality
document.querySelectorAll('.hire-me-nav, .floating-hire-btn').forEach(button => {
    button.addEventListener('click', () => {
        const contactSection = document.querySelector('#contact');
        if (contactSection) {
            window.scrollTo({
                top: contactSection.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});