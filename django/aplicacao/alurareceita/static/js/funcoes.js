var checkbox = document.querySelector("input[name=publicada]");
checkbox.addEventListener("change", verificaCheck());
function verificaCheck()
    alert('FOI')
    if(checkbox.checked) {
        console.log("O cliente marcou o checkbox");
    } else {
        console.log("O cliente não marcou o checkbox");
    }