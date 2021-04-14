// // Exercise 1 : Keyless Car
// // Instructions
// // Ask the user for their age, and save the value to a variable.
// let userAge = +prompt("Enter your age: ");
// // Create a function called checkDriverAge() that will notify the user if they are permitted to drive. They must be at least 18 to drive.
// function checkDriverAge(age){
//     if (age < 18){
//         alert('Sorry, you are too young to drive this car. Powering off');
//     }
//     else if (age >= 18){
//         alert('You are old enough to drive, Powering On. Enjoy the ride!');
//         if(age=== 18){
//             alert('Congratulations on your first year of driving. Enjoy the ride!');
//         }
//     }
// }

// checkDriverAge(userAge);

// // if the user is too young, alert “Sorry, you are too young to drive this car. Powering off”
// // if the user is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// // if the user just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// // Instead of using prompt to ask the user for their age, have the checkDriverAge() function accept an argument age.


// Exercise 2 : What’s In My Wallet ?
// Instructions
// Given a item price and an array representing the amount of change in your pocket, determine whether or not you can afford the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
let coinValue = [0.25, 0.10, 0.05, 0.01];
// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01
function changeEnough(pocket, price){
let i, totalChange = 0;
for (i=0; i<pocket.length;i++) {
    totalChange += (pocket[i]*coinValue[i]);
}
if (totalChange >= price){
    console.log("You have enough change to buy your item.");
}
else{console.log("You don't have enough change to buy your item.");}
}
changeEnough([25, 20, 5, 0], 6.25);
changeEnough([2, 100, 0, 0], 14.11);
// To illustrate:
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// Examples

// changeEnough([2, 100, 0, 0], 14.11) ➞ false
// changeEnough([0, 0, 20, 5], 0.75) ➞ true


// // Exercise 3: Find The Multiples Of 23
// // Instructions
// // Write a js function that console.logs all multiples of 23 less than 500, at the end return the sum of all the multiples.

////I adjusted it to accept a parameter to multiply by, so this works not just for 23 
//function Multiples(x){
// let sum=0, i=0, temp=0;

// while (temp < 500){
//     console.log(temp);
//     sum += temp;
//     temp = i*x 
//     i++;
//   } 
// return sum
// }
// // Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// // 391 414 437 460 483
// // Sum : 5313


// // Exercise 4 : Amazon Shopping
// // Instructions
// var amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// // Create a function called checkBasket().
// // It should:
// // prompt the user for an item
// // let the user know if the item is in the basket
// // Hint: Use the in keyword inside the conditional
// function checkBasket(basket){
//     let item = prompt("Enter the name of an item: ").toLowerCase();
//     // if (basket[item]){
//     if (item in basket){   
//     console.log("Your item is in the basket.");
//     }
//     else{
//         console.log("Your item is not in the basket.");
//     }
// }

// checkBasket(amazonBasket);

// // Exercise 5 : Shopping List
// // Instructions
// var list = ["banana", "orange", "apple"];
// var stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// var prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
// // Add the stock and prices objects to your js file.

// // Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
// // Create a function called myBill() that takes no arguments.
// function myBill(){
//     let total = 0;
//     for (item of list){
//         if(stock[item]>1){
//             total+=prices[item];
//             stock[item]-=1;//bonus
//         } 
//     }
//     console.log(total);
// }
// myBill();

// // The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// // The item must be in stock.
// // If the item is in stock find out the price in the prices object.
// // Call the myBill() function.
// // Bonus: If the item is in stock, decrease the item’s stock by 1


// // Exercise 6 : Tips
// // Instructions
// // John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// // The calculator has the following rules:
// // 1. Tip 20% when the bill is less than $50,
// // 2. Tip 15% when the bill is between $50 and $200,
// // 3. Tip 10% if the bill is more than $200.
// let bill = +prompt("How much was your bill? ");
// // Ask John for the amount of the bill.
// // Create the program explained above.
// function calcTip(bill){
//     let tip = 0;
//     if (bill > 200){
//         tip = 0.1*bill;
//     }
//     else if (bill >= 50 ){
//         tip = 0.15*bill;
//     }
//     else if (bill < 50)
//         {
//             tip = 0.2*bill;
//     }
//     else{
//         console.log("You entered invalid data");
//         return;
//     }
//     console.log(`Your tip was ${tip}.`)
//     console.log(`Your total bill was ${bill+tip}.`);
//     return;
// }
// calcTip(bill);
// // In the end, John would like to know:
// // Tip amount.
// // Final bill (bill + tip).
// // (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)


// // Exercise 7 : Vacations Costs
// // Instructions
// // Let’s create functions that calculate your vacation’s costs:

// // Define a function called hotel_cost().
// // It should ask the user for the number of nights they would like to stay in the hotel.
// // If the user doesn’t answer or if the answer is not a number, ask again.
// // The hotel costs $140 per night. The function should return the total price of the hotel.
// function hotel_cost(){

//     do {var nights = +prompt("How many nights would you like to stay? ")}
//     while (nights <=0 || isNaN(nights));

//     return (140*nights);
// }
// // Define a function called plane_ride_cost().
// // It should ask the user for their destination.
// // The function should return a different price depending on the location.
// // “London”: 183$
// // “Paris” : 220$
// // All other destination : 300$
// // If the user doesn’t answer or if the answer is not a string, ask again.
// function plane_ride_cost(){
//     do{var destination = prompt("Where would you like to go? ").toLowerCase();}
//     while (!isNaN((parseInt(destination))) || destination === "");

//     if (destination === "london"){
//         return 183;
//     }
//     else if (destination === "paris"){
//         return 220;
//     }
//     else{
//         return 300;
//     }
// }
// // Define a function called rental_car_cost().
// // It should ask the user for the number of days they would like to rent the car.
// // If the user doesn’t answer or if the answer is not a number, ask again.
// // Calculate the cost to rent the car. The car costs $40 everyday.
// // If the user rents a car for more than 10 days, they get a 5% discount.
// // The function should return the total price of the car rental.
// function rental_car_cost(){
//     do {var days = +prompt("How many days would you like to rent a car? ");}
//     while (days <=0 || isNaN(days));
//     console.log(days);
//     console.log(typeof days);

//     if (days>10){
//         return (0.95*(days *40));
//     }
//     else{
//         return (days*40);
//     }
// }
// // Define a function called total_vacation_cost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// // Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// // Hint: You have to call the functions hotel_cost(), plane_ride_cost() and rental_car_cost() inside the function total_vacation_cost.
// // Call the function total_vacation_cost()
// function total_vacation_cost(hotel, flight, car){
//     console.log(`The hotel costs $${hotel}.`)
//     console.log(`The flight costs $${flight}.`)
//     console.log(`The car rental costs $${car}.`)
//     console.log(`Your total cost is : $${hotel + flight+ car}`);
// }
// total_vacation_cost(hotel_cost(),plane_ride_cost(),rental_car_cost());

// // Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the total_vacation_cost() function.
