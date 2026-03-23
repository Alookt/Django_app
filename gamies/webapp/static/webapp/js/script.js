// Basic JavaScript for the Django app

document.addEventListener('DOMContentLoaded', function() {
    console.log('Django app loaded!');

    // Example: Add a click event to the header
    const header = document.querySelector('header h1');
    if (header) {
        header.addEventListener('click', function() {
            alert('Welcome to Gamies!');
        });
    }
});