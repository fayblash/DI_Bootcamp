// Exercise 1 : My Book List
// Instructions
// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty div:
// <div class="listBooks"></div>
// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :

// let book1={title:"A Tree Grows in Brooklyn", author:"Betty Smith", image:"url", alreadyRead:true};
// let book2={title:"Pride and Prejudice", author:"Jane Austin", image:"url", alreadyRead:true};
// let allBooks=[book1,book2];

let allBooks = [{title:"A Tree Grows in Brooklyn", author:"Betty Smith", image:"url", alreadyRead:true},
        {title:"Pride and Prejudice", author:"Jane Austin", image:"url", alreadyRead:true}
]
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
let bookTable = document.createElement("table");
document.querySelector(".listBooks").appendChild(bookTable);

// function generateTableHead(table, data) {
//     let thead = table.createTHead();
//     let row = thead.insertRow();
//     for (let key of data) {
//       let th = document.createElement("th");
//       th.innerHTML= key;
//       row.appendChild(th);
//     }
//   }
let bookKeys = Object.keys(allBooks[0]);

let thead = bookTable.createTHead();
let row = thead.insertRow();
for (let key of bookKeys) {
      let th = document.createElement("th");
      th.innerHTML= key;
      row.appendChild(th);
}

for (let element of allBooks) {
    let row = bookTable.insertRow();
    for (key in element) {
        let cell = row.insertCell();
        cell.innerHTML=element[key];
    }
}


// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.


// Exercise 2 : Red Table
// Instructions
// <!DOCTYPE HTML>
// <html>
// <head>
//   <style>
//     table {
//       border-collapse: collapse;
//     }
//     td {
//       border: 1px solid black;
//       padding: 3px 5px;
//     }
//   </style>
// </head>

// <body>
//   <table>
//     <tr>
//       <td>1:1</td>
//       <td>2:1</td>
//       <td>3:1</td>
//       <td>4:1</td>
//       <td>5:1</td>
//     </tr>
//     <tr>
//       <td>1:2</td>
//       <td>2:2</td>
//       <td>3:2</td>
//       <td>4:2</td>
//       <td>5:2</td>
//     </tr>
//     <tr>
//       <td>1:3</td>
//       <td>2:3</td>
//       <td>3:3</td>
//       <td>4:3</td>
//       <td>5:3</td>
//     </tr>
//     <tr>
//       <td>1:4</td>
//       <td>2:4</td>
//       <td>3:4</td>
//       <td>4:4</td>
//       <td>5:4</td>
//     </tr>
//     <tr>
//       <td>1:5</td>
//       <td>2:5</td>
//       <td>3:5</td>
//       <td>4:5</td>
//       <td>5:5</td>
//     </tr>
//   </table>
//   <script>
//     let table = document.body.firstElementChild;
//     // your code
//   </script>
// </body>
// </html>


// Copy the code above and write some Javascript code to color all diagonal table cells in red.
// let table = document.body.firstElementChild;
// let count = table.children[0].childElementCount;
// for(let i=0;i<count;i++){
//     table.firstElementChild.children[i].children[i].style.backgroundColor = "red";
//     table.firstElementChild.children[i].children[count-i-1].style.backgroundColor = "red";
// }