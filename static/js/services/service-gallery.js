
const serviceBlocks = document.querySelectorAll('.services > .service');

serviceBlocks.forEach(serviceBlock => {
    serviceBlock.addEventListener('click', () => {
        const activeServiceBlock = document.querySelector('.services > .service.active');
        activeServiceBlock.classList.remove('active');
        serviceBlock.classList.add('active');
    });
});