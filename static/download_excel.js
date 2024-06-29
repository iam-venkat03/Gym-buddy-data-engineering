// document.getElementById('download-excel').addEventListener('click', function() {
//     // Get current timestamp
//     var now = new Date();
//     var year = now.getFullYear().toString().slice(-2); // Extract last two digits of the year
//     var month = ('0' + (now.getMonth() + 1)).slice(-2); // Add leading zero if needed
//     var date = ('0' + now.getDate()).slice(-2); // Add leading zero if needed
//     var hours = ('0' + now.getHours()).slice(-2); // Add leading zero if needed
//     var minutes = ('0' + now.getMinutes()).slice(-2); // Add leading zero if needed
//     var timestamp = year + month + date + '_' + hours + minutes; // Concatenate parts

//     // Generate CSV content
//     var csvContent = '';
    
//     // Get table headers
//     var headers = document.querySelectorAll('#profiles-table th');
//     var headerRow = [];
//     headers.forEach(function(header) {
//         headerRow.push(header.innerText);
//     });
//     csvContent += headerRow.join(',') + '\n';
    
//     // Get table rows
//     var rows = document.querySelectorAll('#profiles-table tbody tr');
//     rows.forEach(function(row) {
//         var cells = row.querySelectorAll('td');
//         var rowData = [];
//         cells.forEach(function(cell, index) {
//             if (index === 2) { // If it's the email ID column
//                 // Retrieve the original unmasked email ID from the server-side data
//                 var originalEmail = cell.getAttribute('data-original-email');
//                 rowData.push(originalEmail);
//             } else {
//                 rowData.push(cell.innerText);
//             }
//         });
//         csvContent += rowData.join(',') + '\n';
//     });

//     // Create a CSV Blob
//     var blob = new Blob([csvContent], {type: 'text/csv'});
//     var a = document.createElement('a');
//     a.href = URL.createObjectURL(blob);
//     a.download = 'profiles_' + timestamp + '.csv'; // Append timestamp to file name
//     a.click();
// });

document.getElementById('download-excel').addEventListener('click', function() {
    // Get current timestamp
    var now = new Date();
    var year = now.getFullYear().toString().slice(-2); // Extract last two digits of the year
    var month = ('0' + (now.getMonth() + 1)).slice(-2); // Add leading zero if needed
    var date = ('0' + now.getDate()).slice(-2); // Add leading zero if needed
    var hours = ('0' + now.getHours()).slice(-2); // Add leading zero if needed
    var minutes = ('0' + now.getMinutes()).slice(-2); // Add leading zero if needed
    var timestamp = year + month + date + '_' + hours + minutes; // Concatenate parts

    // Generate CSV content
    var csvContent = '';
    
    // Get table headers
    var headers = document.querySelectorAll('#profiles-table th');
    var headerRow = [];
    headers.forEach(function(header, index) {
        // Exclude the last column (Actions column)
        if (index < headers.length - 1) {
            headerRow.push(header.innerText);
        }
    });
    csvContent += headerRow.join(',') + '\n';
    
    // Get table rows
    var rows = document.querySelectorAll('#profiles-table tbody tr');
    rows.forEach(function(row) {
        var cells = row.querySelectorAll('td');
        var rowData = [];
        cells.forEach(function(cell, index) {
            // Exclude the last cell in each row (Actions column)
            if (index < cells.length - 1) {
                if (index === 2) { // If it's the email ID column
                    // Retrieve the original unmasked email ID from the server-side data
                    var originalEmail = cell.getAttribute('data-original-email');
                    rowData.push(originalEmail);
                } else {
                    rowData.push(cell.innerText);
                }
            }
        });
        csvContent += rowData.join(',') + '\n';
    });

    // Create a CSV Blob
    var blob = new Blob([csvContent], {type: 'text/csv'});
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'profiles_' + timestamp + '.csv'; // Append timestamp to file name
    a.click();
});
