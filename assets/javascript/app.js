const navLinks = document.querySelectorAll('nav.main a');
const navBar = document.querySelector('nav.main');
const command = document.querySelector('#command');
const commands = ['whoami', 'ls ~/Documents/', 'ping 127.0.0.1'];
const primaryNavColor = '#2d302f'
const secondaryNavColor = '#373838';

let typeInterval;

const typeText = async (text) => {
    if (text.length > 0) {
        command.innerText += text[0];
        typeInterval = setTimeout(function() {typeText(text.substring(1,text.length))}, 60);
    }
    else return;
}

for (nav of navLinks) {
    nav.addEventListener('mouseover', (evt) => {
        typeText(commands[parseInt(evt.target.id.replace('link-','')) - 1]);
    })

    nav.addEventListener('mouseout', (evt) => {
        clearTimeout(typeInterval);
        //for (interval of typeInterval) clearTimeout(typeInterval);
        command.innerText = '';
    })
}

// adjust nav BG color to it's current section
window.addEventListener('scroll', () => {
    if (parseInt(scrollY / window.innerHeight) % 2 !== 0) navBar.style.backgroundColor = primaryNavColor;
    else navBar.style.backgroundColor = secondaryNavColor;
})