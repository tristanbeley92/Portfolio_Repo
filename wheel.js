import { wrapDelta, snapTurn, indexAt, coastStep } from './wheel-motion.mjs';

const rotor = document.querySelector('#wheel-rotor');
const wheel = document.querySelector('.skill-wheel');
const categories = [...document.querySelectorAll('[data-skill-category]')];
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
let skills = [], turn = 0, frame = 0, drag = null, suppressClick = false;
const paint = () => rotor.style.setProperty('--turn', `${turn}deg`);
const status = text => document.querySelector('#wheel-state').textContent = text;
function stop() { cancelAnimationFrame(frame); frame = 0; }
function reveal() {
  const selected = indexAt(turn, skills.length);
  [...rotor.children].forEach((button, i) => button.setAttribute('aria-pressed', String(i === selected)));
  const skill = skills[selected];
  document.querySelector('#wheel-name').textContent = skill.dataset.skill;
  document.querySelector('#wheel-description').textContent = skill.dataset.summary;
  document.querySelector('#skill-story-title').textContent = skill.dataset.skill;
  document.querySelector('#skill-story').textContent = skill.dataset.story;
  document.querySelector('.wheel-count').textContent = `${String(selected + 1).padStart(2, '0')} / ${String(skills.length).padStart(2, '0')}`;
  wheel.classList.remove('is-spinning');
  status('Locked in');
}
function settle(target = snapTurn(turn, skills.length)) {
  stop();
  const from = turn, start = performance.now();
  if (reduced.matches || Math.abs(target - from) < .05) { turn = target; paint(); reveal(); return; }
  wheel.classList.add('is-spinning'); status('Settling…');
  function tick(now) {
    const t = Math.min((now - start) / 420, 1);
    turn = from + (target - from) * (1 - Math.pow(1 - t, 3)); paint();
    if (t < 1) frame = requestAnimationFrame(tick);
    else { frame = 0; reveal(); }
  }
  frame = requestAnimationFrame(tick);
}
function coast(velocity) {
  stop();
  if (reduced.matches || Math.abs(velocity) < .025) { settle(); return; }
  wheel.classList.add('is-spinning'); status('Spinning…');
  let last = performance.now();
  function tick(now) {
    const step = coastStep(velocity, Math.min(now - last, 48)); last = now;
    turn += step.distance; velocity = step.velocity; paint();
    if (Math.abs(velocity) > .025) frame = requestAnimationFrame(tick);
    else settle();
  }
  frame = requestAnimationFrame(tick);
}
function chooseSkill(index) {
  settle(turn + wrapDelta(-index * 360 / skills.length - turn));
}
function releaseDrag() {
  if (!drag) return;
  const id = drag.id; drag = null;
  wheel.classList.remove('is-dragging');
  if (wheel.hasPointerCapture(id)) wheel.releasePointerCapture(id);
}
function chooseCategory(category) {
  stop(); releaseDrag(); suppressClick = false;
  skills = [...document.querySelectorAll('[data-skill]')].filter(item => item.dataset.skillGroup === category);
  categories.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.skillCategory === category)));
  turn = 0; rotor.replaceChildren();
  document.querySelector('#wheel-category').textContent = category;
  skills.forEach((skill, i) => {
    const button = document.createElement('button');
    button.type = 'button'; button.className = 'wheel-skill';
    button.style.setProperty('--angle', `${i * 360 / skills.length}deg`);
    button.textContent = skill.dataset.skill;
    button.addEventListener('click', () => chooseSkill(i)); rotor.append(button);
  });
  paint(); reveal();
}
const angle = event => {
  const rect = wheel.getBoundingClientRect();
  return Math.atan2(event.clientY - rect.top - rect.height / 2, event.clientX - rect.left - rect.width / 2) * 180 / Math.PI;
};
wheel.addEventListener('pointerdown', event => {
  if (!event.isPrimary || event.button !== 0 || drag) return;
  stop(); suppressClick = false;
  drag = { id: event.pointerId, angle: angle(event), time: performance.now(), velocity: 0, distance: 0, moved: false, x: event.clientX, y: event.clientY };
});
wheel.addEventListener('pointermove', event => {
  if (!drag || event.pointerId !== drag.id) return;
  const now = performance.now(), next = angle(event), delta = wrapDelta(next - drag.angle);
  if (!drag.moved && Math.hypot(event.clientX - drag.x, event.clientY - drag.y) < 6) return;
  if (!drag.moved) {
    drag.moved = true; wheel.setPointerCapture(event.pointerId);
    wheel.classList.add('is-dragging', 'is-spinning'); status('Drag to spin');
  }
  const dt = Math.max(now - drag.time, 8);
  drag.velocity = .65 * Math.max(-1.4, Math.min(1.4, delta / dt)) + .35 * drag.velocity;
  turn += delta; drag.angle = next; drag.time = now; paint();
});
function finish(event, cancelled = false) {
  if (!drag || event.pointerId !== drag.id) return;
  const { moved, time, velocity } = drag;
  const clicked = event.target.closest('.wheel-skill');
  releaseDrag();
  if (moved) {
    suppressClick = true;
    coast(cancelled || performance.now() - time > 100 ? 0 : velocity);
  } else if (!clicked) settle();
}
window.addEventListener('pointerup', event => finish(event));
window.addEventListener('pointercancel', event => finish(event, true));
wheel.addEventListener('lostpointercapture', event => finish(event, true));
wheel.addEventListener('click', event => {
  if (suppressClick && event.detail !== 0) { event.preventDefault(); event.stopImmediatePropagation(); suppressClick = false; }
}, true);
wheel.addEventListener('keydown', event => {
  if (['ArrowLeft','ArrowRight'].includes(event.key)) {
    event.preventDefault(); settle(snapTurn(turn, skills.length) + (event.key === 'ArrowLeft' ? 1 : -1) * 360 / skills.length);
  }
});
categories.forEach(button => button.addEventListener('click', () => chooseCategory(button.dataset.skillCategory)));
document.querySelectorAll('[data-wheel-step]').forEach(button => button.addEventListener('click', () => settle(snapTurn(turn, skills.length) - Number(button.dataset.wheelStep) * 360 / skills.length)));
function interrupt() { stop(); releaseDrag(); turn = snapTurn(turn, skills.length); paint(); reveal(); }
document.addEventListener('visibilitychange', () => { if (document.hidden) interrupt(); });
window.addEventListener('blur', interrupt);
reduced.addEventListener('change', interrupt);
chooseCategory(categories[0].dataset.skillCategory);
