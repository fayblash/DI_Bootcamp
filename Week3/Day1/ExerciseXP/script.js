// Exercise 1 : Change The Navbar
// Instructions
//  <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>

// In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
document.getElementsByTagName("DIV"[0]).setAttribute("id","socialNetworkNavigation");

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
let newLI = document.createElement("LI");
// Create a new text node with “Logout” as its specified text.
let txtNd = document.createTextNode("Logout");
// Append the text node to the newly created list node (li).
newLI.appendChild(txtNd);
// Finally, append this updated list node to the unordered list above, using the appendChild method.
document.getElementsByTagName("UL"[0]).appendChild(newLI);
// Bonus

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements from their parent element (ul). Display the text of each link. (Hint: use the textContent property).
document.getElementByTagName("UL"[0]).firstElementChild.textContent;
document.getElementByTagName("UL"[0]).lastElementChild.textContent;

// Exercise 2 : Users
// Instructions
// <html>
// <body>
//   <div id="container">Users:</div>
//   <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
//   <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
//   </ul>
// </body>
// </html>


// In the HTML above change the name “Pete” to “Richard”.
document.getElementsByTagName("UL"[0]).lastElementChild.textContent="Richard";
// Change each first name of the two <ul>'s to your name.
document.getElementsByClassName("list").firstElementChild.textContent="Fay";
// At the end of each <ul> add a <li> that says “Hey students”.
let newLI1 =document.createElement("li");
let newLI2 =document.createElement("li");

newLI1.innerHTML = "Hey Students";
newLI2.innerHTML = "Hey Students";

documents.getElementsByTagName("UL"[0]).appendChild(newLI1);
documents.getElementsByTagName("UL"[1]).appendChild(newLI2);
// Delete the name Sarah from the second <ul>.
documents.getElementByTagName("UL"[1]).children[1].innerHTML = "";
// Bonus

// Add a class called student_list to both of the <ul>'s.
document.getElementsByClassName("list").className += "student_list";
// Add the classes university and attendance to the first <ul>.
documents.getElementsByTagName("UL"[0]).className+= "university, attendance";


// Exercise 3 : Users And Style
// Instructions
// <html>
// <body>
//   <div>Users:</div>
//   <ul>
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
// </body>
// </html>


// For the following exercise use the HTML presented above:

// Add a “light blue” background color and some padding to the <div>.
let myDiv = document.getElementsByTagName("DIV"[0]);
myDiv.style.backgroundColor="light blue";
myDiv.style.padding ="50px";
// Do not display the first name (John) in the list.
document.getElementsByTagName("LI"[0]).style.display = "none";
// Add a border to the second name (Pete).
document.getElementsByTagName("LI"[1]).style.border = "1px solid black";
// Change the font size of the whole body.
document.body.style.fontSize = "x-large";
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
if (myDiv.style.backgroundColor==="light blue"){
    alert(`Hello ${document.getElementsByTagName("LI"[0])} and ${document.getElementsByTagName("LI"[1])}`);
}