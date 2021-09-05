
let flag = 1;
function changeColor() {
    
    let color1 = document.getElementById("a1");
    let color2 = document.getElementById("a2");
    let color3 = document.getElementById("a3");
    let color4 = document.getElementById("a4");
    let color5 = document.getElementById("a5");

    if(flag){
        color1 = document.getElementById("a1").style.background="rgb(229, 16, 16)";
        color2 = document.getElementById("a2").style.background="rgb(229, 16, 16)";
        color3 = document.getElementById("a3").style.background="rgb(229, 16, 16)";
        color4 = document.getElementById("a4").style.background="rgb(229, 16, 16)";
        color5 = document.getElementById("a5").style.background="rgb(229, 16, 16)";
        flag=0;
    }else{
        color1 = document.getElementById("a1").style.background="rgba(18, 18, 119, 0.897)";
        color2 = document.getElementById("a2").style.background="rgba(18, 18, 119, 0.897)";
        color3 = document.getElementById("a3").style.background="rgba(18, 18, 119, 0.897)";
        color4 = document.getElementById("a4").style.background="rgba(18, 18, 119, 0.897)";
        color5 = document.getElementById("a5").style.background="rgba(18, 18, 119, 0.897)";
        flag=1;
    }    

        
        
    }    

    






