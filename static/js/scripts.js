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

async function fetchAbsentDays() {
    try {
        const response = await fetch('/api/allowed-absent/'); // Adjust the URL as necessary
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch absent days:', error);
        return []; // Return an empty array in case of error
    }
}

async function fetchRequestedDays() {
    try {
        const response = await fetch('/api/days-requested/'); // Adjust the URL as necessary
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch requested days:', error);
        return []; // Return an empty array in case of error
    }
}

function countRequestedDays(data) {
    return data.reduce((acc, date) => {
        acc[date] = (acc[date] || 0) + 1;
        return acc;
    }, {});
}


async function generateCalendar(year, month) {
    const absentDaysData = await fetchAbsentDays();
    const daysRequestedData = await fetchRequestedDays();
    const requestedDaysCount = countRequestedDays(daysRequestedData);


    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];
    const calendarTitle = document.getElementById('calendar-title');
    const firstDayOfMonth = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    // Update the calendar title
    if (calendarTitle) {
        calendarTitle.textContent = `${monthNames[month]} ${year}`;
    }

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
        spacer.classList.add('calendar-date', 'empty-date');
        calendarDatesElement.appendChild(spacer);
    }

    // Days of the month
    for (let day = 1; day <= daysInMonth; day++) {
        const dateElement = document.createElement('div');
        dateElement.classList.add('calendar-date');
        dateElement.textContent = day;

        // Format the date string for each day
        const shiftDate = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;

        // Find the corresponding absent day data
        const absentDay = absentDaysData.find(data => data.shiftDay === shiftDate);
        const allowedAbsent = absentDay ? absentDay.allowedAbsent : 'No data';


        // Create a span to show the allowedAbsent info
        const absentInfo = document.createElement('span');
        absentInfo.textContent = `Allowed Absent: ${allowedAbsent}`;
        absentInfo.classList.add('absent-info');
        dateElement.appendChild(absentInfo);

        const requestedOffCount = requestedDaysCount[shiftDate];
        if (requestedOffCount) {
            const requestInfo = document.createElement('span');
            requestInfo.textContent = `Requested Off: ${requestedOffCount}`;
            requestInfo.classList.add('request-info');
            dateElement.appendChild(requestInfo);
        }

        // Add click event listener to each date
        dateElement.addEventListener('click', function() {
            const currentAllowedAbsent = absentDaysData.find(data => data.shiftDay === shiftDate)?.allowedAbsent || 'No data';
            const newAllowedAbsent = prompt(`Enter new allowed absent value for ${shiftDate}:`, currentAllowedAbsent);

            if (newAllowedAbsent !== null) {
                updateAllowedAbsent(shiftDate, newAllowedAbsent, this);
            }
        });
        
        calendarDatesElement.appendChild(dateElement);
    }

    // Call this function at the end of generateCalendar to style the current date
    highlightCurrentDate();
}

async function updateAllowedAbsent(shiftDate, newAllowedAbsent, dateElement) {
    try {
        const response = await fetch('/api/update-allowed-absent/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is sent
            },
            body: JSON.stringify({ shiftDay: shiftDate, allowedAbsent: newAllowedAbsent })
        });
        if (response.ok) {
            // Find the absentInfo span within the clicked dateElement and update its text
            const absentInfo = dateElement.querySelector('.absent-info');
            if (absentInfo) {
                absentInfo.textContent = `Allowed Absent: ${newAllowedAbsent}`;
            }
            alert('Update successful!');
        } else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        console.error('Failed to update allowed absent:', error);
        alert('Update failed!');
    }
}


// Helper function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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