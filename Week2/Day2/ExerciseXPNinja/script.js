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

zip = parseInt(zip);
    // Check for white space

// Zip codes consists of 5 numbers
// if (zip.length === 5)
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length
