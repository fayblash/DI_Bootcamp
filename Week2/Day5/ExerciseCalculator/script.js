function display(input){
    document.getElementById("result").value+=input;
}
  
function solve(){
    let x = eval(document.getElementById("result").value);
    document.getElementById("result").value = x;
}
  
function reset(){
    document.getElementById("result").value = "";
}

function back(){
    let sliced = document.getElementById("result").value.slice(0,-1);
    document.getElementById("result").value = sliced;
}