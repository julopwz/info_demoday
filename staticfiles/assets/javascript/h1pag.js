$(document).ready(function(){
    let textos = ["InfoVeg", "Saúde", "Bem estar", "Nova maneira", "De", "Vida"];
    let atual = 0;
    $('#frases').text(textos[atual++]);
    setInterval(function() {
        $('#frases').fadeOut(function() {
            if (atual >= textos.length) atual = 0;
            $('#frases').text(textos[atual++]).fadeIn();
        });
    }, 3000);
});