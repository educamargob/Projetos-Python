console.log('carregou')
var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
};

django.jQuery(function(){
    $('.mask-cep form-control').mask(SPMaskBehavior, spOptions);
});

  
