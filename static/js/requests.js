/**
 * This file contains the JavaScript code for the requests page.
 * It is responsible for handling the search form submission and displaying the search results.
 * The search results are displayed in a card format, with each card containing the details of a request.
 * The card is styled based on the approval status of the request.
 * If no requests are found, a message is displayed indicating that no requests were found.
 * A reset button is also displayed to allow the user to reset the search and view all requests.
 * The reset button reloads the page when clicked.
 */
document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById('search-form');

    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const clockNumber = document.getElementById('clock_number').value;

            fetch(`/search-requests?clock_number=${clockNumber}`)
                .then(response => response.json())
                .then(data => {
                    const container = document.querySelector('.container');
                    container.innerHTML = '';

                    if (data.length > 0) {
                         data.forEach(request => {
                             const requestCard = document.createElement('div');
                             requestCard.classList.add('request-card');
                             requestCard.classList.add(`status-${request.approval_status}`);

                             const requestCardTop = document.createElement('div');
                             requestCardTop.classList.add('request-card-top');

                             const filledBy = document.createElement('div');
                             filledBy.textContent = `Filled by: ${request.filled_by}`;

                             const requestType = document.createElement('div');
                             requestType.classList.add('request-type');
                             requestType.textContent = request.absence_type;

                             requestCardTop.appendChild(filledBy);
                             requestCardTop.appendChild(requestType);

                             const requestCardBottom = document.createElement('div');
                             requestCardBottom.classList.add('request-card-bottom');

                             const startDate = document.createElement('div');
                             startDate.textContent = `Start Date: ${request.start_date}`;

                             const endDate = document.createElement('div');
                             endDate.textContent = `End Date: ${request.end_date}`;

                             const shift = document.createElement('div');
                             shift.textContent = `Shift: ${request.shift_number}`;

                             const hoursGone = document.createElement('div');
                             hoursGone.textContent = `Hours Gone: ${request.hours_gone}`;

                             const supervisor = document.createElement('div');
                             supervisor.textContent = `Supervisor: ${request.approval}`;

                             const statusText = document.createElement('div');
                             statusText.classList.add('status-text');
                             statusText.textContent = `Status: ${request.approval_status}`;

                             requestCardBottom.appendChild(startDate);
                             requestCardBottom.appendChild(endDate);
                             requestCardBottom.appendChild(shift);
                             requestCardBottom.appendChild(hoursGone);
                             requestCardBottom.appendChild(supervisor);
                             requestCardBottom.appendChild(statusText);

                             requestCard.appendChild(requestCardTop);
                             requestCard.appendChild(requestCardBottom);

                             container.appendChild(requestCard);
                         })
                    } else {
                        const noRequestMessage = document.createElement('p');
                        noRequestMessage.textContent = 'No requests found.';
                        container.appendChild(noRequestMessage);
                    }

                    const resetButton = document.createElement('button');
                    resetButton.classList.add('reset-button');
                    resetButton.textContent = 'Reset';
                    resetButton.addEventListener('click', function() {location.reload();});
                    container.appendChild(resetButton);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    }
});
