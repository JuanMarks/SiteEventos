var botaoAvancar = document.querySelector(".botaoAvancar");
var botaoAnterior = document.querySelector(".botaoAnterior");

botaoAvancar.addEventListener("click", () => {
    if (botaoAvancar.value == "step2") {
        document.querySelector("#step1").style.display = "none";
        document.querySelector("#step2").style.display = "block";
        document.querySelector("#step3").style.display = "none";
        document.querySelector(".botao").style.display = "none";
        document.querySelector(".botaoAnterior").style.visibility = "visible";
        document.querySelector('#step-usuario').classList.remove('active');
        document.querySelector('#step-email').classList.add('active');
        botaoAvancar.value = "step3";
        botaoAnterior.value = "step1";
    } else if (botaoAvancar.value == "step3") {
        document.querySelector("#step1").style.display = "none";
        document.querySelector("#step2").style.display = "none";
        document.querySelector("#step3").style.display = "block";
        document.querySelector(".botao").style.display = "block";
        document.querySelector(".botaoAnterior").style.visibility = "visible";
        document.querySelector('#step-email').classList.remove('active');
        document.querySelector('#step-senha').classList.add('active');
        botaoAvancar.style.display = "none";
        botaoAnterior.value = "step2";
    }
});

botaoAnterior.addEventListener('click', () => {
    if (botaoAnterior.value == "step1") {
        document.querySelector("#step1").style.display = "block";
        document.querySelector("#step2").style.display = "none";
        document.querySelector("#step3").style.display = "none";
        document.querySelector(".botao").style.display = "none";
        document.querySelector(".botaoAnterior").style.visibility = "hidden";
        document.querySelector('#step-usuario').classList.add('active');
        document.querySelector('#step-senha').classList.remove('active');
        document.querySelector('#step-email').classList.remove('active');
        botaoAvancar.style.display = "block";
        botaoAvancar.value = "step2";
        botaoAnterior.value = "";
    } else if (botaoAnterior.value == "step2") {
        document.querySelector("#step1").style.display = "none";
        document.querySelector("#step2").style.display = "block";
        document.querySelector("#step3").style.display = "none";
        document.querySelector(".botao").style.display = "none";
        document.querySelector(".botaoAnterior").style.visibility = "visible";
        document.querySelector('#step-email').classList.add('active');
        document.querySelector('#step-usuario').classList.remove('active');
        document.querySelector('#step-senha').classList.remove('active');
        botaoAvancar.style.display = "block";
        botaoAnterior.value = "step3";
        botaoAnterior.value = "step1";
    } else if (botaoAnterior.value = "step3") {
        document.querySelector("#step1").style.display = "none";
        document.querySelector("#step2").style.display = "none";
        document.querySelector("#step3").style.display = "block";
        document.querySelector(".botao").style.display = "none";
        document.querySelector(".botaoAnterior").style.visibility = "visible";
        document.querySelector('#step-email').classList.add('active');
        document.querySelector('#step-senha').classList.remove('active');
        botaoAnterior.style.display = "block";
        botaoAnterior.value = "step2";
    }
});