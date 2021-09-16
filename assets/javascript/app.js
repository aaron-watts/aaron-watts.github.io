// for adjusting nav color to fit backgorund
const navBar = document.querySelector('nav.main');

// for CLI affect on hero section
const navLinks = document.querySelectorAll('nav.main a.type, .links a i');
const command = document.querySelector('#command');

// for carousel on Projects section
const imgs = [...document.querySelectorAll('img.thumb')];
const carouselLeft = document.querySelector('.carousel-left');
const carouselRight = document.querySelector('.carousel-right');

// colors to adjust nav color
const primaryNavColor = '#2d302f'
const secondaryNavColor = '#373838';

// variable used to abandon setInterval calls on command line animation
let typeInterval;

// adjust nav BG color to it's current section
window.addEventListener('scroll', () => {
    if (parseInt(scrollY / (window.innerHeight - navBar.offsetHeight)) % 2 !== 0) {
        navBar.style.backgroundColor = primaryNavColor;
    }
    else navBar.style.backgroundColor = secondaryNavColor;
})

// Typing animation function
// Type one letter at a time with delay to create a typing effect
const typeText = async (text) => {
    if (text.length > 0) {
        command.innerText += text[0];
        // assign setTimeout to global to allow animation to be cancelled when no longer hovering
        typeInterval = setTimeout(function () { typeText(text.substring(1, text.length)) }, 60);
    }
    else return;
}

for (nav of navLinks) {
    // type relevant text to command line on hover
    // command is assigned to html in customText attribute
    nav.addEventListener('mouseover', (evt) => {
        typeText(evt.target.attributes.customText.value);
    })

    // clear interval and text if no hover
    nav.addEventListener('mouseout', (evt) => {
        clearTimeout(typeInterval);
        command.innerText = '';
    })
}

// Carousel function
// active refers to index of active image in imgs array
// direction is positive or negative depending on left or right buttons
const turnCarousel = (active, direction) => {
    // Get directions in text form for class assignments
    const dir = direction > 0 ? 'right' : 'left';
    const opp = dir === 'right' ? 'left' : 'right';

    imgs[active].classList.remove('active');
    imgs[active].classList.add(`off-${opp}`);
    imgs[active + direction].classList.remove(`off-${dir}`);
    imgs[active + direction].classList.add('active');
}

// roll images along carousel LEFT
carouselLeft.addEventListener('click', () => {
    // find index of image with class of active
    const active = imgs.findIndex(img => img.classList.contains('active'));

    // check we are not at the edge of the carousel
    if (active !== imgs.length - 1) turnCarousel(active, 1);
})

carouselRight.addEventListener('click', () => {
    // find index of image with class of active
    const active = imgs.findIndex(img => img.classList.contains('active'));

    // check we are not at the edge of the carousel
    if (active > 0) turnCarousel(active, -1);
})