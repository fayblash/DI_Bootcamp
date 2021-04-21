// // Exercise 1 : Select A Kind Of Music
// // Instructions
// // <select id="genres">
// //   <option value="rock">Rock</option>
// //   <option value="blues" selected>Blues</option>
// //<div id="result"></div>
// // </select>

// // Display the value of the selected option.
// let selector = document.querySelector("#genres");
// selector.addEventListener('change', function() {
//   let result = document.querySelector("#result");
// result.innerHTML = this.value;
// }, false);
// // Add an additional option to the select tag:
// // <option value="classic">Classic</option>

// let option = document.createElement("option");
// option.innerHTML = "Classic";
// option.setAttribute('selected', 'selected')
// selector.add(option);
// // The newly added option should be selected by default.

// // Exercise 2: Delete Colors
// // Instructions
// {/* <form>
//     <select id="colorSelect">
//         <option>Red</option>
//         <option>Green</option>
//         <option>White</option>
//         <option>Black</option>
//     </select>
//     <input type="button" value="Select and Remove">
// </form> */}

// // Create a function called : removecolor() that removes the selected color from the dropdown list.
// // function removeColor(){
// // let select = document.querySelector("#colorSelect");
// // select.remove(this.value);
// // }
// // let button = document.querySelector("button");
// // button.addEventListener("click", removeColor);
// function colorRemove() {
//     let select = document.querySelector("#colorSelect");
//     select.remove(select.selectedIndex);
// }

// let btn = document.querySelector("#button");
// btn.addEventListener("click",colorRemove);

// Exercise 3 : Create A Shopping List
// Instructions
// For this exercise, you need to work on your js file.
// The one and only element on your HTML file should be:

// <div id="root"></div>
// In your js file:
// Create an empty array. For example: let shoppingList=[].
let shoppingList = [];
// Create a form containing : a text input field and an “AddItem” button. Add this form to the DOM.
let form = document.createElement("form");

let textInput = document.createElement("input"); //input element, text
textInput.setAttribute('type',"text");
textInput.setAttribute('name',"username");

let button = document.createElement("button"); //input element, Submit button
button.innerHTML = "Add Item";

form.appendChild(textInput);
form.appendChild(button);

let root = document.querySelector("#root");
root.appendChild(form);

let h1 = document.createElement("h1");
h1.innerHTML = "Shopping List";
root.appendChild(h1)

let list = document.createElement("div");
root.appendChild(list);
// Type what you need to buy in the text input field, then add the new item to the array as soon as you click on the “AddItem” button (Hint: create a function named addItem()).
function addItem(e){
    e.preventDefault();
    let t=textInput.value
    shoppingList.push(t)
    list.innerHTML += t + "<br />";
}
form.addEventListener("submit", addItem);

// Add a “ClearAll” button to the DOM, that when clicked on, should call the clearAll() function (see below).
// Create a function named clearAll() that should clear out all the items in the shopping list.
let buttonClr = document.createElement("button"); //input element, Submit button
buttonClr.style.marginTop = "50px"
buttonClr.innerHTML = "Clear List";
root.appendChild(buttonClr);

function clearAll(){
    shoppingList = [];
    list.innerHTML = "";
}
buttonClr.addEventListener("click",clearAll);

