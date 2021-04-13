const numbers = [5,0,9,1,7,4,2,6,3,8];

// Using the .toString() method convert the array to a string.
let numString = numbers.toString();
// Using the .join()method convert the array to a string. Try passing different values into the join.
// let joinString = numbers.join("");
// let joinString = numbers.join("+");
let joinString = numbers.join(" ");
// Eg .join(“+”), .join(” “), .join(“”)
// Bonus : To do this Bonus look up how to work with nested for loops
// Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).

for (let i = 0; i < numbers.length; i++){
    let temp = 0;
    if (numbers[i] < numbers[i+1]){
        temp = 
    }
}








// let len = numbers.length;
// for (let i = 0; i < len; i++) {
//     for (let j = 0; j < len; j++) {
//         if (numbers[j] < numbers[j + 1]) {
//             let tmp = numbers[j];
//             numbers[j] = numbers[j + 1];
//             numbers[j + 1] = tmp;
//         }
//     }
// }

// The output should be: [9,8,7,6,5,4,3,2,1,0]
// Hint: The algorithm is called “Bubble Sort”
// Use a temporary variable to swap values in the array.
// Use 2 “nested” for loops (Nested means one inside the other).
// Add comments and console.log the result for each step, this will help you understand.
// Requirement: Don’t copy paste solutions from Google