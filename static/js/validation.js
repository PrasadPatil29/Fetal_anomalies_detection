// static/js/validation.js

function validateForm() {
    const fileInput = document.getElementById('file-input');
    const alertMessage = document.getElementById('alert-message');

    if (fileInput.files.length === 0) {
        alertMessage.classList.add('visible');
        return false; // Prevent form submission
    }

    alertMessage.classList.remove('visible');
    return true; // Allow form submission
}
