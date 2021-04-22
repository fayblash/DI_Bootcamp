// // Exercise 1 : Animation With The Alphabet
// // Instructions
// // Create multiple squares/boxes with letters inside. There should be 26 squares/boxes for all the letters (A to Z) next to each other.
// // Make all the squares draggable.
// // You should be able to drag and drop the letters depending on their coordinates x and y.
//     let letterBox=document.querySelector("#letterBox");
    
//     for (let i=0;i<26;i++){
//         let box=document.createElement("div");
//         let ltr = (i+10).toString(36);
//         box.setAttribute("id", ltr);
//         box.setAttribute("class","box");
//         box.setAttribute("draggable","true");
//         box.innerHTML = ltr;
//         box.addEventListener("dragstart", dragStart);
//         letterBox.appendChild(box);
//     }
    
//     function allowDrop(ev) {
//         ev.preventDefault(); 
//     }
//     function dragStart(ev) {
//         ev.dataTransfer.setData("text", ev.target.id);
//     }
        
//     function dragDrop(ev) {
//         ev.preventDefault();
      
//         let data = ev.dataTransfer.getData("text");
         
//         let box = document.getElementById(data)
//         ev.target.appendChild(box);
//     }
    
//     let wordBox=document.querySelector("#wordBox");
    
//     wordBox.addEventListener("dragover", allowDrop);
//     wordBox.addEventListener("drop", dragDrop);



// Exercise 2 : Animation With A Paragraph
// Instructions
// Create a paragraph and make it draggable.
// You should be able to drag and drop the paragraph.
// Change the font size of the paragraph according to the screen coordinates.
let par = document.createElement("p");
par.setAttribute("draggable","true");
par.setAttribute("id","par");
par.innerHTML="It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters. ‘My dear Mr. Bennet,’ said his lady to him one day, ‘have you heard that Netherfield Park is let at last?’ Mr. Bennet replied that he had not. ‘But it is,’ returned she; ‘for Mrs. Long has just been here, and she told me all about it.’ Mr. Bennet made no answer. ‘Do you not want to know who has taken it?’ cried his wife impatiently. ‘YOU want to tell me, and I have no objection to hearing it.’This was invitation enough.";
par.addEventListener("dragstart", dragStart);
let source=document.querySelector("#source");
source.appendChild(par);

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


let dropped1 = document.querySelector("#dropped1");
let dropped2 = document.querySelector("#dropped2");

dropped1.addEventListener("dragover", allowDrop);
dropped1.addEventListener("drop", dragDrop);

dropped2.addEventListener("dragover", allowDrop);
dropped2.addEventListener("drop", dragDrop);

