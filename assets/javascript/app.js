const navLinks = document.querySelectorAll('nav.main a, .links a');
const navBar = document.querySelector('nav.main');
const command = document.querySelector('#command');
const commands = ['cd ~', 'whoami', 'ls ~/Documents/', 'ping 127.0.0.1', 'git remote -v'];
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

// type one letter at a time with delay to create a typing animation
const typeText = async (text) => {
    if (text.length > 0) {
        command.innerText += text[0];
        // assign setTimeout to global variable to clear if no longer hovering over link
        typeInterval = setTimeout(function() {typeText(text.substring(1,text.length))}, 60);
    }
    else return;
}

for (nav of navLinks) {
    // type relevant text to command line on hover
    nav.addEventListener('mouseover', (evt) => {
        typeText(commands[parseInt(evt.target.id.replace('link-',''))]);
    })

    // clear text and interval if no hover
    nav.addEventListener('mouseout', (evt) => {
        clearTimeout(typeInterval);
        command.innerText = '';
    })
}