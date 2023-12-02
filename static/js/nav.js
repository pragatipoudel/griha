const navBar = document.querySelector('nav');
const navBarToggle = document.querySelector('nav .nav-toggle');

navBarToggle.addEventListener('click', () => {
    navBar.classList.toggle('open');
});