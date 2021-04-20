// Instructions
// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank inputs with different word types (ie : noun, adjective, verb), and then a story is generated based on the words you chose, and sometimes the story is surprisingly funny.
// In this exercise you will complete the functionality with event listeners.

// Follow these steps :
// Get the value of each of the inputs in the HTML file when the button is clicked.
// Make sure the values are not empty
let noun = document.querySelector("#noun");
        let adjective = document.querySelector("#adjective");
        let person = document.querySelector("#person");
        let verb = document.querySelector("#verb");
        let place = document.querySelector("#place");
        let story = document.querySelector("#story");
        let button = document.querySelector("#lib-button");

        button.addEventListener("click",makeStory);

        function makeStory(){
            if (noun.value === "" || adjective.value ==="" || person.value ==="" || verb.value ==="" || place.value===""){
                alert("You did not enter all the values");
                return;
            } 
            else{
                let blankStory = `Once upon a time there was a ${adjective.value} ${noun.value} who wanted to ${verb.value} with ${person.value} in ${place.value}.`;
                document.querySelector("#story").innerHTML = blankStory;
            }
        }

// Write a story that uses each of the values.

// Make sure you check the console for errors when playing the game.

// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.