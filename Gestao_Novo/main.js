$.ajax({
    type: 'GET',
    url: '/apieventos/',
    success: function(response){
        console.log(response);
        const data = JSON.parse(response)
        console.log(data);
        data.forEach(el=>{
            console.log(el.fields);
        });
    },
    error: function(error){
        console.log(error);
        
    }
})