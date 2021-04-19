// Instructions
// In this exercise we will be creating a webpage with a black background as the universe and we will fill the universe with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.

// Create an array which value is the planets of the solar system.
let arrPlanets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"];
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
let arrColors= ["#FF329F", "#FFFF9F", "#0000FF", "#00CB60", "#FFB52A","#C941EC","#00FFEC", "#1C8027"]
for (let i=0;i<arrPlanets.length;i++){
    let newDiv = document.createElement("DIV");
    newDiv.innerHTML = arrPlanets[i];
    newDiv.className = "planet";
    newDiv.style.backgroundColor = arrColors[i];
    document.querySelector("section").appendChild(newDiv);
}
// Each planet should have a different background color. (Hint: add a new class to each planet).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
let arrMoons = [0,0,1,2,53,53,27,14];

for (let x=0; x<arrPlanets.length;x++){
    let margin = 150;
    for (let y=0;y<arrMoons[x];y++){
        let moonDiv = document.createElement("DIV");
        moonDiv.className = "moon";
        margin+=50;
        moonDiv.style.marginLeft=`${margin}px`;
        document.getElementsByClassName("planet")[x].appendChild(moonDiv);
    }  
}

// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?
// <!DOCTYPE html>
// <html>
//     <head>
//         <meta charset="utf-8">
//         <title>Challenge: Create a solar system</title>
//         <style>
//             body {
//                 background-color: black;
//                 padding: 10px;
//             }
//             .planet {
//                 width: 100px;
//                 height: 100px;
//                 border-radius: 50%;
//                 text-align: center;
//                 padding: 10px;
//                 position: relative;
//             }
//             .moon {
//                 position: absolute;
//                 width: 30px;
//                 height: 30px;
//                 border-radius: 50%;
//                 background: rgb(237, 237, 237);
//             }
//         </style>
//     </head>
//     <body>

//     <section class="listPlanets"></section>

//     <script src="..."></script>
//     </body>
// </html>
