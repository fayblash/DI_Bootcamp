function addTask(e){
    e.preventDefault(); 
    inputTask.innerHTML="";
    let newTask = document.createElement("div");
    newTask.setAttribute("class","newTask");
    let xBtn = document.createElement("i");
    xBtn.setAttribute("class","far fa-window-close xBtn");
    newTask.appendChild(xBtn);
    let checkBox = document.createElement("input");
    checkBox.setAttribute("type","checkbox");
    checkBox.setAttribute("class","checkbox");
    newTask.appendChild(checkBox);
    let task = document.createElement("div");
    task.setAttribute("class","task");
    task.innerHTML = inputTask.value;
    taskArr.push(task.innerHTML);
    console.log(taskArr);
    newTask.appendChild(task);
    listTasks.appendChild(newTask);
    //crosses of task when completed
    checkBox.addEventListener("change", function() {
        let next = this.nextSibling;
        if(this.checked) {
        next.style.color="red";
        next.style.textDecoration="line-through";}
        else{
            next.style.color="black";
            next.style.textDecoration="none";}   
        });
    xBtn.addEventListener("click", function(e){
        //removes value from array
        let x=this.nextSibling.nextSibling.innerHTML;
        taskArr = taskArr.filter(item => item !== x)
        //removes task from list
        this.parentNode.parentNode.removeChild(this.parentNode)});
    inputTask.value="";
}
let inputForm = document.querySelector("#inputForm");
let inputTask = document.querySelector("#inputTask");
let listTasks = document.querySelector("#listTasks");
let taskArr =[];

inputForm.addEventListener("submit", addTask);
