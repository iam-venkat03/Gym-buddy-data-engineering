document.getElementById('download-excel').addEventListener('click', function() {
    // Get current timestamp
    var now = new Date();
    var year = now.getFullYear().toString().slice(-2); // Extract last two digits of the year
    var month = ('0' + (now.getMonth() + 1)).slice(-2); // Add leading zero if needed
    var date = ('0' + now.getDate()).slice(-2); // Add leading zero if needed
    var hours = ('0' + now.getHours()).slice(-2); // Add leading zero if needed
    var minutes = ('0' + now.getMinutes()).slice(-2); // Add leading zero if needed
    var timestamp = year + month + date + '_' + hours + minutes; // Concatenate parts
    
    // Generate unmasked HTML specifically for Excel download
    var unmaskedHTML = '<table><thead>';
    var headers = document.querySelectorAll('#profiles-table th');
    unmaskedHTML += '<tr>';
    headers.forEach(function(header) {
        unmaskedHTML += '<th>' + header.innerText + '</th>';
    });
    unmaskedHTML += '</tr></thead><tbody>';
    var rows = document.querySelectorAll('#profiles-table tbody tr');
    rows.forEach(function(row) {
        unmaskedHTML += '<tr>';
        var cells = row.querySelectorAll('td');
        cells.forEach(function(cell, index) {
            if (index === 2) { // If it's the email ID column
                // Retrieve the original unmasked email ID from the server-side data
                var originalEmail = cell.getAttribute('data-original-email');
                unmaskedHTML += '<td>' + originalEmail + '</td>';
            } else {
                unmaskedHTML += '<td>' + cell.innerText + '</td>';
            }
        });
        unmaskedHTML += '</tr>';
    });
    unmaskedHTML += '</tbody></table>';

    // Download as Excel
    var blob = new Blob([unmaskedHTML], {type: 'application/vnd.ms-excel'});
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'profiles_' + timestamp + '.xls'; // Append timestamp to file name
    a.click();
});
