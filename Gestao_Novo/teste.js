const element = document.querySelectorAll('#botao')


$(element).click(function() {
    //alert( "Clicado" );
    //const id_evento = element
    //id_evento = element.getAttribute('data-bs-whatever')
    //console.log(id_evento)
    element.forEach(el =>{
        id_evento = el.getAttribute('data-bs-whatever')
        console.log(id_evento)
    })
  });