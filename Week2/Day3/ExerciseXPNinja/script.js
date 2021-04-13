// Exercise 1 : Checking The BMI
// Instructions
// Create two objects, each object should hold a persons details. Here are the details:
// FullName
// Mass
// Height
// Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person
// Outside of the objects, create a JS function that compares the BMI of both objects.
// Display the name of the person who has the largest BMI.

var Person1 = {
    FullName: "Fay",
    Weight: 60,
    Height: 1.65,
    BMI: function BMICalc(){
            let bmi = this.Weight/(this.Height**2);
            return bmi;
    }
};

var Person2 = {
    FullName: "Dina",
    Weight: 55,
    Height: 1.58,
    BMI: function BMICalc(){
        let bmi = this.Weight/(this.Height**2);
        return bmi;
    }
};

function higherBMI(bmi1, bmi2){
    if (bmi1 > bmi2){
        return bmi1;
    }
    else if (bmi < bmi2){
        return bmi2;
}
}

let higher = higherBMI(Person1.BMI(),Person2.BMI());

if (Person1.BMI() == higher){
    console.log(`${Person1.FullName} has the higher BMI.`);
}
else{
    console.log(`${Person2.FullName} has the higher BMI.`);  
}


// Exercise 2 : Grade Average
// Instructions
// Hint:
// - This Exercise is trickier then the others. You have to think about its structure before you start coding.
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.
function findAvg(gradesList){
    let total = 0;
    for (let i = 0; i < gradesList.length; i++){
        total += gradesList[i];
    }
    let avg = total / gradesList.length;
    console.log(avg);
    if (avg > 65){
        console.log("You passed.");
    }
    else{
        console.log("You failed.");
    }
}

let historyGrades=[69, 99, 66, 85];
findAvg(historyGrades);



// Create a function called findAvg(gradesList) that takes an argument called gradesList.
// Your function must calculate and console.log the average.
// If the average is above 65 let the user know they passed
// If the average is below 65 let the user know they failed and must repeat the course.
// Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
// Hint One function must call the other.
function findAvg(gradesList){
    let total = 0;
    for (let i = 0; i < gradesList.length; i++){
        total += gradesList[i];
    }
    let avg = total / gradesList.length;
    console.log(avg);
    return avg;
}

let historyGrades=[69, 99, 66, 85];
// findAvg(historyGrades);

function Passed(avg){
if  (avg > 65){
    console.log("You passed.");
}
else{
    console.log("You failed.");
}
}
Passed(findAvg(historyGrades));


