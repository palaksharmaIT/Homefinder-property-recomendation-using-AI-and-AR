document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordField = document.getElementById('password');
    const toggleButton = document.getElementById('togglePassword');

    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleButton.textContent = 'Hide';
    } else {
        passwordField.type = 'password';
        toggleButton.textContent = 'Show';
    }
});

document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission for demonstration

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simple validation (you can replace this with actual validation logic)
    if (username === '' || password === '') {
        showMessage('Please fill in all fields.');
    } else {
        showMessage('Login successful!'); // Replace with actual login logic
        // Here you would typically send the data to the server
    }
});

function showMessage(message) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
}