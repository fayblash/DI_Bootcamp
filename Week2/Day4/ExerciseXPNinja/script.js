// // Exercise 1: Random Number
// // Instructions
// // Get a random number between 1 and 100.
// // Console.log all even numbers from 0 to the random number.
// function evenToRandom(){

// let randInt = Math.floor(Math.random() * 100) +1;
// // console.log(randInt);
// for (let i=0; i < randInt; i++){
//     if(i%2 === 0){
//         console.log(i);
//     }
// }
// }

// evenToRandom();

// // Exercise 2: Capitalized Letters
// // Instructions
// // Create a function that takes a string as an argument.
// function  capEven(string){
//     let swap1 = ""; //ULUL
//     let swap2 = ""; //LULU
//     for (let i=0;i<string.length;i++){
//         //even index
//         if (i%2===0){
//             if(string[i] === string[i].toLowerCase()){//If L
//                 swap1+= string[i].toUpperCase();//U
//                 swap2+= string[i];//L
//             }
//             else{//If U
//                 swap1+= string[i];//U
//                 swap2+= string[i].toLowerCase();//L
//             }
//         }
//         //odd index
//         else{
//             if(string[i] === string[i].toLowerCase()){//If L
//                 swap1+= string[i];//L
//                 swap2+= string[i].toUpperCase();//U
//             }
//             else{//If U
//                 swap1+= string[i].toLowerCase();//L
//                 swap2+= string[i];//U
//             }
//         }
//     }
//     console.log(swap1, swap2);
// }
// capEven("abcdef");

// // Have the function return
// // The string but all letters in even indexes should be capitalized.
// // The string but all letters in odd indexes should be capitalized.
// // Note:
// // Index 0 will be considered even.
// // The argument of the function should be a lowercase string with no spaces.
// // For example,

// // capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']


// Exercise 3 : Is Palindrome?
// Instructions
// Write a JavaScript function that checks whether a string is a palindrome or not.
// Note A palindrome is a word, phrase or sequence that is spelled the same both backwards and forward, e.g., madam, bob or kayak.
// palindrome
function Palindrome(){
    let string = prompt("Enter a word or phrase and I'll tell you if it's a palindrome: ");
    string=string.toLowerCase().replace(/[^a-zA-Z]/g, '');
   
    for (let i = 0; i < string.length; i++){
        if (string[i] === string[(string.length-1)-i]){
        }
        else{
            console.log("Not a palindrome.");
            return;
        }
    }
    console.log("It's a palindrome!");
    return;
}
Palindrome();

// // Exercise 4 : Biggest Number
// // Instructions
// // Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
// // Note : This function should work with any array;
// // Example:
// function biggestNum(array){
//     let biggest=0;
//     for (num of array){
//         if (num > biggest){
//             biggest = num;
//         }
//     }
//     console.log(biggest);
// }
// const array = [-1,0,3,100, 99, 2, 99] ;// should return 100 
// const array2 = ['a', 3, 4, 2]; // should return 4 
// const array3 = []; // should return 0
// biggestNum(array);
// biggestNum(array2);
// biggestNum(array3);

// // Exercise 5: Unique Elements
// // Instructions
// // Write a JS function that takes an array and returns a new array with only unique elements.
// function uniqueArr(array){
//     let newArray = [];
//     for (let i = 0; i < array.length; i++){
//         if (newArray.includes(array[i]) === false){
//             newArray.push(array[i]);
//         }
//     }
//     console.log(newArray);
// }
// // Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
// // Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
// uniqueArr([1,2,3,3,3,3,4,5]);
// uniqueArr([1,2,7,3,5,3,4,4,5]);