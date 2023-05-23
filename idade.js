
var idade = document.querySelector("#idade").value;
var ano = document.querySelector("#ano").value;
var x =  (ano - idade)
function recarregarAPagina(){
    window.location.reload();
} 

document.write("Voce nasceu em ", x)