$(document).ready(function(){
    var textos = ["InfoVeg", "Sáude", "Bem estar", "Nova maneira", "De", "Vida"];
    var atual = 0;
    $('#frases').text(textos[atual++]);
    setInterval(function() {
        $('#frases').fadeOut(function() {
            if (atual >= textos.length) atual = 0;
            $('#frases').text(textos[atual++]).fadeIn();
        });
    }, 3000);
});