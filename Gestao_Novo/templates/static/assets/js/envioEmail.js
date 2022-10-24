'use strict'

let btn__manual = document.getElementById('btn__manual')
let escolha1 = document.getElementById('manual')
let btn__todos = document.getElementById('btn__todos')
let escolha2 = document.getElementById('todos')
let container__manual = document.getElementById('container__manual')
let btn__evento = document.getElementById('btn__evento')
let escolha3 = document.getElementById('evento')
let container__evento = document.getElementById('container__evento')
let container__todos = document.getElementById('container__todos')


btn__todos.addEventListener('click', () => { 
    escolha2.click();
    if(btn__manual.classList){
        btn__evento.classList.remove('escolhido');
        btn__manual.classList.remove('escolhido');
        btn__todos.classList.add('escolhido');
        if(container__todos.classList){
            container__todos.classList.remove('none');
            if (container__manual.classList != "none"){
                container__manual.classList.add('none');
            }
            if (container__evento.classList != "none"){
                container__evento.classList.add('none');
            }
        }
    }
});
btn__manual.addEventListener('click', () => {
    escolha1.click();
    if(btn__todos.classList){
        btn__todos.classList.remove('escolhido');
        btn__evento.classList.remove('escolhido');
        btn__manual.classList.add('escolhido');
        if(container__manual.classList){
            container__manual.classList.remove('none');
            if (container__todos.classList != "none"){
                container__todos.classList.add('none');
            }
            if (container__evento.classList != "none"){
                container__evento.classList.add('none');
            }
        }
        
    }
})
btn__evento.addEventListener('click', () => {
    escolha3.click();
    if(btn__todos.classList){
        btn__todos.classList.remove('escolhido');
        btn__manual.classList.remove('escolhido');
        btn__evento.classList.add('escolhido');
        if(container__evento.classList){
            container__evento.classList.remove('none');
            if (container__todos.classList != "none"){
                container__todos.classList.add('none');
            }
            if (container__manual.classList != "none"){
                container__manual.classList.add('none');
            }
        }
        
    }
})
