"use strict";

const passengersForm = document.forms.passengers;
const selectPassenger = passengersForm.elements.passengers;
const nextPassenger = document.querySelector("button.person");
const nextPassengerDiv = document.querySelector(".next-passenger");
const deleteBtn = document.querySelector(".delete");

nextPassenger.addEventListener("click", () => {
  let select = document.createElement("select");
  let deletePassenger = document.createElement("div");
  deletePassenger.innerHTML = "-";
  deletePassenger.classList.add("delete");
  deletePassenger.addEventListener("click", () => {
    select.remove();
    deletePassenger.remove();
  });
  select.innerHTML = document.getElementById("passenger").innerHTML;
  nextPassengerDiv.append(select);
  nextPassengerDiv.append(deletePassenger);
});

let getAllPassengers = async function () {
  let result = await fetch("/user_info");
  let data = await result.json();
  return data;
};

getAllPassengers().then((data) => {
  if (data.passengers) {
    for (let passenger of data.passengers) {
      let opt = new Option(passenger.first_name + " " + passenger.last_name);
      opt.setAttribute("value", passenger.id);
      selectPassenger.append(opt);
    }
  }
});

// passengersForm.elements.passengers.addEventListener("change", (event) => {
//   //Button active
// });
