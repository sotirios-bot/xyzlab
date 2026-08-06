// Year
document.getElementById('year').textContent = new Date().getFullYear();

// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

toggle.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  toggle.setAttribute('aria-expanded', isOpen);
});

// Mobile: tap dropdown parent link to toggle sub-menu instead of navigating
navLinks.querySelectorAll('.nav-has-dropdown > a').forEach(link => {
  link.addEventListener('click', e => {
    if (window.innerWidth <= 700) {
      e.preventDefault();
      const parent = link.closest('.nav-has-dropdown');
      const wasOpen = parent.classList.contains('mobile-open');
      navLinks.querySelectorAll('.nav-has-dropdown').forEach(el => el.classList.remove('mobile-open'));
      if (!wasOpen) parent.classList.add('mobile-open');
    }
  });
});

navLinks.querySelectorAll('.nav-dropdown a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    navLinks.querySelectorAll('.nav-has-dropdown').forEach(el => el.classList.remove('mobile-open'));
  });
});

navLinks.querySelectorAll('a:not(.nav-has-dropdown > a)').forEach(link => {
  if (!link.closest('.nav-dropdown')) {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  }
});

// Contact form – mailto (no backend required, sends via visitor's email client)
const form = document.querySelector('.contact-form');
if (form) {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const name     = form.querySelector('#name').value.trim();
    const email    = form.querySelector('#email').value.trim();
    const interest = form.querySelector('#interest').value || 'General Enquiry';
    const message  = form.querySelector('#message').value.trim();

    const subject = encodeURIComponent('XYZ Lab Enquiry: ' + interest);
    const body    = encodeURIComponent(
      'Name: ' + name +
      '\nEmail: ' + email +
      '\nInterest: ' + interest +
      '\n\nMessage:\n' + message
    );

    window.location.href = 'mailto:hello@xyzlab.com?subject=' + subject + '&body=' + body;

    const btn = form.querySelector('button[type="submit"]');
    btn.textContent = 'Opening your email app…';
    btn.style.background = '#069e8e';
    btn.disabled = true;
    setTimeout(() => {
      btn.textContent = 'Send Message';
      btn.style.background = '';
      btn.disabled = false;
    }, 3000);
  });
}

// Scroll-in animation
const animatables = document.querySelectorAll(
  '.course-card, .stat-card, .hero-card, .contact-card, .why-text'
);
const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);
animatables.forEach(el => {
  el.classList.add('animate-on-scroll');
  observer.observe(el);
});

