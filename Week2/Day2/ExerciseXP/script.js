//Exercise 1
let x = 15;
let y = 21;

if (x > y) {
alert("x is the bigger number");
}
else if  (x < y) {
    alert("y is the bigger number");
}
else{
    alert("x and y are equal");
}

//Exercise 2
let newDog = prompt("Enter the breed of your dog: ");

//check and display length
console.log(newDog.length);

//convert and print upp and lower
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

//if else statment
if (newDog === "Chihuahua"){
    alert("I love Chihuahuas, it's my favorite dog breed.");
}
else{
    alert("I love Chihuahuas, it's my favorite dog breed.");
}

//Exercise 3
let num = +prompt("Please enter a number: ");

if (num%2 == 0){
    alert(`${num} is an even number.`)
}
else{
    alert(`${num} is an odd number`)
}

//Exercise 4
// Using this function, answer the questions below:

// function moveCommand(direction) {
//     var whatHappens;
//     switch (direction) {
//         case "forward":
//             break;
//             whatHappens = "you encounter a monster";
//         case "back":
//             whatHappens = "you arrived home";
//             break;
//             break;
//         case "right":
//             return whatHappens = "you found a river";
//             break;
//         case "left":
//             break;
//             whatHappens = "you run into a troll";
//             break;
//         default:
//             whatHappens = "please enter a valid direction";
//     }
//     return whatHappens;
// }
// What is the returned value when moveCommand("forward") "you encounter a monster"

// What is the returned value when moveCommand("back") "you arrived home"

// What is the returned value when moveCommand("right") "you found a river"

// What is the returned value when moveCommand("left") "you run into a troll"

//Exercise 5
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

if (users.length === 0){
    alert("no one is online");
    
}
else if (users.length === 1){
    alert(`${users[0]} is online`);
}
else if (users.length === 2){
    alert(`${users[0]} and ${users[1]} are online`);
}
else {
    alert(`${users[0]} and ${users[1]} and ${users.length - 2} more are online`);
}