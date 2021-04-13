// //Exercise 1: Favorite Colors
// let colors = ["aqua", "teal", "mint", "seafoam"];

// let i;
// for (i=0; i < colors.length; i++) {
//     console.log(`My #${i+1} choice is ${colors[i].}`)
// }

// //bonus
// let colors = ["aqua", "teal", "mint", "seafoam"];
// let ordinals = ["1st", "2nd", "3rd", "4th"];

// let i;
// for (i=0; i < colors.length; i++) {
//     console.log(`My ${ordinals[i]} choice is ${colors[i].}`)
// }

// //Exercise 2: List of People
// let people = ["Greg", "Mary", "Devon", "James"]
// // Write code to remove “Greg” from the people array.
// people.shift();
// // Write code to replace “James” to “Jason”.
// people.splice(2,1,"Jason");
// // Write code to add your name to the end of the people array.
// people.push("Fay");
// // Using a loop, iterate through the people array and console.log each person.
// let i;
// for (i=0; i< people.length; i++){
//     console.log(people[i]);
// }
// // Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
// let i;
// for (i=0; i< people.length; i++){
//     console.log(people[i]);
//     if (people[i]==="Jason"){
//         break;
//     }
// }
// // Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
// let newPeople = people.slice(1,-1);
// // // Write code that console.logs Mary’s index. take a look at indexOf on google.
// console.log(people.indexOf('Mary'));
// // Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
// console.log(people.indexOf('Foo'));
// // Create a variable called last which value is the last element of the array.
// let last = people[people.length - 1];
// // Hint: What is the relationship between the index of the last element in the array and the length of the array?

// // Exercise 3 : Repeat The Question
// // Instructions
// // Promt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
// // Tip : Which while loop is more relevant for this situation?
// do{
//     var num = +prompt("Enter a number 10 or larger: ")
// }
// while (num<10);

// // Exercise 4 : Attendance
// // Instructions
// let guestList = {
//   randy: "Germany",
//   karla: "France",
//   wendy: "Japan",
//   norman: "England",
//   sam: "Argentina"
// }
// // Given the object above where the key is the students name and the value is the country they are from.
// // 1. Prompt the student for their name :
// let guest = prompt("Please enter your name: ").toLowerCase();
// // * If the name is in the object, console.log the name of the student and the country they come from.
// if (guestList[guest]){
//     console.log(`Hi I'm ${guest} and I'm from ${guestList[guest]}`);
// }
// else{
//     console.log("Hi, I'm a guest.");
// }
// // example: "Hi! I'm [name], and I'm from [country]."
// // * Hint: Look up the statement if ... in
// // * If the name is not in the object, console.log: "Hi! I'm a guest."

// // Exercise 5 : Family
// // Instructions
// // Create an object called family with a few key value pairs.
// let family = {
//     mom:"Fay", child1:"Elisheva", child2:"Ezra", child3:"Elazar", child4:"Noam", child5:"Tali", child6:"Nava"
// }
// // Console.log the keys. (using a for loop).
// for (let x in family){
//     console.log(x);
// }
// // Console.log the values. (using a for loop).
// for (let x in family){
//     console.log(family[x]);
// }

// // Exercise 6
// Instructions
// let details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }

// // Given the object above, console.log “my name is Rudolf the raindeer”
// let x, str = "";
// for (x in details){
//     str = str + " " + x + " " + details[x];
// }
// console.log(str);

// // Exercise 7 : Secret Group
// // Instructions
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// // A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// names = names.sort();
// let society = "";
// for (x of names){
//     society += x[0];
// }
// console.log(`The name of the secret society is ${society}.`);
// // Hint: a string is an array of letters
// // Console.log the name of their secret society.




