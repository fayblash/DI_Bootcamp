// Exercise 1 : Move The Box
// Instructions
// Move the box from left to right

function myMove() {
    let box = document.getElementById("animate");   
    let loc = 0;
    let id = setInterval(frame, 5);
    function frame() {
      if (loc === 350) {
        setInterval(reverse,5);  
        //clearInterval(id);
      } else {
        loc++; 
        box.style.top = loc + 'px'; 
        box.style.left = loc + 'px'; 
      }
    }
    function reverse (){
        if (loc >0){
        loc--;
        box.style.top = loc + 'px'; 
        box.style.right = loc + 'px'; 
        }
        else{
            clearInterval(id);
        }
    }
  }
// Exercise 2: Drag & Drop
// Instructions
// Create a draggable square/box element in your HTML file.
// In your javascript file add the functionality which will allow you to drag the square/box and drop it into a larger box.
function allowDrop(ev) {
    ev.preventDefault(); 
  }
function dragStart(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    }
    
function dragDrop(ev) {
    ev.preventDefault();
  
    let data = ev.dataTransfer.getData("text");
     
    let box = document.getElementById(data)
    ev.target.appendChild(box);
    }
//if not using inline event listeners to buttons directly
let box1 = document.querySelector("#box1");
let box2 = document.querySelector("#box2");
let box3 = document.querySelector("#box3");

box1.addEventListener("dragstart", dragStart);

box2.addEventListener("dragstart", dragStart);
box2.addEventListener("dragover", allowDrop);
box2.addEventListener("drop", dragDrop);

box3.addEventListener("dragover", allowDrop);
box3.addEventListener("drop", dragDrop);



   
    