$.ajax({
    type: 'GET',
    url: '/apieventos/',
    success: function(response){
        console.log(response);
        const data = $.parseJSON(response.data);
        console.log(data);
        data.forEach(el=>{
            console.log(el.fields);
        });
    },
    error: function(error){
        console.log(error);
        
    }
})