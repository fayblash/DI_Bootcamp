let startNum = +prompt("Enter a number from 1-99 to start the song:");
let dropNum = startNum;
for (i=1; i<=dropNum; i++){
console.log(`${dropNum} bottles of beer on the wall`);
console.log(`${dropNum} bottles of beer`);
    if(i===1){
        console.log(`Take ${i} down, pass it around`);
    }
    else{
        console.log(`Take ${i} down, pass them around`);   
    }
dropNum-=i;
console.log(`${dropNum} bottles of beer on the wall`);
}
console.log("Drink up!");
