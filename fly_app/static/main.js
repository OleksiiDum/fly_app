'use strict'

const forms = document.querySelectorAll(".form");
const flightForm = document.forms.flights;
const passengerForm = document.forms.passengers;
const paymentForm = document.forms.payment;
const confirmForm = document.forms.confirm;

const tabs = document.querySelectorAll(".tabs");
const flightsTab = document.querySelector(".flights");
const passengersTab = document.querySelector(".passengers");
const paymentsTab = document.querySelector(".payments");
const confirmTab = document.querySelector(".confirm");

let myIndex = 0;

function carousel() {
  let i;
  const x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 5000); // Change image every 2 seconds
}

carousel();

function activeTab(tabName){
  tabs.forEach((tab)=>{
    tab.classList.remove("active");
  });
  tabName.classList.add("active");
};

function hideForms(formName){
  forms.forEach((form)=>{
    form.classList.add("hidden");
    formName.classList.remove("hidden");
  })
};

flightsTab.addEventListener('click', (event)=> {
  activeTab(flightsTab);
  hideForms(flightForm);
})
passengersTab.addEventListener('click', (event)=> {
  activeTab(passengersTab);
  hideForms(passengerForm);
})
paymentsTab.addEventListener('click', (event)=> {
  activeTab(paymentsTab);
  hideForms(paymentForm);
})
confirmTab.addEventListener('click', (event)=> {
  activeTab(confirmTab);
  hideForms(confirmForm);
})