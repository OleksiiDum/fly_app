const form = document.forms.passengers;
// const add = form.elements.add;
const fName = form.elements.first;
const fNameExp = new RegExp(/^[a-z ,.'-]+$/i)
const lName = form.elements.last;
const lNameExp = new RegExp(/^[a-z ,.'-]+$/i)
const nationality = form.elements.nationality;
const passport = form.elements.passport;
const passportExp = new RegExp(/^[a-z ,.'-]+$/i)
const age = form.elements.age;
const submit = form.elements.submit;
const errorSpan = document.querySelector("span.error");
const passengersList = document.querySelector(".passengers-list");

form.addEventListener("submit", (event)=>{
    event.preventDefault();
    let formData = new FormData(form);
    let response = fetch('/add_passenger', {
        method: 'POST',
        body: formData
      });
    //   console.log(...formData);
    response.then(r=>r.json()).then((passengers)=>{
        passengersList.innerHTML = null;
        console.log(passengers);
        for(let p of passengers){
            let li = document.createElement("li");
            li.textContent = p.first_name + ' ' + p.last_name;
            passengersList.append(li);
        }
        form.reset();
    });
});

fName.addEventListener('input', (event)=> {
    validateFirstName(event.target.value);
});

lName.addEventListener('input', (event)=> {
    validateLastName(event.target.value);
});

passport.addEventListener('input', (event)=> {
    validatePassport(event.target.value);
});

age.addEventListener('input', (event)=> {
    validateAge(event.target.value);
});

function validateFirstName(text){
    if (fNameExp.test(text) == true){
        fName.style.background = "#fff";
        errorSpan.innerHTML = ' ';
        errorSpan.background = 'none';
        return true;
    }
    else {
        fName.style.background = "pink";
        errorSpan.innerHTML = "Name Not Valid";
        errorSpan.style.display = "inline";
        errorSpan.style.background = "pink";
        // submit.style.backgroundColor = '#e7ecf3';
        // submit.style.color = '#000';
        return false
    }
};

function validateLastName(text){
    if (lNameExp.test(text) == true){
        lName.style.background = "#fff";
        errorSpan.innerHTML = ' ';
        errorSpan.background = 'none';
        return true;
    }
    else {
        lName.style.background = "pink";
        errorSpan.innerHTML = "Last Name Not Valid";
        errorSpan.style.display = "inline";
        errorSpan.style.background = "pink";
        // submit.style.backgroundColor = '#e7ecf3';
        // submit.style.color = '#000';
        return false
    }
};

function validatePassport(text){
    if (passportExp.test(text) == true){
        passport.style.background = "#fff";
        errorSpan.innerHTML = ' ';
        errorSpan.background = 'none';
        return true;
    }
    else {
        passport.style.background = "pink";
        errorSpan.innerHTML = "Passport Not Valid";
        errorSpan.style.display = "inline";
        errorSpan.style.background = "pink";
        // submit.style.backgroundColor = '#e7ecf3';
        // submit.style.color = '#000';
        return false
    }
};

function validateAge(text){
    if(0 > text > 200){
        age.style.background = "pink";
        errorSpan.innerHTML = 'Impossible age';
        errorSpan.background = 'pink';
        return false;
    } else {
        errorSpan.innerHTML = ' ';
        errorSpan.background = 'none';
        return true;
    }
}