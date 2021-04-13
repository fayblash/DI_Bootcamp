// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).
// Do this Daily Challenge by youself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

//First method
for (let i = 1; i < 7; i++){
    console.log("*".repeat(i));
}

// Second Method
for (let i=1; i<7; i++){
    let stars="";
    for (let x=0; x<i; x++)
    {  
        stars += "* "   
    }
    console.log(stars);
} 