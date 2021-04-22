// Exercise 1 : Change The Article
// Instructions
{/* <article>
    <h1> Some Facts </h1>
    <h2> The Chocolate </h2>
    <h3>History of the chocolate</h3>
    <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
    Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
    <p> After the European discovery of the Americas, chocolate became 
    very popular in the wider world, and its demand exploded. </p>
    <p> Chocolate has since become a popular food product that millions enjoy every day, 
    thanks to its unique, rich, and sweet taste.</p> 
    <p> But what effect does eating chocolate have on our health?</p> 
</article>
<form id="myForm">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit" id="submit">
</form> 
<div class="usersAnswer"></div> */}


// // Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
// let article = document.querySelector("article");
// article.removeChild(article.lastElementChild);
// // Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
// let h2 = document.querySelector("h2");
// h2.addEventListener("click",function(){
// 	h2.style.backgroundColor = "red";});
// // Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)
// let h1 = document.querySelector("h1");
// let randSize = Math.floor(Math.random() * 101); 
// h1.style.fontSize = `${randSize}px`;
// // Add an event listener which will hide the h3 when it’s clicked on (use the display property).
// let h3=document.querySelector("h3");
// h3.addEventListener("click",function(){
//     h3.style.display = "none";
// })
// // Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// //<button type="button" id="Bold">Bold</button>

// let btn = document.querySelector("#Bold");
// let allP = document.querySelectorAll("p");

// function bold(){
//     for (let par of allP){
//         let text = par.innerHTML;
//         par.innerHTML = text.bold();
//     }
// }
// btn.addEventListener("click",bold);
// When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.
let form = document.querySelector("#myForm");
let fname = document.querySelector("#fname");
let lname = document.querySelector("#lname");

form.addEventListener("submit", makeTable);

function makeTable(e){
e.preventDefault();
let table = document.createElement("table");
let tbody = document.createElement("tbody");
table.style.border = "1px solid black";
let tr = tbody.insertRow(0);
let cell1 = tr.insertCell(0);
cell1.style.border = "1px solid black";
let cell2 = tr.insertCell(1);
cell2.style.border = "1px solid black";
cell1.innerHTML = fname.value;
cell2.innerHTML = lname.value;
table.appendChild(tbody);
document.body.appendChild(table);
}

// // When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
// allP[1].addEventListener("mouseover", function(){
//     allP[1].style.opacity = "0.5";
// }); 
// allP[1].addEventListener("mouseout",function(){
//     allP[1].style.opacity = "1";    
// })

// // Exercise 2 : Transform The Sentence
// // Instructions
// // Add this sentence to your HTML file then follow the steps :

// // <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// // <strong>end</strong> you <strong>will</strong> be great Developers!
// // <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>


// // Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph.
// let arrStrong = document.querySelectorAll("strong");

// // Create a function called highlight() that changes the color of all the bold text to blue.
// function highlight(){
//     this.style.color = "blue"
// }
// // Create a function called return_normal() that changes the color of all the bold text back to black.
// function return_normal(){
//     this.style.color = "black";
// }
// // Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
// for (let strong of arrStrong) {
//     strong.addEventListener("mouseover", highlight);
//     strong.addEventListener("mouseout", return_normal);
// }
// // Exercice 3 : Volume Of A Sphere
// // Instructions
// // Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
// // <!doctype html> 
// // <html lang="en"> 
// //     <head> 
// //         <meta charset="utf-8"> 
// //         <title>Volume of a Sphere</title> 
// //         <style>  
// //             body{padding-top:30px;} 
// //             label,input{display:block;}  
// //         </style> 
// //     </head> 
// //     <body> 
// //         <p>Input radius value and get the volume of a sphere.</p> 
// //         <form  id="MyForm"> 
// //             <label for="radius">Radius</label><input type="text" name="radius" id="radius" required> 
// //             <label for="volume">Volume</label><input type="text" name="volume" id="volume"> 
// //             <input type="submit" value="Calculate" id="submit">    
// //         </form> 
// //     </body> 
// // </html> 
//         let radius = document.querySelector("#radius");
//         let volume = document.querySelector("#volume");
//         let form = document.querySelector("#MyForm");

//         form.addEventListener("submit", calcVol);

//         function calcVol(e){
//             e.preventDefault();
//             let r = radius.value;
//             console.log(r);
//             let volumeVal = (4/3) * Math.PI * r**3;
//             console.log(volumeVal);
//             volume.value = volumeVal;
//         }

// // Bonus Exercise 4 : Event Listeners
// // Instructions
// // Add as many events listeners as possible to one element on your webpage. Each listener should do a different thing, for instance- change position x, change position y, change color, change the font size… and more.
// let h1 = document.querySelector("h1");
// h1.addEventListener("click",function(){
//     h1.style.color = "aquamarine";
// })
// h1.addEventListener("mouseover", function(){
//     h1.style.fontSize="x-large";
// })
// h1.addEventListener("mouseout", function(){
//     h1.innerHTML="I've changed!!";
// })

