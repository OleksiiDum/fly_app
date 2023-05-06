'use strict'

let registrationForm = document.forms.registration;
let errorSpan = document.querySelector("span.error");

registrationForm.addEventListener("submit", (event)=> {
    event.preventDefault();
    validateEmail(event);
    validatePassword(event);
});

function validateEmail(event){
    let email = event.email;
};

function validatePassword(event){
    let password = event.password;
    let submitPassword = event.submit-password;
};