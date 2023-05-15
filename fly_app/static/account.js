const form = document.forms.passengers;
const add = form.elements.add;
console.log(add, form);

add.addEventListener("submit", (event)=>{
    event.preventDefault();
    let formData = new FormData(form);
    let response = fetch('/add_passenger', {
        method: 'POST',
        body: formData
      });
    response.then(r=>r.json()).then(data=>console.log(data));
})