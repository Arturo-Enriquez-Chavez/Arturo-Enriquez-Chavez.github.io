
let flag = 1;
function changeColor() {
    
    let color1 = document.getElementById("a1");
    let color2 = document.getElementById("a2");
    let color3 = document.getElementById("a3");
    let color4 = document.getElementById("a4");
    let color5 = document.getElementById("a5");
    let color6 = document.getElementById("a6");
    let color7 = document.getElementById("a7");
    let color8 = document.getElementById("a8");

    if(flag){
        color1 = document.getElementById("a1").style.background="rgb(229, 16, 16)";
        color2 = document.getElementById("a2").style.background="rgb(229, 16, 16)";
        color3 = document.getElementById("a3").style.background="rgb(229, 16, 16)";
        color4 = document.getElementById("a4").style.background="rgb(229, 16, 16)";
        color5 = document.getElementById("a5").style.background="rgb(229, 16, 16)";
        color6 = document.getElementById("a6").style.background="rgba(18, 18, 119, 0.897)";
        color7 = document.getElementById("a7").style.background="rgba(18, 18, 119, 0.897)";
        color8 = document.getElementById("a8").style.background="rgba(18, 18, 119, 0.897)";
        flag=0;
    }else{
        color1 = document.getElementById("a1").style.background="rgba(18, 18, 119, 0.897)";
        color2 = document.getElementById("a2").style.background="rgba(18, 18, 119, 0.897)";
        color3 = document.getElementById("a3").style.background="rgba(18, 18, 119, 0.897)";
        color4 = document.getElementById("a4").style.background="rgba(18, 18, 119, 0.897)";
        color5 = document.getElementById("a5").style.background="rgba(18, 18, 119, 0.897)";
        color6 = document.getElementById("a6").style.background="rgb(229, 16, 16)";
        color7 = document.getElementById("a7").style.background="rgb(229, 16, 16)";
        color8 = document.getElementById("a8").style.background="rgb(229, 16, 16)";
        flag=1;
    }    
}    

function extraccion(){
    const nya=document.getElementById("nya").value;

    let i=nya.split(' ');
    document.getElementById("ext_pa").value = i[0];
    document.getElementById("ext_ma").value = i[1];
    document.getElementById("ext_nom").value = i[2]+" "+i[3];

    var union=i[0]+i[1];
    document.getElementById("lap").value =  union.length;

    let fecha=document.getElementById("fecha").value;
    let anio = fecha.split('-');
    
    let edad = 2021 - anio[0];
    let meses = ['Enero', "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
    document.getElementById("edad").value = edad+" años";
    document.getElementById("mesl").value = meses[parseInt(anio[1]-1)];
    
}