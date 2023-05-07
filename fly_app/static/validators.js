'use strict'

const form = document.forms.register;
const email = form.elements.email;
const password = form.elements.password;
const confirmPass = form.elements.confirm;
const submit = form.elements.submit;
const errorSpan = document.querySelector("span.error");
const emailExp = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);
const passwordExp = new RegExp("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$");

form.addEventListener('submit', (event)=> {
    event.preventDefault;
});

email.addEventListener('input', (event)=> {
    validateEmail(event);
});

password.addEventListener('input', (event)=> {
    validatePassword(event);
});

confirmPass.addEventListener('input', (event)=> {
    confirmPassword(event);
});

function validateEmail(event){
    if (emailExp.test(event.target.value) == true){
        event.target.style.background = "#fff";
        errorSpan.innerHTML = ' ';
        errorSpan.background = 'none';
        submit.disabled = false;
        submit.style.backgroundColor = '#2e196a';
        submit.style.color = '#e7ecf3';
        if(validatePassword(event)){
            console.log("Done!");
        };
        return true;
    }
    else {
        event.target.style.background = "pink";
        errorSpan.innerHTML = "Not Valid";
        errorSpan.backgroundColor = 'pink';
        submit.disabled = true;
        submit.style.backgroundColor = '#e7ecf3';
        submit.style.color = '#000';
        return false
    }
};

function validatePassword(event){
    if(passwordExp.test(event.target.value) == true){
        errorSpan.innerHTML = '';
        console.log("Valid");
        return true;
    }else{
        errorSpan.innerHTML = "Minimum eight characters, at least one letter, one number and one special character";
        return false;
    };
};

function confirmPassword(event){
    if(event.target.value.match(password.value)){
        errorSpan.innerHTML = 'Match';
    }else{
        errorSpan.innerHTML = 'No';
    }
};