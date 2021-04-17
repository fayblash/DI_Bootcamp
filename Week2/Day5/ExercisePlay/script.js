function playTheGame(){
    if(confirm("Do you want to play the game?")){
        let userNumber = +prompt("Enter a number between 1-10: ");
        if(userNumber >=1 && userNumber <=10){
            let computerNumber = Math.floor(Math.random() * 10)+1;
            test(userNumber,computerNumber);
        }else if (userNumber <= 0 || userNumber > 10){
            alert("Sorry it's not a good number.");
            playTheGame();
        }else{
            alert("Sorry, it's not a number. Goodbye."); 
            playTheGame();
        }
    } else{
        alert("No problem, Goodbye.");
    }
}
     
function test(userNumber,computerNumber) {
    for (let i=0;i<3;i++){
        if(userNumber === computerNumber){
            alert("Winner!");
            return;
        }else if(userNumber < computerNumber){
            alert("Your number is smaller then the computer's, guess again.");
            userNumber = +prompt("Enter a new number: ");
        }else if(userNumber > computerNumber){
            alert("Your number is larger then the computer’s, guess again.");
            userNumber = +prompt("Enter a new number: ");
        }
        else{
            return;
        }
    }
    alert("Out of chances.");
    return;
}
  