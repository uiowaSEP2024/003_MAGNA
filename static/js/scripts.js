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
/**
 * Updates the date and time in the HTML elements with id 'date' and 'time' respectively.
 */
function updateDateTime() {
    // Create a new Date object to get the current date and time
    var now = new Date();

    //Get current year and date for calendar
    currentYear = now.getFullYear(); // Update the current year
    currentMonth = now.getMonth(); // Update the current month

    // Format the date as a long weekday, year, month, and day
    var dateString = now.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });

    // Format the time as 2-digit hour and minute
    var timeString = now.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });

    // Update the HTML elements with the formatted date and time
    document.getElementById('date').textContent = dateString;
    document.getElementById('time').textContent = timeString;
}

// Optionally, set it to update every minute
setInterval(updateDateTime, 60000);


/**
 * Activates the navigation button for the current page
 */
function activateCurrentPageNav() {
    // Get the current page from the URL
    const currentPage = window.location.pathname.split('/').pop();

    // Map of page names to corresponding button IDs
    const navButtonIdMap = {
        'pto.html': 'new-request',
        'requests.html': 'current-requests',
        'calendar.html': 'calendar'
    };

    // Get the button ID for the current page
    const activeButtonId = navButtonIdMap[currentPage];

    // Activate the button for the current page
    if (activeButtonId) {
        document.getElementById(activeButtonId).classList.add('active');
    }
}

window.onload = activateCurrentPageNav;

/**
 * Navigates the calendar based on the specified direction.
 * @param {string} direction - The direction to navigate ('prev' or 'next').
 */
function navigateCalendar(direction) {

    // Update the current month and year based on the specified direction
    if (direction === 'prev') {
        if (currentMonth === 0) {
            currentMonth = 11; // Set to December
            currentYear--;
        } else {
            currentMonth--;
        }
    } else {
        if (currentMonth === 11) {
            currentMonth = 0; // Set to January
            currentYear++;
        } else {
            currentMonth++;
        }
    }

    // Generate the calendar based on the updated month and year
    generateCalendar(currentYear, currentMonth);
}

/**
 * Fetches the allowed absent days from the API
 * @returns {Promise<Array>} The array of allowed absent days
 */
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

/**
 * Fetches the requested days from the API
 * @returns {Promise<Array>} The requested days
 */
async function fetchRequestedDays() {
    try {

        // Make a GET request to the '/api/days-requested/' endpoint
        const response = await fetch('/api/days-requested/'); // Adjust the URL as necessary
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Parse the JSON response and return it
        return await response.json();
    } catch (error) {

        // Log an error message and return an empty array in case of failure
        console.error('Failed to fetch requested days:', error);
        return [];
    }
}

/**
 * Counts the frequency of requested days in the given data array.
 * @param {Array} data - The array of requested days
 * @returns {Object} - An object containing the frequency of each requested day
 */
function countRequestedDays(data) {
    return data.reduce((acc, date) => {
        acc[date] = (acc[date] || 0) + 1; // Increase the count for the requested day
        return acc;
    }, {});
}

/**
 * Generates and populates a calendar for the specified year and month.
 * @param {number} year - The year for the calendar.
 * @param {number} month - The month for the calendar (0-11).
 */
async function generateCalendar(year, month) {

    // Fetch data for absent days and requested days
    const absentDaysData = await fetchAbsentDays();
    const daysRequestedData = await fetchRequestedDays();
    const requestedDaysCount = countRequestedDays(daysRequestedData);

    // Array of month names
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];

    // Get the calendar title element and update it with the specified month and year
    const calendarTitle = document.getElementById('calendar-title');

    // Update the calendar title
    if (calendarTitle) {
        calendarTitle.textContent = `${monthNames[month]} ${year}`;
    }

    // Get the first day of the month and the total days in the month
    const firstDayOfMonth = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    // Adjusting for the fact that JavaScript counts Sunday as 0
    const dayOffset = firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1;

    // Get the calendar dates element and clear any existing elements
    const calendarDatesElement = document.querySelector('.calendar-dates');
    if (!calendarDatesElement) {
        console.error('Calendar dates element not found.');
        return;
    }

    calendarDatesElement.innerHTML = ''; // Clear any existing elements

    // Add empty date elements to account for the offset
    for (let i = 0; i < dayOffset; i++) {
        const spacer = document.createElement('div');
        spacer.classList.add('calendar-date', 'empty-date');
        calendarDatesElement.appendChild(spacer);
    }

    // Add date elements for each day in the month
    for (let day = 1; day <= daysInMonth; day++) {

        const dateElement = document.createElement('div');
        dateElement.classList.add('calendar-date');
        dateElement.textContent = day;

        // Format the date string for each day
        const shiftDate = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;

        // Find the corresponding day data
        const absentDay = absentDaysData.find(data => data.shiftDay === shiftDate);
        const allowedAbsent = absentDay ? absentDay.allowedAbsent : 'No data';
        const requestedOffCount = requestedDaysCount[shiftDate] || 0;

        // Highlight the date if there are too many requested days
        if (requestedOffCount > allowedAbsent) {
            dateElement.classList.add('high-request');
        }

        // Create a span to show info
        const infoSpan = document.createElement('span');
        infoSpan.classList.add('date-info');
        const absentInfo = `Allowed Absent: ${allowedAbsent}`;
        const requestInfo = `Requested Off: ${requestedOffCount}`;
        infoSpan.textContent = `${absentInfo}, ${requestInfo}`;
        dateElement.appendChild(infoSpan);

        // Add click event listener to each date to update the allowed absent value
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

/**
 * Updates the allowed absent for a given shift date
 * @param {string} shiftDate - The date of the shift to update
 * @param {number} newAllowedAbsent - The new allowed absent count
 * @param {HTMLElement} dateElement - The element representing the date in the UI
 */
async function updateAllowedAbsent(shiftDate, newAllowedAbsent, dateElement) {
    try {
        // Send a POST request to update the allowed absent count
        const response = await fetch('/api/update-allowed-absent/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is sent
            },
            body: JSON.stringify({ shiftDay: shiftDate, allowedAbsent: newAllowedAbsent })
        });
        if (response.ok) {

            // Update the date-info span within the clicked dateElement with the new allowed absent count
            const dateInfo = dateElement.querySelector('.date-info');
            if (dateInfo) {
                const requestedOffText = dateInfo.textContent.split(', ')[1]; // Keep the existing Requested Off text
                dateInfo.textContent = `Allowed Absent: ${newAllowedAbsent}, ${requestedOffText}`;

                // Check if the requested off count is higher than the new allowed absent
                const requestedOffCount = requestedOffText.split(': ')[1];
                if (parseInt(requestedOffCount) > parseInt(newAllowedAbsent)) {
                    dateElement.classList.add('high-request');
                } else {
                    dateElement.classList.remove('high-request');
                }
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





/**
 * Helper function to get CSRF token from cookies
 * @param {string} name - The name of the cookie to retrieve
 * @returns {string} The value of the specified cookie
 */
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

/**
 * Highlights the current date in the calendar by adding 'current-date' class to the corresponding date element.
 */
function highlightCurrentDate() {

    // Get today's date
    const today = new Date();
    const todayDate = today.getDate();

    // Check if today's date matches the calendar's current month and year
    if (today.getFullYear() === currentYear && today.getMonth() === currentMonth) {

        // Get all date elements in the calendar
        const dateElements = document.querySelectorAll('.calendar-date');

        // Iterate through each date element and add 'current-date' class to the element with today's date
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

document.addEventListener('DOMContentLoaded', function() {
    const formComponentsDiv = document.getElementById('pdfFormComponents');
    const addTextInputButton = document.getElementById('addTextInput');
    const addCheckboxButton = document.getElementById('addCheckbox');

    // Function to add a label input for a text input component
    function addTextInputLabel() {
        const labelInput = document.createElement('input');
        labelInput.type = 'text';
        labelInput.name = 'textInputLabels[]';
        labelInput.placeholder = 'Label for text input';
        formComponentsDiv.appendChild(labelInput);
    }

    // Function to add a label input for a checkbox component
    function addCheckboxLabel() {
        const labelInput = document.createElement('input');
        labelInput.type = 'text';
        labelInput.name = 'checkboxLabels[]';
        labelInput.placeholder = 'Label for checkbox';
        formComponentsDiv.appendChild(labelInput);
    }

    addTextInputButton.addEventListener('click', addTextInputLabel);
    addCheckboxButton.addEventListener('click', addCheckboxLabel);
});



