$(document).ready(function(){
    $('input#lugares').on('click', function(){
        // console.log('presionado')
        $('#interacciones tr.persona').hide();
        /* este es cuando tiene propiedades original es un block
        $('#interacciones tr.persona').css('display', 'none');*/
        $('#interacciones tr.lugar').show();
        /*$('#interacciones tr.persona').css('display', 'block');*/
    });
    $('input#personas').on('click', function(){
        $('#interacciones tr.lugar').hide();
        $('#interacciones tr.persona').show();
    });
});
