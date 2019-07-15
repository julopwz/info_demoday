$(document).ready(function(){
    let textos = ["InfoVeg","Área do cliente"];
    let atual = 0;
    $('#frases').text(textos[atual++]);
    setInterval(function() {
        $('#frases').fadeOut(function() {
            if (atual >= textos.length) atual = 0;
            $('#frases').text(textos[atual++]).fadeIn();
        });
    }, 3000);
});