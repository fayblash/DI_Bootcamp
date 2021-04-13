// Exercise 1 : Building Management
// Instructions
let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}
// Console.log the number of levels in the building.
console.log(building.number_levels);
// Console.log how many apartments are on levels 1 and 3.
console.log(building.number_of_apt_by_level[1], building.number_of_apt_by_level[3] );
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(building.name_of_tenants[1], building.number_of_rooms_and_rent.Dan[0]);
// Check if the sum of Sarah and David’s rent is bigger than Dan’s rent.
// If it is than increase Dan’s rent.
if ((building.number_of_rooms_and_rent.Sarah[1] + building.number_of_rooms_and_rent.David[1]) > building.number_of_rooms_and_rent.Dan[1]){
    building.number_of_rooms_and_rent.Dan[1] += 100;
}

// Exercise 2 : Divisible By Three
// Instructions
let numbers = [123, 8409, 100053, 333333333, 7];
// Loop through the array above and determine whether or not each number is divisible by three.

let x;
for (x of numbers){
    if (x%3 === 0){
        console.log("true");
    }
    else{
        console.log("false");
    }
}


// Exercise 3 : Playing With Numbers
// Instructions
let age = [20,5,12,43,98,55];
// Requirements : Don’t use built-in Javascript methods to answer the following questions. You have to create the logic by yourself. Use simple for and while loops.
// 1. Console.log the sum of all the numbers in the age array.
let sum=0;
for (let x in age){
    sum += age[x];
}
console.log(sum);
// 2. Console.log the largest age in the array.
let largest=0;
for (let x in age){
    if(age[x] > largest){
        largest = age[x];
    }
}
console.log(largest);

