// First attempt - converting string to array to use splice

// let sentence = "This smoothie is not that bad , I like the flavors."

// sentence = sentence.split(" ");

// let wordNot = sentence.indexOf("not");
// let wordBad = sentence.indexOf("bad");


// if (wordNot >= 0 && wordNot < wordBad){

//     sentence.splice(wordNot, (wordBad-wordNot+1), "good");
//     let newSentence =sentence.join(" ");
//     console.log(newSentence);
// }

// else {
//     let newSentence = sentence.join(" ");
//     console.log(newSentence);
// }

//Second attempt - just using string and substrings
let sentence = "This smoothie is bad, I like the flavors."

let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordNot >=0 && wordNot < wordBad){

    console.log(sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad+3));
}
else {
    console.log(sentence);
}