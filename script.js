'use strict';
const menu = document.querySelector('.menu-toggle');
const mobile = document.querySelector('#mobile-menu');
menu.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  menu.textContent = open ? 'Close −' : 'Menu +';
  mobile.hidden = !open;
});
mobile.addEventListener('click', event => {
  if (event.target.closest('a')) { mobile.hidden = true; menu.setAttribute('aria-expanded', 'false'); menu.textContent = 'Menu +'; }
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !mobile.hidden) { mobile.hidden = true; menu.setAttribute('aria-expanded', 'false'); menu.textContent = 'Menu +'; menu.focus(); }
});

const pages = [
  ['Home', 'index.html', 'Page'], ['About', 'about.html', 'Page'],
  ['Experience', 'experience.html', 'Page'], ['Skills', 'skills.html', 'Page'],
  ['Projects', 'projects.html', 'Page'], ['Contact', '#contact', 'Section'],
  ['TEDxThirdWard', 'project-tedx.html', 'Project'], ['NutriScan AI', 'project-nutriscan.html', 'Project'],
  ['Adaptive Playlist Generator', 'project-playlist.html', 'Project'], ['Escape PolyLand', 'project-unity.html', 'Project'],
  ['Open Cam Lab', 'project-opencam.html', 'Project'], ['This portfolio', 'project-portfolio.html', 'Project']
];
const dialog = document.querySelector('#command-dialog');
const search = document.querySelector('#command-search');
const results = document.querySelector('.command-results');
function renderResults() {
  results.replaceChildren();
  const matches = pages.filter(([name]) => name.toLowerCase().includes(search.value.trim().toLowerCase()));
  for (const [name, href, type] of matches) {
    const link = document.createElement('a'); link.href = href; link.textContent = name;
    const label = document.createElement('span'); label.textContent = type + ' ↗'; link.append(label);
    link.addEventListener('click', () => dialog.close()); results.append(link);
  }
  if (!matches.length) { const empty = document.createElement('p'); empty.textContent = 'No matches. Try a page or project name.'; results.append(empty); }
}
function openCommand() { search.value = ''; renderResults(); dialog.showModal(); search.focus(); }
document.querySelector('[data-command]').addEventListener('click', openCommand);
document.querySelector('[data-close]').addEventListener('click', () => dialog.close());
search.addEventListener('input', renderResults);
search.addEventListener('keydown', event => {
  if (event.key === 'ArrowDown') { event.preventDefault(); results.querySelector('a')?.focus(); }
  if (event.key === 'Enter') { event.preventDefault(); results.querySelector('a')?.click(); }
});
results.addEventListener('keydown', event => {
  const links = [...results.querySelectorAll('a')]; const index = links.indexOf(document.activeElement);
  if (event.key === 'ArrowDown') { event.preventDefault(); links[(index + 1) % links.length]?.focus(); }
  if (event.key === 'ArrowUp') { event.preventDefault(); if (index <= 0) search.focus(); else links[index - 1].focus(); }
});
dialog.addEventListener('click', event => { if (event.target === dialog) { const r = dialog.getBoundingClientRect(); if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close(); } });
document.addEventListener('keydown', event => {
  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); if (dialog.open) dialog.close(); else openCommand(); }
});
document.querySelector('[data-copy]').addEventListener('click', async () => {
  const status = document.querySelector('.copy-status');
  try { await navigator.clipboard.writeText('tristanbeley@gmail.com'); status.textContent = 'Copied. Talk soon!'; }
  catch { status.textContent = 'tristanbeley@gmail.com'; }
});

document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('[data-filter]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  let count = 0;
  document.querySelectorAll('[data-category]').forEach(card => { card.hidden = button.dataset.filter !== 'All' && card.dataset.category !== button.dataset.filter; if (!card.hidden) count++; });
  document.querySelector('#filter-status').textContent = `${count} ${count === 1 ? 'project' : 'projects'} shown`;
}));
const previews = {
  tedx: ['TEDxThirdWard', 'A public website and a custom admin console for the people behind the event.', 'red'],
  nutriscan: ['NutriScan AI', 'A 36-hour nutrition prototype. Two HackWestern awards. Built together under a deadline.', 'green'],
  playlist: ['Adaptive Playlist Generator', 'Mood, context, and a swipe-style interface for making a Spotify playlist your own.', 'purple']
};
document.querySelectorAll('[data-preview]').forEach(button => button.addEventListener('click', () => {
  const slug = button.dataset.preview; const [title, description, color] = previews[slug];
  document.querySelectorAll('[data-preview]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  document.querySelector('#stage-title').textContent = title;
  document.querySelector('#stage-description').textContent = description;
  document.querySelector('#stage-link').href = `project-${slug}.html`;
  const art = document.querySelector('#stage-art');
  const source = document.querySelector(`.project-card a[href="project-${slug}.html"]`).firstElementChild;
  art.replaceChildren(source.cloneNode(true)); art.className = `stage-art project-art ${color}`;
}));
