function printA(){
    let starA="";
    for (let i=0;i<7;i++){
        for (let j=0;j<5;j++){
            if (i===0){
                if (j===0||j===4){
                  starA+= " ";   
                }
                else{
                    starA+="*";
                }   
            }
            else if (i===3){
                starA+="*"
            }
            else{
                if (j===0||j===4){
                    starA+="*";
                }
                else{
                    starA+=" ";
                }  
            }     
        }  
        starA+="\n";     
    }   
    console.log(starA);
}
printA();