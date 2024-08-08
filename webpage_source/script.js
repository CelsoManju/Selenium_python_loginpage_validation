document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var username = document.getElementById('txt_inp_username').value;
    var password = document.getElementById('txt_inp_password').value;
    var message = document.getElementById('p_message');
    
    if (username === 'admin' && password === 'password') {
        message.style.color = 'green';
        message.textContent = 'Login successful!';
    } else {
        message.style.color = 'red';
        message.textContent = 'Invalid username or password.';
    }
});
