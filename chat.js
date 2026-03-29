/* ============================================================
   XYZ Lab — AI Chat Widget
   Calls Anthropic API (claude-haiku) with context-aware system
   prompts. Falls back to keyword-matched responses when no API
   key is configured.
   ============================================================ */

const BASE_KNOWLEDGE = `
You are the friendly AI assistant for XYZ Lab, a Singapore-based AI marketing training company.

ABOUT XYZ LAB:
- All courses are LIVE, in-person training sessions held in Singapore
- Location: 160 Robinson Road, #14-04 Business Federation Centre, Singapore 068914
- Email: hello@xyzlab.com | WhatsApp: +65 9426 0742
- Sessions: small groups (max 12 participants), certificate provided
- Group rates available for 3+ people
- Cancellation: full refund 7+ days before session

COURSES OFFERED:
1. AI for Google Ads — AI-powered PPC, ad copywriting, smart bidding, Performance Max
2. AI for Meta Ads — Audience research, creative generation, A/B testing, scaling
3. AI for SEO — Keyword research, content briefs, technical SEO, link outreach
4. AI for Marketing Analytics — GA4, Looker Studio, attribution, predictive analytics
5. AI Content Creation — AI writing, image generation (Midjourney/DALL-E), video/voiceover
6. Vibe Coding with AI — Build apps & automations without traditional coding (Cursor, Bolt, v0)

TONE: Friendly, helpful, concise. Encourage visitors to WhatsApp or email for scheduling.
RESPONSE LENGTH: Keep answers under 120 words. Use short paragraphs or bullet points.
SCOPE: Only answer questions relevant to XYZ Lab's services, AI marketing, and digital marketing.
If asked something off-topic, gently redirect to XYZ Lab topics.
`;

const COURSE_CONTEXT = {
  general: '',
  'google-ads': `
CURRENT PAGE: AI for Google Ads course.
This 7-hour live course covers: AI ad copywriting for RSAs, Smart Bidding (tROAS/tCPA),
AI keyword research & clustering, Performance Max campaigns, audience targeting & remarketing,
Google Ads Scripts, automated Looker Studio reporting.
Tools: Google Ads, Claude, ChatGPT, GA4, Looker Studio, SEMrush, SpyFu.
Ideal for: business owners, PPC managers, ecommerce brands, agency teams.
`,
  'meta-ads': `
CURRENT PAGE: AI for Meta Ads course.
This 6-hour live course covers: AI audience persona building, creative strategy & briefs,
ad copy generation at scale, A/B testing, Advantage+ campaigns, retargeting & lookalikes,
automated performance reporting.
Tools: Meta Ads Manager, Claude, ChatGPT, Midjourney, DALL-E 3, Canva AI, AdCreative.ai.
Ideal for: growth marketers, ecommerce brands, agency teams, business owners.
`,
  seo: `
CURRENT PAGE: AI for SEO course.
This 7-hour live course covers: AI keyword research & clustering, content briefs at scale,
on-page optimisation, technical SEO audits (Screaming Frog + AI), link building outreach,
Google Search Console insights, programmatic SEO basics.
Tools: SEMrush, Ahrefs, Claude, ChatGPT, SurferSEO, Google Search Console, Screaming Frog.
Ideal for: SEO specialists, content marketers, business owners, agency teams.
`,
  'marketing-analytics': `
CURRENT PAGE: AI for Marketing Analytics course.
This 7-hour live course covers: GA4 with AI interpretation, Looker Studio dashboard automation,
attribution modelling, predictive analytics & forecasting, data storytelling,
anomaly detection, cohort analysis, BigQuery basics for marketers.
Tools: GA4, Looker Studio, Claude, ChatGPT, BigQuery, Google Sheets, Supermetrics.
Ideal for: marketing managers, CMOs, agency teams, business owners.
`,
  'content-creation': `
CURRENT PAGE: AI Content Creation course.
This 8-hour live course covers: AI writing & prompting frameworks, blog & long-form content,
social media at scale (30-day calendars), email marketing sequences,
AI image generation (Midjourney, DALL-E 3), video scripts & voiceover (ElevenLabs, Descript),
content repurposing across channels.
Tools: Claude, ChatGPT, Midjourney, DALL-E 3, Canva AI, Descript, ElevenLabs, Notion AI.
Ideal for: content marketers, social media managers, business owners, freelancers.
`,
  'vibe-coding': `
CURRENT PAGE: Vibe Coding with AI course.
This 6-hour live course covers: prompting for builders, building apps without traditional coding,
deploying with Vercel/Netlify, automation workflows (n8n, Make), custom AI chatbots,
working with APIs & data, multi-step AI agents, building & monetising micro-SaaS products.
Tools: Cursor, Bolt.new, v0 by Vercel, Claude, ChatGPT, Replit, n8n, Make, Supabase.
Ideal for: founders, marketers, students, side-project builders — zero coding knowledge required.
`,
};

const SUGGESTIONS = {
  general: [
    'What courses do you offer?',
    'Are classes live in-person?',
    'Which course suits a beginner?',
    'Can my team join together?',
  ],
  'google-ads': [
    'What will I learn in this course?',
    'Do I need Google Ads experience?',
    'What tools will we use?',
    'When is the next session?',
  ],
  'meta-ads': [
    'What does this course cover?',
    'Is this right for ecommerce?',
    'Do I need a Meta Business account?',
    'How many participants per session?',
  ],
  seo: [
    'Do I need coding knowledge?',
    'What will I build in this course?',
    'Which SEO tools are covered?',
    'Is this for beginners or advanced?',
  ],
  'marketing-analytics': [
    'Do I need data skills?',
    'What can I automate after this course?',
    'Is GA4 covered in depth?',
    'What reporting tools will I use?',
  ],
  'content-creation': [
    'Does this cover video content?',
    'Which AI image tools are taught?',
    'Can I use AI for social media?',
    'How do I repurpose content with AI?',
  ],
  'vibe-coding': [
    'Do I need to know how to code?',
    'What will I build on the day?',
    'Which AI tools are covered?',
    'Is this for marketers or developers?',
  ],
};

const MOCK_RESPONSES = [
  {
    keys: ['price', 'cost', 'fee', 'how much', 'sgd', '$'],
    answer: 'For current pricing and upcoming session dates, please contact us directly — we\'d love to help! 📩 **hello@xyzlab.com** or WhatsApp **+65 9426 0742**.',
  },
  {
    keys: ['schedule', 'date', 'when', 'next session', 'upcoming'],
    answer: 'Sessions run regularly throughout the year. To find the next available date for any course, WhatsApp us at **+65 9426 0742** or email **hello@xyzlab.com** and we\'ll get back to you quickly!',
  },
  {
    keys: ['group', 'team', 'company', 'corporate', 'private'],
    answer: 'Yes! We offer **group rates for teams of 3+** and can arrange private in-house sessions tailored to your tools and goals. Email **hello@xyzlab.com** to discuss.',
  },
  {
    keys: ['certificate', 'certification', 'credential'],
    answer: 'Every participant receives an **XYZ Lab certificate of completion** — great for your LinkedIn profile and portfolio.',
  },
  {
    keys: ['beginner', 'no experience', 'never used', 'starting out', 'new to'],
    answer: 'All our courses are designed for **all levels** — including complete beginners. We cover fundamentals before going into advanced techniques, so you\'ll be confident from day one.',
  },
  {
    keys: ['online', 'virtual', 'remote', 'zoom', 'recording'],
    answer: 'All XYZ Lab courses are **live, in-person training** at our Singapore CBD office. No pre-recorded content — you get real hands-on practice and direct trainer feedback.',
  },
  {
    keys: ['location', 'where', 'address', 'mrt', 'venue'],
    answer: 'Training is held at **160 Robinson Road, #14-04 Business Federation Centre, Singapore 068914** — a short walk from Tanjong Pagar MRT.',
  },
  {
    keys: ['google ads', 'ppc', 'search ads', 'smart bidding', 'roas'],
    answer: 'Our **AI for Google Ads** course covers AI ad copywriting, Smart Bidding (tROAS/tCPA), keyword research, Performance Max, and automated reporting. Perfect for PPC managers and business owners.',
  },
  {
    keys: ['meta', 'facebook', 'instagram', 'social ads'],
    answer: 'The **AI for Meta Ads** course teaches AI audience research, creative generation at scale, A/B testing, retargeting, and Advantage+ campaigns — for any level.',
  },
  {
    keys: ['seo', 'search engine', 'keyword', 'ranking', 'organic'],
    answer: 'The **AI for SEO** course covers keyword clustering, content briefs at scale, technical audits, on-page optimisation, and link outreach — all powered by AI.',
  },
  {
    keys: ['analytics', 'ga4', 'data', 'dashboard', 'reporting', 'looker'],
    answer: 'The **AI for Marketing Analytics** course covers GA4, automated Looker Studio dashboards, attribution modelling, predictive analytics, and AI-powered data storytelling.',
  },
  {
    keys: ['content', 'writing', 'copywriting', 'blog', 'social media', 'video', 'image'],
    answer: 'The **AI Content Creation** course covers AI writing, Midjourney/DALL-E image generation, video scripts, ElevenLabs voiceover, and content repurposing across all channels.',
  },
  {
    keys: ['vibe', 'coding', 'code', 'app', 'build', 'no-code', 'automation', 'cursor', 'bolt'],
    answer: 'The **Vibe Coding with AI** course is for non-developers who want to build real apps and automations using AI. No coding knowledge needed — you\'ll ship a working project on the day.',
  },
  {
    keys: ['refund', 'cancel', 'policy'],
    answer: 'We offer a **full refund if you cancel 7+ days** before the course. Within 7 days, we transfer your spot to a future session. Email **hello@xyzlab.com** for any queries.',
  },
  {
    keys: ['enrol', 'register', 'sign up', 'book', 'join'],
    answer: 'To enrol, simply contact us! 📩 **hello@xyzlab.com** or WhatsApp **+65 9426 0742**. We\'ll confirm your spot and send details for the next available session.',
  },
];

function getMockAnswer(question) {
  const q = question.toLowerCase();
  for (const item of MOCK_RESPONSES) {
    if (item.keys.some(k => q.includes(k))) return item.answer;
  }
  return 'Great question! For the most accurate answer, please reach out directly — we\'re happy to help. 📩 **hello@xyzlab.com** or WhatsApp **+65 9426 0742**.';
}

function renderMarkdown(text) {
  return text
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>');
}

/* ── Chat Widget Init ── */
document.addEventListener('DOMContentLoaded', () => {
  const section = document.getElementById('ask-ai');
  if (!section) return;

  const context = section.dataset.context || 'general';
  const messagesEl = document.getElementById('chatMessages');
  const inputEl = document.getElementById('chatInput');
  const sendBtn = document.getElementById('chatSend');
  const suggestionsEl = document.getElementById('chatSuggestions');

  let conversationHistory = [];
  let isLoading = false;

  // Greeting
  appendMessage('bot', 'Hi there! 👋 I\'m the XYZ Lab AI assistant. Ask me anything about our live AI marketing courses, what\'s right for you, or how to enrol.');

  // Suggestions
  const suggestions = SUGGESTIONS[context] || SUGGESTIONS.general;
  suggestionsEl.innerHTML = suggestions
    .map(q => `<button class="suggestion-pill" data-q="${q}">${q}</button>`)
    .join('');

  suggestionsEl.addEventListener('click', e => {
    const pill = e.target.closest('.suggestion-pill');
    if (pill) sendMessage(pill.dataset.q);
  });

  sendBtn.addEventListener('click', () => sendMessage(inputEl.value));
  inputEl.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(inputEl.value); }
  });

  function appendMessage(role, text) {
    const div = document.createElement('div');
    div.className = `chat-msg chat-msg--${role}`;
    div.innerHTML = `
      <div class="chat-avatar">${role === 'bot' ? '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect width="16" height="16" rx="4" fill="#08bfad"/><path d="M4 8h8M8 4v8" stroke="white" stroke-width="1.5" stroke-linecap="round"/></svg>' : '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="5" r="3" fill="#fec55c"/><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6" fill="#fec55c"/></svg>'}</div>
      <div class="chat-bubble">${renderMarkdown(text)}</div>
    `;
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
    return div;
  }

  function appendLoading() {
    const div = document.createElement('div');
    div.className = 'chat-msg chat-msg--bot chat-msg--loading';
    div.innerHTML = `
      <div class="chat-avatar"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect width="16" height="16" rx="4" fill="#08bfad"/><path d="M4 8h8M8 4v8" stroke="white" stroke-width="1.5" stroke-linecap="round"/></svg></div>
      <div class="chat-bubble"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>
    `;
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
    return div;
  }

  async function sendMessage(text) {
    text = text.trim();
    if (!text || isLoading) return;

    isLoading = true;
    inputEl.value = '';
    sendBtn.disabled = true;
    suggestionsEl.style.display = 'none';

    appendMessage('user', text);
    conversationHistory.push({ role: 'user', content: text });

    const loader = appendLoading();

    const apiKey = window.XYZLAB_API_KEY;
    const useMock = !apiKey || apiKey === 'YOUR_ANTHROPIC_API_KEY_HERE';

    if (useMock) {
      await new Promise(r => setTimeout(r, 700 + Math.random() * 600));
      loader.remove();
      const answer = getMockAnswer(text);
      appendMessage('bot', answer);
      conversationHistory.push({ role: 'assistant', content: answer });
    } else {
      try {
        const systemPrompt = BASE_KNOWLEDGE + (COURSE_CONTEXT[context] || '');
        const res = await fetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01',
            'anthropic-dangerous-direct-browser-access': 'true',
          },
          body: JSON.stringify({
            model: 'claude-haiku-4-5-20251001',
            max_tokens: 300,
            system: systemPrompt,
            messages: conversationHistory,
          }),
        });

        if (!res.ok) throw new Error(`API error ${res.status}`);
        const data = await res.json();
        const answer = data.content?.[0]?.text || 'Sorry, I couldn\'t get a response. Please try again.';

        loader.remove();
        appendMessage('bot', answer);
        conversationHistory.push({ role: 'assistant', content: answer });
      } catch (err) {
        loader.remove();
        appendMessage('bot', 'Hmm, something went wrong on my end. Please try again or contact us at **hello@xyzlab.com**.');
        console.error('Chat error:', err);
      }
    }

    isLoading = false;
    sendBtn.disabled = false;
  }
});
