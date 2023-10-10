"use strict";

const FORM_STATE = {};

const forms = document.querySelectorAll(".form");
const tabs = document.querySelectorAll(".tabs");
const allForms = ["flights", "passengers", "seats", "payments", "confirmAll"];

const dateBtn = document.querySelector(".dateBtn");

function neededForm(i) {
  let myform = document.forms[allForms[i]];
  return myform;
}

function neededTab(i) {
  let tab = document.getElementsByClassName(allForms[i] + "Tab")[0];
  return tab;
}

forms.forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    let formName = event.target.name;
    let formIndex = allForms.indexOf(formName);
    const clickedButton = event.submitter;
    if (clickedButton.value == "Next") {
      activeTab(neededTab(formIndex + 1));
      showForm(neededForm(formIndex + 1));
    } else if (clickedButton.value == "Back") {
      activeTab(neededTab(formIndex - 1));
      showForm(neededForm(formIndex - 1));
    }
  });
});

let myIndex = 0;

function carousel() {
  let i;
  const x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  myIndex++;
  if (myIndex > x.length) {
    myIndex = 1;
  }
  x[myIndex - 1].style.display = "block";
  setTimeout(carousel, 5000);
}

carousel();

function activeTab(tabName) {
  tabs.forEach((tab) => {
    tab.classList.remove("active");
  });
  tabName.classList.add("active");
}

function showForm(formName) {
  forms.forEach((form) => {
    form.classList.add("hidden");
    formName.classList.remove("hidden");
  });
}
