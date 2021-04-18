// Create the “Hangman” game. Your game will run in the console.
// You need to guess a hidden word. Each letter you guess will appear in the console. You have 10 chances before you lose the game.

// Check it out here

// Prompt player 1 for a word. The word must have a minimum of 8 letters. Present the word in the console with stars (********).
// At this point continuously prompt player 2 for a letter.
// If the letter is in the word chosen by player 1, display the word in stars again but with the correct letter (*****t**).
// If the letter appears in the word multiple times, make sure it is seen in all the correct places when showing the stars with the correct guesses (***t**t*).
// If player 2 guesses incorrectly 10 times display a message in the console saying YOU LOSE.
// Show a list of all the guesses after each turn. In your code prevent player 2 from guessing the same letter twice.
// If player 1 wins, display a message that says CONGRATS YOU WIN.

//function to check for all occurrences of letter in word 
function getAllIndexes(arr, val) {
    var indexes = [], i;
    for(i = 0; i < arr.length; i++)
        if (arr[i] === val)
            indexes.push(i);
    return indexes;
}

function hangMan(){
    //prompt for word 8 at least 8 letters
    do{
        var userWord = prompt("Player1: Enter a word (min 8 letters): ");
    }while(userWord.length<8 || userWord === "");
    //create array of word
    let arrWord=userWord.split("");
    //create corresponding array for stars/results
    let arrHangman=[];
    for (let i=0; i<arrWord.length;i++){
        arrHangman[i] = "*";
    }
    //counter gives you 10 chances
    let counter=0;
    //checks how many stars were replaced with letters
    let winCount=0;
    //array of letters guessed already
    let used = [];
    
    while(counter<10){
        let letter = prompt("Player2: Enter a letter").toLowerCase();
        // In your code prevent player 2 from guessing the same letter twice.
        if(used.includes(letter)){
            console.log("You used that letter already. Guess again")
        }
        else{
            //if guess is in word
            if (arrWord.includes(letter)){
                //replaces all indices of letter
                let tempArr= getAllIndexes(arrWord, letter);
                for (let f=0;f<tempArr.length;f++){
                    arrHangman[tempArr[f]]=letter;
                    winCount++;   
                }
                used.push(letter);
                console.log("Good guess!");
                console.log(arrHangman);
                console.log(`You used these letters: ${used}`);
                
                //checks if you solved the whole word
                if (winCount === arrWord.length){
                    console.log(`Congrats! You win! The word was ${userWord}`);
                    return true;
                }
            }else{
                //guess is not in word, reprompt
                used.push(letter);
                console.log("Nope. Try again")
                console.log(`You used these letters: ${used}`);
                counter++;
                console.log(`You used ${counter} out of 10 chances`);
            }
        }
    }

    console.log(`You lose. The word was ${userWord}`);
    return false;
}

hangMan();



