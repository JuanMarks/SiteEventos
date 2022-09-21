'use strict'

let btn__manual = document.getElementById('btn__manual')
let escolha1 = document.getElementById('manual')
let btn__todos = document.getElementById('btn__todos')
let escolha2 = document.getElementById('todos')
let container__manual = document.getElementById('container__manual')
let container__todos = document.getElementById('container__todos')


btn__todos.addEventListener('click', () => { 
    escolha2.click();
    if(btn__manual.classList){
        btn__manual.classList.remove('escolhido');
        btn__todos.classList.add('escolhido');
        if(container__todos.classList){
            container__todos.classList.remove('none');
            container__manual.classList.add('none');
        }
    }
});
btn__manual.addEventListener('click', () => {
    escolha1.click();
    if(btn__todos.classList){
        btn__todos.classList.remove('escolhido');
        btn__manual.classList.add('escolhido');
        if(container__manual.classList){
            container__manual.classList.remove('none');
            container__todos.classList.add('none');
        }
        
    }
})
