const neon = document.querySelector('.neon-light');
const INTERVAL = 6500;

setInterval(() => {
    const randInt = () => Math.floor(Math.random() * 100) + 80;

    let delay = randInt();  
    let numFlashes = (Math.floor(Math.random() * 3) + 1) * 2;
    let className = delay > 95 ? 'surge' : 'cut';

    for (let i = 0; i < numFlashes; i++) {
        setTimeout(() => neon.classList.toggle(className), delay);
        delay += randInt();
    }
}, INTERVAL);
