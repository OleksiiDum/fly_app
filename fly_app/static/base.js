const regLink = document.getElementsByClassName('registration-link');
const loginLink = document.getElementsByClassName('login-link');

regLink[0].addEventListener('click', function() {
    const regWindow = document.getElementsByClassName('registration-form');
    regWindow[0].classList.toggle('hidden');
    const falseBackground = document.getElementsByClassName('false-background');
    falseBackground[0].classList.toggle('hidden');
});

loginLink[0].addEventListener('click', function() {
    const loginWindow = document.getElementsByClassName('login-form');
    loginWindow[0].classList.toggle('hidden');
    const falseBackground = document.getElementsByClassName('false-background');
    falseBackground[0].classList.toggle('hidden');
});