$(document).ready(function() {

  //textos a serem exibidos
  var textos = ["texto 1", "texto 2", "texto 3"];

  //exibição inicial
  var atual = 0;
  $('#frases').text(textos[atual++]);

  //define intervalo de troca
  setInterval(function() {

      //efeito de desaparecer
      $('#frases').fadeOut(function() {

          //função "callback" que mostra o próximo texto
          if (atual >= textos.length) atual = 0;
          $('#frases').text(textos[atual++]).fadeIn();

      });

  }, 3000);
});