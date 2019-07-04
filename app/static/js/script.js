let nav = document.getElementById('nav');

nav.onmouseover = () => {
  setTimeout(() => nav.classList.add('open'));
};
nav.onmouseleave = () => nav.classList.remove('open');

Array.from(
  nav.children[0].children
).forEach((li, i) => {
  li.onmouseover = () => nav.setAttribute('data-hover', i);
});