const menuBtn = document.querySelector('.main-nav__menu');      // hamburger button
const nav = document.querySelector('.main-nav');                // nav container

// Nav items that are supposed to cause the hamburger menu to close
const navLinks = document.querySelectorAll(
    `.main-nav .main-nav__page-links li, 
    .main-nav .main-nav__brand`
);

const primaryColor = '#2d302f'
const secondaryColor = '#373838';

const homeBash = document.querySelector('.home-bash');
const aboutBash = document.querySelector('.about-bash');
// declared in global scope to allow cancel timeout, used in typeText()
let typeInterval;

// Recursive function to create typing effect
const typeText = async (text, elem) => {
    console.log(`${text.length}`)
    if (text.length > 0) {
        elem.innerText += text[0];
        // assign setTimeout to global to allow animation to be cancelled when no longer hovering
        typeInterval = setTimeout(function () { 
            typeText(text.substring(1, text.length), elem) 
        }, 60);
    }
    else return;
}

const clearText = (elem) => {
    elem.innerText = '';
}

// Apply active class to relevant navLink if not home
const applyActiveTarget = () => {
    if (document.querySelector(':target')) {                    // First check if target exists
        const target = document.querySelector(':target');       // Get target
        const targetNav = document.querySelector(`
            a[href="#${target.id}"]`
        );                                                      // Get relevant nav anchor

        for (let link of navLinks) {
            if (link === targetNav.parentElement) {             // If link is targetNavs parent (li)
                link.classList.add('active');
            }
            else if (link.classList.contains('active')) {       // Don't remove non existent classes
                link.classList.remove('active');
            }
        }

        if (target.attributes.bashtext) {
            document.querySelector(`section.${target.id} h2`).classList.add('show');
            const element = document.querySelector(`.${target.id}-bash`);
            clearText(element);
            setTimeout(() => {
                typeText(target.attributes.bashtext.value, element);
            }, 1300);
        }
    } else {                                                    // If no target (home)
        for (let link of navLinks) {
            if (link.classList.contains('active')) {            // Don't remove non existent classes
                link.classList.remove('active');
            }
        }
    }
}

// Apply active class to relevant link in nav on load and on hashchange
window.addEventListener('load', applyActiveTarget);
window.addEventListener('hashchange', applyActiveTarget);


// Adjust nav BG color to it's current section
window.addEventListener('scroll', () => {
    if (parseInt(scrollY / (window.innerHeight - nav.offsetHeight)) % 2 !== 0) {
        nav.style.backgroundColor = primaryColor;
    }
    else nav.style.backgroundColor = secondaryColor;
})

// Hamburger Menu Toggler (Small screens only - negated by CSS at larger sizes)
menuBtn.addEventListener('click', () => {
    nav.classList.toggle('open');
})

// Close hamburger menu when a relevant link selected
for (let link of navLinks) {
    link.addEventListener('click', () => {
        nav.classList.remove('open');
    })
}

// Debug to check script loaded
console.log('Script Loaded');

