var element = document.getElementById("number-of-persons");

element.addEventListener('input', () => {
    var inputValue = element.value;
    var table = document.querySelector('.my-matrix');
    table.innerHTML = '';

    var transactions = []; // Array to store the transactions

    for (var i = 0; i < inputValue; i++) {
        var newRow = document.createElement('tr');
        newRow.classList.add('display-row');

        var th = document.createElement('th');
        th.classList.add('person-name');

        var personLabel = String.fromCharCode('A'.charCodeAt(0) + i);
        th.innerHTML = 'Person ' + personLabel + ' pays:';
        newRow.appendChild(th);

        for (var j = 0; j < inputValue; j++) {
            var td = document.createElement('td');
            td.classList.add('input-weight');
            var input = document.createElement('input');
            input.setAttribute('class', 'edge-weight');
            input.setAttribute('placeholder', 'Enter value here');
            input.setAttribute('type', 'number');
            td.appendChild(input);
            newRow.appendChild(td);

            (function(rowIndex, colIndex) {
                input.addEventListener('input', function() {
                    transactions[rowIndex * inputValue + colIndex].amount = parseInt(this.value);
                });
            })(i, j);

            var transaction = {
                payer: personLabel,
                payee: String.fromCharCode('A'.charCodeAt(0) + j),
                amount: 0 // Default amount
            };
            transactions.push(transaction);
        }

        table.appendChild(newRow);
    }

    var submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', function() {
        displayTransactions(transactions);
        sendTransactionsToServer(transactions);
    });
});

function displayTransactions(transactions) {
    console.log({"transactions": transactions});
}


// Function to display result in list format
function displayResult(resultData) {
    // Get the ul element where you want to display the result
    const resultList = document.getElementById('result-list');

    // Clear any existing content
    resultList.innerHTML = '';

    // Loop through the result array and create list items
    resultData.result.forEach(item => {
        // Create list item element
        const listItem = document.createElement('li');
        // Set the text content of the list item
        listItem.textContent = item;
        // Append the list item to the unordered list
        resultList.appendChild(listItem);
    });

  const imageDiv = document.getElementById('graph-image');
  imageDiv.innerHTML = `<img src="https://ameykulkarni.onrender.com/projects/cash-flow-minimizer/static/graph.png alt="Graph">`;



}

function sendTransactionsToServer(transactions) {
    fetch('"https://ameykulkarni.onrender.com/projects/cash-flow-minimizer/min-flow', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "transactions": transactions })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Transactions successfully sent:', data["result"]);
        displayResult(data);
    })
    .catch(error => {
        console.error('Error sending transactions:', error);
    });
}
function isMobileDevice() {
    return window.innerWidth <= 768; // Adjust the threshold as needed
}

// Function to display an alert if the page is viewed on a mobile device
function showAlertForMobile() {
    if (isMobileDevice()) {
        alert('This might not look best on a mobile phone. Please use a Bigger Screen on use phone in Landscape Mode for the best experience.');
    }
}

// Call the function to display the alert when the page loads
window.onload = showAlertForMobile;
