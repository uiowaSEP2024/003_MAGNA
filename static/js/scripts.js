// You might add JavaScript code if you need to handle something before submit, for example:
document.addEventListener('DOMContentLoaded', function() {
    var loginForm = document.querySelector('form');

    loginForm.onsubmit = function() {
        // Perform validation or pre-submit actions if necessary
    };
});

document.addEventListener('DOMContentLoaded', (event) => {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.backgroundColor = 'red';
        });

        card.addEventListener('mouseleave', () => {
            card.style.backgroundColor = ''; // Or set it to the original color if needed
        });
    });
});

function updateDateTime() {
    var now = new Date();

    // Format the date as you like
    var dateString = now.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    var timeString = now.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });

    // Update the HTML elements
    document.getElementById('date').textContent = dateString;
    document.getElementById('time').textContent = timeString;
}

// Update the date/time on page load
updateDateTime();

// Optionally, set it to update every minute
setInterval(updateDateTime, 60000);

