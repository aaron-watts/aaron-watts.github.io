const menuBtn = document.querySelector('.main-nav__menu');
const nav = document.querySelector('.main-nav');

menuBtn.addEventListener('click', () => {
    nav.classList.toggle('open');
})