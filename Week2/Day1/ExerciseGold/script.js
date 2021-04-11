// Exercise 1: Favorite Color
let me = ["my","favorite","color","is","blue"]
console.log(me.join());

// Exercise2: Mixup
let str1="Ashira"
let str2="Blashka"
str1New = str2.slice(0,2) + str1.slice(2);
str2New = str1.slice(0,2) + str2.slice(2);
console.log(str1New + " " + str2New);


// Exercise 3: Calculator

let num1= prompt('Enter your first number: ');
let num2= prompt('Enter your second number: ');
let Sum= Number(num1) + Number(num2);
let Difference = Number(num1) - Number(num2);
let Product = Number(num1) * Number(num2);
let Quotient = Number(num1) / Number(num2);
alert(`Sum = ${Sum}`);
alert(`Difference = ${Difference}`);
alert(`Product = ${Product}`);
alert(`Quotient = ${Quotient}`);
