"use strict";

const from = document.querySelector(".inputFrom");
const to = document.querySelector(".inputTo");
const infoSpan = document.querySelector(".info-span");

async function getAirports() {
  let url = "/all_airports";
  let request = await fetch(url);
  let response = await request.json();
  return response;
}

getAirports();

async function getFlights(from_city, to_city) {
  let airports = {
    from: from_city,
    to: to_city,
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

function attachEvents(inputDiv) {
  const inputField = inputDiv.querySelector("input");
  const ulField = inputDiv.querySelector("ul");

  function renderSearch(cities) {
    ulField.innerHTML = null;
    for (let city of cities) {
      let li = document.createElement("li");
      li.textContent = city.city;
      ulField.append(li);
    }
  }

  ulField.addEventListener("click", (event) => {
    inputField.value = event.target.textContent;
    ulField.innerHTML = null;
    return;
  });

  window.addEventListener("click", () => {
    ulField.innerHTML = null;
  });

  inputField.addEventListener("input", (event) => {
    if (event.target.value.length < 3) {
      ulField.innerHTML = null;
      return;
    }

    let exp = `.*${event.target.value.toLowerCase()}.*`;

    getAirports()
      .then((data) => {
        return data.filter((airport) => {
          if (airport.city.toLowerCase().match(exp)) {
            return true;
          } else {
            return false;
          }
        });
      })
      .then(renderSearch);
  });
}

attachEvents(from);
attachEvents(to);

dateBtn.addEventListener("click", (event) => {
  const from_city = from.querySelector("input").value;
  const to_city = to.querySelector("input").value;
  getFlights(from_city, to_city)
    .then((data) => {
      // if (data[error]) {
      //   console.log(error);
      // }
      infoSpan.innerHTML = data[0].flight[2];
    })
    .catch((err) => (infoSpan.innerHTML = err));
});
