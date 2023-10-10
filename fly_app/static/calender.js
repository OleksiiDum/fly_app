"use strict";

const flightsForm = document.forms.flights;
const dateOfFlight = flightsForm.elements.date;
const fromCity = flightsForm.elements.from;
const toCity = flightsForm.elements.to;
const submitFlights = flightsForm.elements.submit;
const calenderWindow = document.querySelector(".calender");
const monthWindow = document.querySelector(".month");
const weekDays = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"];
const closeDateWindow = document.querySelector(".btn");
const openDateWindow = document.querySelector(".dateBtn");

const months = [
  { January: 31 },
  { February: 28 },
  { March: 30 },
  { April: 31 },
  { May: 30 },
  { June: 31 },
  { July: 30 },
  { August: 31 },
  { September: 30 },
  { October: 31 },
  { November: 30 },
  { December: 31 },
];

async function getFlightDays() {
  let airports = {
    from: fromCity.value,
    to: toCity.value,
  };
  let url = "/get_flight";
  let request = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8",
    },
    body: JSON.stringify(airports),
  });
  let response = await request.json();
  return response;
}

function showMonth(year, monthObj, day) {
  monthWindow.innerHTML = null;
  for (const [m, d] of Object.entries(monthObj)) {
    const month = document.createElement("div");
    month.classList.add("month");
    var monthHead = document.createElement("header");
    monthHead.innerText = m + " " + year;
    monthWindow.append(monthHead);
    monthWindow.append(month);
    for (let num of Array(d).keys()) {
      let monthday = document.createElement("div");
      monthday.classList.add("day");
      monthday.innerText = num + 1;
      if (num == day - 1) {
        monthday.style.fontSize = "18px";
        monthday.style.backgroundColor = "#9996";
      }
      month.append(monthday);
    }
  }
  const days = document.querySelectorAll(".day");

  days.forEach((monthday) => {
    getFlightDays().then((data) => {
      if (monthday.innerText == data[0].flight[2].slice(-2)) {
        monthday.classList.add("active");
        monthday.addEventListener("click", () => {
          let num = monthday.innerText;
          calenderWindow.classList.add("hidden");
          dateOfFlight.value = num + " " + monthHead.innerText;
          if (fromCity.value != null && toCity.value != null) {
            submitFlights.disabled = false;
          }
        });
      }
    });
  });
}

closeDateWindow.addEventListener("click", (event) => {
  event.preventDefault();
  calenderWindow.classList.add("hidden");
});
openDateWindow.addEventListener("click", (event) => {
  event.preventDefault();
  const date = new Date();

  let day = date.getDate();
  let month = date.getMonth() + 1;
  let year = date.getFullYear();
  showMonth(year, months[month], day);
  calenderWindow.classList.remove("hidden");
});
