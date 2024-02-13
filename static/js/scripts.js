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



function activateCurrentPageNav() {
    const currentPage = window.location.pathname.split('/').pop();

    const navButtonIdMap = {
        'pto.html': 'new-request',
        'requests.html': 'current-requests',
    };

    const activeButtonId = navButtonIdMap[currentPage];
    if (activeButtonId) {
        document.getElementById(activeButtonId).classList.add('active');
    }
}

window.onload = activateCurrentPageNav;

/* Calendar Navigation */
function navigateCalendar(direction) {
    // Add logic to navigate the calendar (load previous or next month)
    if (direction === 'prev') {
        // Logic to load the previous month's data
    } else {
        // Logic to load the next month's data
    }
}

// Call a function to fill the calendar with dates when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Logic to populate the calendar with dates
});