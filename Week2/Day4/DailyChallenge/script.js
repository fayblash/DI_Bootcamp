// Instructions
// Prompt the user for several words (separated by commas).
// Put the words into an array.
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.
// For example, if the user gives you:
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:
function starMaker(){
let userInput = prompt("Please enter several words separated by commas (no spaces): ");
let arrInput = userInput.split(','); 
//checking for length of longest word
let strLongest = 0;
for (item of arrInput){
    if (item.length>strLongest){
        strLongest = item.length;
    }
}
//print star box
console.log("*".repeat(strLongest+4));
for (let i=0; i<arrInput.length;i++){
    console.log("* " + arrInput[i] + " ".repeat(strLongest-arrInput[i].length) + " *");
}
console.log("*".repeat(strLongest+4));
}

starMaker();