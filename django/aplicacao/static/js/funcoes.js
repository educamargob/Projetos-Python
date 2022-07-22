console.log("FOIIII");
var checkbox = document.querySelector("input[name=checkbox]");
function verificaCheck()
    if(checkbox.checked) {
        console.log("O cliente marcou o checkbox");
    } else {
        console.log("O cliente não marcou o checkbox");
    }