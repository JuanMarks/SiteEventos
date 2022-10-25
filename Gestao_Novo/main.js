$.ajax({
    type: 'GET',
    url: '/api/',
    success: function(response){
        console.log(response)
    },
    error: function(error){
        console.log(error)
    }
})