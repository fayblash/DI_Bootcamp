// // Exercise 1 : Age Difference
// // Instruction
// // Given the years two people were born, find the date when the younger one is exactly half the age of the older.
// // Notes: The dates are given in the format YYYY
// let dob1 = +prompt("What year was Person1 born? (YYYY)");
// let dob2 = +prompt("What year was Person2 born? (YYYY)");

// if (dob1 > dob2){
//     let diff = dob1 - dob2;
//     let year = dob1 + diff;
//     console.log(`In ${year} Person1 will be ${year-dob1} years old, which is half the age of Person2 (who will be ${year-dob2} years old).`)
// }
// else if (dob2 > dob1){
//     let diff = dob2 - dob1;
//     let year = dob2 + diff
//     console.log(`In ${year} Person2 will be ${year-dob2} years old, which is half the age of Person1 (who will be ${year-dob1} years old).`)
//     // console.log(`Person2 will be half the age of Person1 in the year ${dob2+diff}`)
// }
// else if (dob1 === dob2){
//     console.log("Person1 and Person2 are the same age.");
// }
// else{
//     console.log("You entered invalid data.");
// }


// Exercise 2 : Zip Codes
// Instruction
// Harder exercise
// Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

// While working in a Post Office you must have the clients’ zip code in order to send them their letters.
// Ask the client for their zip code and console.log “success” or “error” based on the following rules.
let zip = prompt("Enter your ZIP code: ");

function isNumeric(s) {
    return !isNaN(s);
}

function hasWhiteSpace(s) {
    return s.indexOf(' ') >= 0;
  }


function hasPeriod(s) {
    return s.indexOf('.') >= 0;
  }


if ((zip.length === 5) && (isNumeric(zip) === true) && (hasWhiteSpace(zip)===false) && (hasPeriod(zip)===false)){
    alert("success");
}
else{
    alert("error");
}
// Zip codes consists of 5 numbers
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length

// part 2 reg ex

// function hasWhiteSpace(s) {
//     return /\s/g.test(s);
//   }


// function isNumeric(s){
//     return /^\d+$/;
// }


// Exercise 3 : Secret Word
// Instruction
// Harder exercise
// Hint : Use Regular Expressions

// Prompt the user for a word and save it to a variable.
// let word = prompt("Enter a word: ");
// // Delete all the vowels of the word and console.log the result.
// function disemvowel(string) {

//     let vowels = {
//       'a': true,
//       'e': true,
//       'i': true,
//       'o': true,
//       'u': true
//     };
  
//     let result = "";
  
//     for (let i = 0; i < string.length; i++) {
//       let letter = string[i].toLowerCase();
//       if (!vowels[letter]) {
//         result += string[i];
//       }
//     };
//     return result;
//   };

//   alert(disemvowel(word));
// // Bonus: Replace the vowels with another character and console.log the result
// function changeVowel(string) {

//     let vowels = {
//       'a': 1,
//       'e': 2,
//       'i': 3,
//       'o': 4,
//       'u': 5
//     };
  
//     let result = "";
  
//     for (let i = 0; i < string.length; i++) {
//       let letter = string[i].toLowerCase();
//       if (!vowels[letter]) {
//         result += string[i];
//       }
//       else{
//           result += vowels[letter]
//       }
//     };
//     return result;
//   };
//   alert(changeVowel(word));
// // a = 1
// // e = 2
// // i = 3
// // o = 4
// // u = 5
