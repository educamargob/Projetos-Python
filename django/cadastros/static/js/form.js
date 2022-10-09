
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
    $('.mask-preco').mask("#.##0,00", {reverse: true});

    $('#cliente_form').submit(function(){
        $('#cliente_form').find(":input[class*='mask-']").unmask();
    }) 
    $('#produto_form').submit(function(){
        $('#produto_form').find(":input[class*='mask-']").unmask();
    });

    const preencheForm = (endereco) => {
        $('#id_endereco')[0].value = endereco.logradouro;
        $('#id_bairro')[0].value = endereco.bairro;
        $('#id_cidade')[0].value = endereco.localidade;
        $('#id_estado')[0].value = endereco.uf;
    }
    const limpaForm =()=>{
        $('#id_endereco')[0].value = '';
        $('#id_bairro')[0].value = '';
        $('#id_cidade')[0].value = '';
        $('#id_estado')[0].value = '';
    }
    const buscaEndereco = (cep) => {
        const url = `http://viacep.com.br/ws/${cep}/json/`
        django.jQuery.get( url, function( data ) {
        var erro = 0;
        if(data.erro == 'true' && erro == 0){
            var section = $("<section />");
            section.append("<ul><li>CEP informado é inválido</li></ul>")
            section.attr({
                class:"alert alert-danger", 
                role:"alert"
            });
            $('#id_CEP').append(section);
            erro = 1;
        }else{
            $('.alert-danger').style.display = 'none';
            console.log(data)
            preencheForm(data); 
        }                            
        });
    }
    $('.mask-cep').focusout(function(){
        const cep = $('.mask-cep').unmask()[0].value;
        if(cep != ''){
            buscaEndereco(cep);
        }else{
            limpaForm();
        }
        $('.mask-cep').mask('00000-000');
        
    });
});



  
