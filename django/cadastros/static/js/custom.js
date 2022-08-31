
var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
};

django.jQuery(function(){

    $('.mask-cep').mask('00000-000');
    $('.mask-cnpj').mask('00.000.000/0000-00', {reverse: true});

    $('#cliente_form').submit(function(){
        $('#cliente_form').find(":input[class*='mask-']").unmask();
        console.log('carregou')
    }) 
});

  
