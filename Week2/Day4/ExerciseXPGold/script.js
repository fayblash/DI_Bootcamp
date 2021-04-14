// // Exercise 1 : Is_Blank
// // Instructions
// // Write a program to check whether a string is blank or not.
// function is_Blank(string){
// return (string.length === 0);
// }
// // console.log(is_Blank('')); --> true
// // console.log(is_Blank('abc')); --> false
// console.log(is_Blank("hello"));
// console.log(is_Blank(""));

// // Exercise 2 : Abbrev_name
// // Instructions
// // Write a JavaScript function to convert a string into an abbreviated form.
// function abbrev_name(name){
// let nameArray = name.split(" ");
// return (`${nameArray[0][0]}. ${nameArray[1][0]}.`)
// }

// console.log(abbrev_name("Robin Singh"));


// // Exercise 3 : SwapCase
// // Instructions
// // Write a JavaScript function which takes a string as an argument and swaps the case of each character.
// // For example :
// function swapCase(){
// let userInput = prompt("Enter a sentence: ");
// let swapped = "";
// for (let i=0;i<userInput.length;i++){
//     if (userInput[i] === userInput[i].toLowerCase()){
//         swapped+= userInput[i].toUpperCase();
//     }
//     else{
//         swapped+= userInput[i].toLowerCase();
//     }
// }
// console.log(swapped);
// }
// swapCase();
// // if you input 'The Quick Brown Fox' 
// // the output should be 'tHE qUICK bROWN fOX'.


// // Exercise 4 : Omnipresent Value
// // Instructions
// // Create a function that determines whether an argument is omnipresent for a given array.
// // A value is omnipresent if it exists in every subarray inside the main array.
// // To illustrate:

// // [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// // // 3 exists in every element inside this array, so is omnipresent.
// // Examples
// function isOmnipresent(array,number){
//     for (item of array){
//         if (item.includes(number)){ 
//         }
//         else{
//             return false;
//         }   
//     }
//     return true;
// }
// console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));
// console.log(isOmnipresent([[1, 1, 6], [1, 3], [5, 1, 4], [6, 1]], 6));


