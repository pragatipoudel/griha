document.addEventListener('DOMContentLoaded', function() {
    const nameInput = document.getElementById('id_name');
    const slugInput = document.getElementById('id_slug');

    nameInput.addEventListener('input', function() {
        const name = this.value;
        const slug = name.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9\-]/g, '');
        slugInput.value = slug
    });
});