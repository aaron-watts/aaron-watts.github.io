const navLinks = document.querySelectorAll('nav.main a');
const command = document.querySelector('#command');
const commands = ['whoami', 'ls ~/Documents/', 'nano contact.txt'];

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