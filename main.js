// Year
document.getElementById('year').textContent = new Date().getFullYear();

// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

toggle.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  toggle.setAttribute('aria-expanded', isOpen);
});

navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  });
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

// Floating WhatsApp + YouTube buttons (injected once, applies to all pages)
(function initFloatingButtons() {
  const el = document.createElement('div');
  el.className = 'floating-actions';
  el.setAttribute('aria-label', 'Quick contact');
  el.innerHTML = `
    <a href="https://www.youtube.com/@xyzl" class="float-btn float-yt" target="_blank" rel="noopener noreferrer" aria-label="Visit YouTube channel">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
      <span class="float-label">YouTube</span>
    </a>
    <a href="https://tally.so/r/RGVaXv" class="float-btn float-coaching" target="_blank" rel="noopener noreferrer" aria-label="Book a coaching session">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
      <span class="float-label">Book Session</span>
    </a>
    <a href="https://wa.me/6594260742" class="float-btn float-wa" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      <span class="float-label">WhatsApp</span>
    </a>
  `;
  document.body.appendChild(el);
}());
