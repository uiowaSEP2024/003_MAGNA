// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the login form
    initializeLoginForm();

    // Setup card hover effects
    setupCardHoverEffects();

    // Fill the calendar with dates
    try {
        generateCalendar(2024, 0); // January is month 0 in JavaScript
    } catch (error) {
        console.error('Error generating calendar:', error);
    }
});

// Initialize login form functionality
function initializeLoginForm() {
    var loginForm = document.querySelector('form');

    loginForm.onsubmit = function() {
        // Perform validation or pre-submit actions if necessary
    };
}

// Set up hover effects for cards
function setupCardHoverEffects() {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.backgroundColor = 'red';
        });

        card.addEventListener('mouseleave', () => {
            card.style.backgroundColor = ''; // Or set it to the original color if needed
        });
    });
}

// Update the date and time on the webpage
function updateDateTime() {
    var now = new Date();
    var dateString = now.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    var timeString = now.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });

    document.getElementById('date').textContent = dateString;
    document.getElementById('time').textContent = timeString;
}
updateDateTime(); // Update on page load
setInterval(updateDateTime, 60000); // Update every minute

// Highlight the current page in navigation
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

// Navigate through the calendar
function navigateCalendar(direction) {
    if (direction === 'prev') {
        // Logic to load the previous month's data
    } else {
        // Logic to load the next month's data
    }
}

// Generate the calendar for a given month and year
function generateCalendar(year, month) {
    const firstDayOfMonth = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const dayOffset = firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1;
    const calendarDatesElement = document.querySelector('.calendar-dates');

    if (!calendarDatesElement) {
        console.error('Calendar dates element not found.');
        return;
    }
    calendarDatesElement.innerHTML = ''; // Clear existing elements

    for (let i = 0; i < dayOffset; i++) {
        const spacer = document.createElement('div');
        spacer.classList.add('calendar-date');
        calendarDatesElement.appendChild(spacer);
    }

    for (let day = 1; day <= daysInMonth; day++) {
        const dateElement = document.createElement('div');
        dateElement.classList.add('calendar-date');
        dateElement.textContent = day;
        calendarDatesElement.appendChild(dateElement);
    }
}
