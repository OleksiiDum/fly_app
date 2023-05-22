'use strict'

const form = document.forms.login;
const email = form.elements.email;
const password = form.elements.password;
const submit = form.elements.submit;
const errorSpan = document.querySelector("span.error");
const emailExp = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);
const passwordExp = new RegExp(/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/);

document.body.style.backgroundImage = "url('static/new-zeeland.png')";
document.body.style.backgroundSize = "cover";
submit.style.backgroundColor = '#e7ecf3';
submit.style.color = '#000';

form.addEventListener('submit', async(event)=> {
    event.preventDefault();
    let response = await fetch('/login', {
        method: 'POST',
        body: new FormData(form)
      });
  
      let result = await response.json();
      if( result.status == true){
        location.assign(location.origin);
      } else{
        form.reset();
        errorSpan.innerHTML = result.message;
      }
});

email.addEventListener('input', (event)=> {
    validateEmail(event.target.value);
});

password.addEventListener('input', (event)=> {
    validatePassword(event.target.value);
});

function validateEmail(text){
    if (emailExp.test(text) == true){
        email.style.background = "#fff";
        errorSpan.innerHTML = ' ';
        errorSpan.background = 'none';
        return true;
    }
    else {
        email.style.background = "pink";
        errorSpan.innerHTML = "Email Not Valid";
        errorSpan.style.display = "inline";
        errorSpan.style.background = "pink";
        errorSpan.style.color = '#000';
        submit.disabled = true;
        submit.style.backgroundColor = '#e7ecf3';
        submit.style.color = '#000';
        return false
    }
};

function validatePassword(text){
    if(passwordExp.test(text) == true){
        errorSpan.innerHTML = '';
        submit.disabled = false;
        submit.style.backgroundColor = '#2e196a';
        submit.style.color = '#e7ecf3';
        return true;
    }else{
        errorSpan.style.display = "inline";
        errorSpan.style.background = "pink";
        errorSpan.style.color = '#000';
        errorSpan.innerHTML = "Minimum eight characters, at least one letter, one number and one special character";
        return false;
    };
};
