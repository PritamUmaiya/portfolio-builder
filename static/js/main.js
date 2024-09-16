document.addEventListener('DOMContentLoaded', () => {
    // Theme toggler
    let themeToggler = document.querySelector('#themeToggler');
    let theme = localStorage.getItem('theme');
    if (theme) {
        document.querySelector('body').classList.add(theme);
        themeToggler.innerHTML = `<i class="bi bi-sun" style="font-size: 1.2rem;"></i>`;
    }

    themeToggler.addEventListener('click', () => {
        themeToggler.innerHTML = ``;

        if (document.querySelector('body').classList.contains('dark')) {
            document.querySelector('body').classList.remove('dark');
            if (theme) {
                localStorage.removeItem("theme");
            }
            themeToggler.innerHTML = `<i class="bi bi-moon" style="font-size: 1.2rem;"></i>`;
        } else {
            document.querySelector('body').classList.add('dark');
            localStorage.setItem('theme','dark');
            themeToggler.innerHTML = `<i class="bi bi-sun" style="font-size: 1.2rem;"></i>`;
        }
    });
});

// Function to toggle menu
function toggleMenu() {
    const sideNav = document.getElementById('sideNav');
    const overlay = document.getElementById('overlay');
    sideNav.classList.toggle('left-0');
    overlay.classList.toggle('d-block');
}
