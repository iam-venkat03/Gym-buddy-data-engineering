document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const preferredTime1 = document.getElementById('preferred-time1');
    const preferredTime2 = document.getElementById('preferred-time2');

    form.addEventListener('submit', function (event) {
        if (preferredTime1.value === preferredTime2.value) {
            alert('Preferred Time 1 and Preferred Time 2 must be different.');
            event.preventDefault();
        }
    });
});