let main = document.querySelector("#main");
//empty boxes for coloring
for (let i=0;i<5000;i++){
    let box=document.createElement("div");
    box.setAttribute("class","box");
    main.appendChild(box);
}

let left = document.querySelector("#left");
//clear button
let clear = document.createElement("button");
clear.setAttribute("id","clear");
clear.textContent="CLEAR";
left.appendChild(clear);

//clear button functionality
let allBoxes = document.querySelectorAll(".box");
clear.addEventListener("click", function(){
    for (allBox of allBoxes){
        allBox.style.backgroundColor = "white";
    }
});
//color boxes
for (let j=0;j<30;j++){
    let colorBox=document.createElement("div");
    colorBox.setAttribute("class","color");
    colorBox.style.backgroundColor=getRandomColor();
    left.appendChild(colorBox);
}
//random color picker for boxes on left
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
//choosing color
let color;
let colorBoxes=document.querySelectorAll(".color");
for (colorBox of colorBoxes){
    colorBox.addEventListener("click", function(e){
        color = e.target.style.backgroundColor;
    });
}
//coloring the boxes
for (allBox of allBoxes){
    allBox.addEventListener("mousemove",function(e){
        if (e.buttons==1){
        e.target.style.backgroundColor = color;
        }
    })
};