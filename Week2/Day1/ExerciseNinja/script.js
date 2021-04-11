// Exercise 1: Nemo
let strNemo = prompt('Enter a sentence that contains "Nemo": ');
let arrNemo = strNemo.split(" ");
let loc = arrNemo.indexOf("nemo");
if (loc >= 0) {
    console.log(`I found nemo at ${loc}`)
}
else {
    console.log("I can't find Nemo.")
}

// Exercise 1: Evaluation
5 >= 1 //true
0 === 1 //false
4 <= 1 //false
1 != 1 //false
"A" > "B" //false
"B" < "C" //true
"a" > "A" //true
"b" < "A" //false
true === false //false
true != true //false

//Exercise 2: Evaluation (2)
let c;
let a = 34;
let b = 21;
a = 2;
a + b

What will be the outcome of a + b? //23
What is the value of c? //undefined
Analyse the code below what will be the outcome?
console.log(3 + 4 + '5'); //75 (3+4) concatenated with '5'

// //Exercise 3: Ask for numbers
 let arrNum = prompt("Enter a series of numbers separated by commas (ex. 3,6,9,13): ").split(","); 
 arrNum = arrNum.map(Number);
 let i, arrSum=0;
for (i = 0; i < arrNum.length; i++) {
  arrSum += arrNum[i];
}
console.log(arrSum);

// Exercise 4: Boom
let numBoom = +prompt("Enter a number: ");
if (numBoom <2) {
   console.log("boom");
} 
else if (numBoom%2===0 && numBoom%5===0){
    console.log("B" + "O".repeat(numBoom) +"M!");
}
else if (numBoom%2===0){
    console.log("b" + "o".repeat(numBoom) +"m!");
}
else if (numBoom%5===0){
    console.log("B" + "O".repeat(numBoom) +"M");
}
else {
    console.log("b" + "o".repeat(numBoom) +"m");
}