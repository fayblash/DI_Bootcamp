//Exercise 1 World Translator

// Ask the user which language they speak.
let lang = prompt("What language do you speak? ")

// Convert the user’s answer to lowercase, so that all the user’s inputs will be accepted in the if statement. For example “english” or “English” or “ENGlish” ect…”
lang = lang.toLowerCase();
// Create a few conditions :
switch (lang) {
            case "french":
                alert("Bonjour");
                break;
            case "english":
                alert("Hello");
                break;
            case "hebrew":
                alert("Shalom");
                break;
            default:
                alert("01110011 01101111 01110010 01110010 01111001");      
            }
    
// If the user speaks French : display “Bonjour”
// If the user speaks English : display “Hello”
// If the user speaks Hebrew : display “Shalom”
// If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’

// Exercise 2 : The Grade Assigner
// Instructions
// Ask the user for their grade.
let grade = +prompt("Enter your grade: ");

// If the grade is bigger than 90, console.log “A”
if (grade > 90){
    alert("A");
}
// If the grade is between 80 and 90 (included), console.log “B”
else if (grade > 80){
    alert("B")
}
// If the grade is between 70(included) and 80 (included), console.log “C”
else if (grade>=70){
    alert("C");
}
else {
    alert("D");
}
// If the grade is lower than 70, console.log “D”

// Exercise 3 : Verbing

// Prompt the user for a string. It must be a verb.
let verb = prompt("Enter a verb: ");
// If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
if (verb.length>=3 && (verb.substring(verb.length-3) !== "ing")){
    alert(`${verb}ing`);
}
// If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
else if (verb.length>=3 && (verb.substring(verb.length-3) === "ing")){
    alert(`${verb}ly`);
}
// If the length of the string is less than 3, leave it unchanged.
else{
    alert(verb);
}