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

let currentYear;
let currentMonth;
function updateDateTime() {
    var now = new Date();

    //Get current year and date for calendar
    currentYear = now.getFullYear(); // Update the current year
    currentMonth = now.getMonth(); // Update the current month

    // Format the date as you like
    var dateString = now.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    var timeString = now.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });

    // Update the HTML elements
    document.getElementById('date').textContent = dateString;
    document.getElementById('time').textContent = timeString;
}

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
    if (direction === 'prev') {
        if (currentMonth === 0) {
            currentMonth = 11; // December
            currentYear--;
        } else {
            currentMonth--;
        }
    } else {
        if (currentMonth === 11) {
            currentMonth = 0; // January
            currentYear++;
        } else {
            currentMonth++;
        }
    }
    generateCalendar(currentYear, currentMonth);
}

function generateCalendar(year, month) {
    const firstDayOfMonth = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const dateElement = document.createElement('div');
    dateElement.classList.add('calendar-date');

    // Adjusting for the fact that JavaScript counts Sunday as 0
    const dayOffset = firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1;

    // The calendar HTML element
    const calendarDatesElement = document.querySelector('.calendar-dates');
    if (!calendarDatesElement) {
        console.error('Calendar dates element not found.');
        return;
    }
    calendarDatesElement.innerHTML = ''; // Clear any existing elements

    // Offset for the first day of the month
    for (let i = 0; i < dayOffset; i++) {
        const spacer = document.createElement('div');
        spacer.classList.add('calendar-date');
        calendarDatesElement.appendChild(spacer);
    }

    // Days of the month
    for (let day = 1; day <= daysInMonth; day++) {
        const dateElement = document.createElement('div');
        dateElement.classList.add('calendar-date');
        dateElement.textContent = day;
        calendarDatesElement.appendChild(dateElement);
    }
}

function highlightCurrentDate() {
    const today = new Date();
    const todayDate = today.getDate();
    if (today.getFullYear() === currentYear && today.getMonth() === currentMonth) {
        const dateElements = document.querySelectorAll('.calendar-date');
        dateElements.forEach(function(el) {
            if (parseInt(el.textContent) === todayDate) {
                el.classList.add('current-date');
            }
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {

    // Update the date/time on page load
    updateDateTime()
    try {
        generateCalendar(currentYear, currentMonth); // January is month 0 in JavaScript
    } catch (error) {
        console.error('Error generating calendar:', error);
    }
    document.getElementById('prevMonth').addEventListener('click', function() {
        navigateCalendar('prev');
    });
    document.getElementById('nextMonth').addEventListener('click', function() {
        navigateCalendar('next');
    });
});