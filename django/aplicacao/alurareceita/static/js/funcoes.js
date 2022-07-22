console.log('FOI');
function verificaCheck(){
    var checkbox = document.querySelector("input[name=publicada]");
    if(checkbox.checked){
        checkbox.value = "True";
        console.log("O cliente marcou o checkbox");
    } else {
        checkbox.value = "False";
        console.log("O cliente não marcou o checkbox");
    }
}
    