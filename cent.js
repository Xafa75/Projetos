var metros = document.querySelector("#metro").value;
var centimetros = (metros * 100);

function recarregarAPagina(){
    window.location.reload();
}
document.write(centimetros, "cm");