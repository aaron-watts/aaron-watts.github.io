const menuBtn = document.querySelector('.main-nav__menu');
const nav = document.querySelector('.main-nav');

const navLinks = document.querySelectorAll(
    `.main-nav .main-nav__page-links li, 
    .main-nav .main-nav__brand`
    );

const navBar = document.querySelector('nav.main-nav');
const primaryColor = '#2d302f'
const secondaryColor = '#373838';

// Hamburger Menu (Small screens only - negated by CSS at larger sizes)
menuBtn.addEventListener('click', () => {
    nav.classList.toggle('open');
})

// Close hamburger menu when link selected
for (let link of navLinks) {
    link.addEventListener('click', () => {
        nav.classList.remove('open');
    })
}

// Adjust nav BG color to it's current section
window.addEventListener('scroll', () => {
    if (parseInt(scrollY / (window.innerHeight - navBar.offsetHeight)) % 2 !== 0) {
        navBar.style.backgroundColor = primaryColor;
    }
    else navBar.style.backgroundColor = secondaryColor;
})

// Debug to check script loaded
console.log('Script Loaded');