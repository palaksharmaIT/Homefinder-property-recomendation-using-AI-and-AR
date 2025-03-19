/*let people = document.getElementById('people');
let people_less = document.getElementById('people_less');
let people_more = document.getElementById('people_more');

let people_index = 4;

people_less.addEventListener('click', () => {
    people_index -=1;
    
    if(people_index <=0){
        people_index =1;
        people.value = people_index + 'People';
    }
    else {
        people.value = people_index + 'People';
    }
})

people_more.addEventListener('click', () => {
    people_index += 1;

    if(people_index >=4){
        people_index =4;
        people.value = people_index + 'People';
    }
    else{
        people.value = people_index + 'People';
    }
})*/
const MAX_PEOPLE = 10; // You can change this limit
let people_index = 1; // Start from 1

const people_more = document.getElementById('people_more');
const people_less = document.getElementById('people_less');
const people = document.getElementById('people');

people_more.addEventListener('click', () => {
    people_index = Math.min(people_index + 1, MAX_PEOPLE); // Limit to MAX_PEOPLE
    people.value = people_index + ' People';
});

people_less.addEventListener('click', () => {
    people_index = Math.max(people_index - 1, 1); // Ensure minimum is 1
    people.value = people_index + ' People';
});


let checkout_data = document.getElementById('checkout_data');
let checkout = document.getElementById('checkout');
let checkin_data = document.getElementById('checkin_data');
let checkin = document.getElementById('checkin');


checkin.addEventListener('change', () => {
    let checkin_value = checkin.value;
    //console.log(checkin_value);

    let dates = new Date(checkin_value);
    let dates2 = new Date();
    const week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    let day = week[dates.getDay()];
    //console.log(day)

    let date = dates.getDate();
    //console.log(date);

    let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    let month = months[dates.getMonth()];
    //console.log(month);

    if (dates < dates2) {
        console.log('No Date');
    } else {
        checkin_data.innerText = day + ' , ' + date + ' ' + month;
    }
})
checkout.addEventListener('change', () => {
    let checkout_value = checkout.value;
    let checkin_value = checkin.value;
    //console.log(checkin_value);

    let dates = new Date(checkout_value);
    let dates2 = new Date(checkin_value);
    const week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    let day = week[dates.getDay()];
    //console.log(day)

    let date = dates.getDate();
    //console.log(date);

    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    let month = months[dates.getMonth()];
    //console.log(month);

    if (dates < dates2) {
        console.log('No Date');
    } else {
        console.log(day + ' , ' + date + ' ' + month)
        checkout_data.innerText = day + ' , ' + date + ' ' + month;
    }
})

let checkin_more = document.getElementById('checkin_more');
let checkin_less = document.getElementById('checkin_less');
let checkout_more = document.getElementById('checkout_more');
let checkout_less = document.getElementById('checkout_less');


checkin_more.addEventListener('click', () => {
    const week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    let today = new Date();
    let tomorrow = new Date(today);

    tomorrow.setDate(tomorrow.getDate() + 1);

    let day = week[tomorrow.getDay()];
    let date = tomorrow.getDate();
    let month = months[tomorrow.getMonth()];

    checkin_data.innerText = day + ' , ' + date + ' ' + month;

})

checkin_less.addEventListener('click', () => {
    const week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    let today = new Date();
    //let tomorrow = new Date(today);

    //tomorrow.setDate(tomorrow.getDate() + 1);

    let day = week[today.getDay()];
    let date = today.getDate();
    let month = months[today.getMonth()];

    checkin_data.innerText = day + ' , ' + date + ' ' + month;

})

checkout_more.addEventListener('click', () => {
    const week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    let today = new Date();
    let tomorrow = new Date(today);

    tomorrow.setDate(tomorrow.getDate() + 2);

    let day = week[tomorrow.getDay()];
    let date = tomorrow.getDate();
    let month = months[tomorrow.getMonth()];

    checkout_data.innerText = day + ' , ' + date + ' ' + month;

})

checkout_less.addEventListener('click', () => {
    const week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    let today = new Date();
    let tomorrow = new Date(today);

    tomorrow.setDate(tomorrow.getDate() + 1);

    let day = week[tomorrow.getDay()];
    let date = tomorrow.getDate();
    let month = months[tomorrow.getMonth()];

    checkin_data.innerText = day + ' , ' + date + ' ' + month;

})

/*const images = [
   { image: "img6.jpg", repeat: "no-repeat", position: "center", size: "cover" },
   { image: "img14.jpeg", repeat: "no-repeat", position: "center", size: "cover" },
   { image: "img15.jpg", repeat: "no-repeat", position: "center", size: "cover" }
];


let index = 1;
let h6 = document.getElementById('h6');
h6.innerText="+" + images.length;

let btn_left = document.getElementById('btn_left');
let btn_right = document.getElementById('btn_right');
let style = document.getElementsByClassName('content')[0].style;

btn_left.addEventListener('click' , () => {
   index -= 1;
   if(index < 0){
       index = (images.length) - 1;
   }
   style.setProperty('--background' , images[index])
})

btn_right.addEventListener('click' , () => {
   index ++
       if(index > (images.length) -1){
          index = 0;
       };
   
   style.setProperty('--background' , images[index])
})*/



const images = [
    { image: "img6.jpg", repeat: "no-repeat", position: "center", size: "cover" },
    { image: "img14.jpeg", repeat: "no-repeat", position: "center", size: "cover" },
    { image: "img15.jpg", repeat: "no-repeat", position: "center", size: "cover" },
    { image: "img11.webp", repeat: "no-repeat", position: "center", size: "cover" },
    { image: "img9.png", repeat: "no-repeat", position: "center", size: "cover" },
    { image: "img8.jpg", repeat: "no-repeat", position: "center", size: "cover" }
];

let index = 0;
let h6 = document.getElementById('h6');
if (h6) {
    h6.innerText = "+" + images.length;
}

let btn_left = document.getElementById('btn_left');
let btn_right = document.getElementById('btn_right');
let content = document.getElementsByClassName('content')[0];

function updateBackground() {
    content.style.backgroundImage = `url('${images[index].image}')`;
    content.style.backgroundRepeat = images[index].repeat;
    content.style.backgroundPosition = images[index].position;
    content.style.backgroundSize = images[index].size;
}

btn_left.addEventListener('click', () => {
    index = (index - 1 + images.length) % images.length;
    updateBackground();
});

btn_right.addEventListener('click', () => {
    index = (index + 1) % images.length;
    updateBackground();
});

// Set initial background
updateBackground();