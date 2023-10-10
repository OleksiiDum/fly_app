"use strict";

const form = document.forms.register;
const email = form.elements.email;
const password = form.elements.password;
const confirmPass = form.elements.confirm;
const submit = form.elements.submit;
const errorSpan = document.querySelector("span.error");
const emailExp = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);
const passwordExp = new RegExp(
  /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/
);
let emailValidation = false;

document.body.style.backgroundImage = "url('static/sea.png')";
document.body.style.backgroundSize = "cover";
submit.style.backgroundColor = "#e7ecf3";
submit.style.color = "#000";

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (confirmPassword(confirmPass.value)) {
    let response = await fetch("/register", {
      method: "POST",
      body: new FormData(form),
    });

    let result = await response.json();
    console.log(result);
    if (result.message == "OK") {
      location.assign(location.origin + "/login_page");
    } else {
      form.reset();
      errorSpan.innerHTML = result.message;
      errorSpan.style.background = "pink";
    }
  } else {
    errorSpan.innerHTML = "Password Not Match or Not Valid";
    errorSpan.style.background = "pink";
  }
});

email.addEventListener("input", (event) => {
  validateEmail(event.target.value);
});

password.addEventListener("input", (event) => {
  validatePassword(event.target.value);
});

confirmPass.addEventListener("input", (event) => {
  confirmPassword(event.target.value);
});

function cleanSpan() {
  errorSpan.innerHTML = " ";
  errorSpan.background = "none";
}

function validateEmail(text) {
  if (emailExp.test(text) == true) {
    email.style.background = "#fff";
    cleanSpan();
    emailValidation = true;
    return true;
  } else {
    email.style.background = "pink";
    errorSpan.innerHTML = "Email Not Valid";
    errorSpan.style.display = "inline";
    errorSpan.style.background = "pink";
    submit.disabled = true;
    submit.style.backgroundColor = "#e7ecf3";
    submit.style.color = "#000";
    emailValidation = false;
    return false;
  }
}

function validatePassword(text) {
  if (passwordExp.test(text) == true) {
    cleanSpan();
    return true;
  } else {
    errorSpan.style.display = "inline";
    errorSpan.style.background = "pink";
    errorSpan.innerHTML =
      "Minimum eight characters, at least one letter, one number and one special character";
    return false;
  }
}

function confirmPassword(text) {
  if (text.match(password.value) && validatePassword(text)) {
    cleanSpan();
    errorSpan.innerHTML = "Password Match";
    errorSpan.style.background = "none";
    if (emailValidation) {
      submit.disabled = false;
      submit.style.backgroundColor = "#2e196a";
      submit.style.color = "#e7ecf3";
    }
    return true;
  } else {
    errorSpan.style.display = "inline";
    errorSpan.style.background = "pink";
    errorSpan.innerHTML = "Password Not Match or Not Valid";
    return false;
  }
}
