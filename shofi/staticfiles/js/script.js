// Initialize Particles.js with enhanced cursor-following effect
document.addEventListener("DOMContentLoaded", function () {
  // Set light theme by default
  document.documentElement.className = "light-theme";

  // Theme Switching
  const themeDots = document.querySelectorAll(
    ".theme-dot, .mobile-theme-switcher .theme-dot"
  );

  themeDots.forEach((dot) => {
    dot.addEventListener("click", function () {
      const theme = this.dataset.theme;
      document.documentElement.className = theme + "-theme";
      localStorage.setItem("theme", theme); // Save preference
    });
  });

  // Load saved theme if user has selected before
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme && savedTheme !== "light") {
    document.documentElement.className = savedTheme + "-theme";
  }

  // Particles.js configuration
  const currentTheme = document.documentElement.classList.contains("dark-theme")
    ? "dark"
    : "light";
  const particleColor = currentTheme === "dark" ? "#ffffff" : "#000000";

  particlesJS("particles-js", {
    particles: {
      number: {
        value: 80,
        density: {
          enable: true,
          value_area: 800,
        },
      },
      color: {
        value: particleColor,
      },
      shape: {
        type: "circle",
        stroke: {
          width: 0,
          color: "#000000",
        },
      },
      opacity: {
        value: currentTheme === "dark" ? 0.3 : 0.1,
        random: false,
      },
      size: {
        value: 3,
        random: true,
        anim: {
          enable: true,
          speed: 4,
          size_min: 0.3,
          sync: false,
        },
      },
      line_linked: {
        enable: true,
        distance: 150,
        color: particleColor,
        opacity: currentTheme === "dark" ? 0.3 : 0.1,
        width: 1,
      },
      move: {
        enable: true,
        speed: 2,
        direction: "none",
        random: true,
        straight: false,
        out_mode: "out",
        bounce: false,
        attract: {
          enable: true,
          rotateX: 600,
          rotateY: 1200,
        },
      },
    },
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: {
          enable: true,
          mode: "grab",
          parallax: {
            enable: true,
            force: 60,
            smooth: 10,
          },
        },
        onclick: {
          enable: true,
          mode: "push",
        },
        resize: true,
      },
      modes: {
        grab: {
          distance: 200,
          line_linked: {
            opacity: 0.8,
          },
        },
        bubble: {
          distance: 400,
          size: 40,
          duration: 2,
          opacity: 8,
          speed: 3,
        },
        repulse: {
          distance: 200,
          duration: 0.4,
        },
        push: {
          particles_nb: 4,
        },
        remove: {
          particles_nb: 2,
        },
      },
    },
    retina_detect: true,
  });

  // Smooth scrolling for navigation links
  document
    .querySelectorAll(".nav-links a, .mobile-menu-links a")
    .forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        const href = this.getAttribute("href");
        if (href.startsWith("#")) {
          e.preventDefault();
          const target = document.querySelector(href);
          if (target) {
            target.scrollIntoView({ behavior: "smooth" });
          }
          // Close mobile menu if open
          mobileMenu.classList.remove("active");
          mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
        }
      });
    });

  // Scroll to top button
  const scrollTopBtn = document.getElementById("scrollTopBtn");

  window.addEventListener("scroll", function () {
    if (window.pageYOffset > 300) {
      scrollTopBtn.classList.add("show");
    } else {
      scrollTopBtn.classList.remove("show");
    }
  });

  scrollTopBtn.addEventListener("click", function () {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  // Hire button functionality
  const hireBtn = document.getElementById("hireBtn");
  const mobileHireBtn = document.getElementById("mobileHireBtn");

  hireBtn.addEventListener("click", function () {
    document.querySelector("#contact").scrollIntoView({
      behavior: "smooth",
    });
  });

  mobileHireBtn.addEventListener("click", function () {
    document.querySelector("#contact").scrollIntoView({
      behavior: "smooth",
    });
  });

  // Mobile menu functionality
  const mobileMenuBtn = document.getElementById("mobileMenuBtn");
  const mobileMenu = document.getElementById("mobileMenu");

  mobileMenuBtn.addEventListener("click", function () {
    mobileMenu.classList.toggle("active");
    // Change icon based on menu state
    if (mobileMenu.classList.contains("active")) {
      mobileMenuBtn.innerHTML = '<i class="fas fa-times"></i>';
    } else {
      mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
    }
  });

  // Close menu when clicking outside
  document.addEventListener("click", function (e) {
    if (!mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
      mobileMenu.classList.remove("active");
      mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
    }
  });

  // Form submission
  const contactForm = document.querySelector(".contact-form form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Thank you for your message! I will get back to you soon.");
      contactForm.reset();
    });
  }

  // Newsletter form submission
  const newsletterForm = document.querySelector(".newsletter-form");
  if (newsletterForm) {
    newsletterForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const emailInput = newsletterForm.querySelector(".newsletter-input");
      if (emailInput.value) {
        alert("Thank you for subscribing to my newsletter!");
        emailInput.value = "";
      }
    });
  }
});
