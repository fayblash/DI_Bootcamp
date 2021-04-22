// //exercise 1 Box Animation
// let plus = document.querySelector("#plus");
// let container = document.querySelector("#container");

// plus.addEventListener("click", createBox);

// function createBox(){
//     let box=document.createElement("div");
//     box.setAttribute("class","box"); 
//     box.style.backgroundColor=getRandomColor();
//     container.appendChild(box);
// }

// function getRandomColor() {
//     var letters = '0123456789ABCDEF';
//     var color = '#';
//     for (var i = 0; i < 6; i++) {
//       color += letters[Math.floor(Math.random() * 16)];
//     }
//     return color;
//   }

// //exercise 3
// document.addEventListener("mousemove",animatedCircles);

// function animatedCircles(ev) {
//     let circle = document.createElement('div');
//     circle.setAttribute('class', 'circle');
//     document.body.appendChild(circle);

//     circle.style.left = ev.clientX + 'px';
//     circle.style.top = ev.clientY + 'px';
//     circle.style.borderColor = getRandomColor();

//     circle.style.transition = 'all 0.5s linear 0s';

//     circle.style.left = circle.offsetLeft - 20 + 'px';
//     circle.style.top = circle.offsetTop - 20 + 'px';

//     circle.style.width = '100px';
//     circle.style.height = '100px';
//     circle.style.borderWidth = '5px';
//     circle.style.borderRadius="50%";
//     circle.style.opacity = 0;
// }

//exercise 2
let circle = document.querySelector("#circle");  
let dot = document.querySelector("#dot"); 
dot.textContent="Loading"; 
let letters = document.querySelector("#letters"); 
let loading = ["L","O","A","D","I","N","G"];
let i=0;

function dotChanger(){
    if (dot.textContent==="Loading....."){
        dot.textContent="Loading";
    } else{
    dot.textContent+=".";
    }
}

function letterChanger(){
    if (i<7){        
    letters.textContent= "*".repeat(i) + loading[i] + "*".repeat(6-i);
    i++;
 }
    else{
    i=0;
     }
}

window.setInterval(dotChanger, 200);
window.setInterval(letterChanger, 1000);

