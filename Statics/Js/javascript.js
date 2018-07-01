function __init()
{

    $('#search_input')
        .val('')
        .focus()
        .keyup(function(){

            if(!$.trim($(this).val()))
                $('.results .error').empty().hide();
        });

    var cache = {};
    $('#search_input').autocomplete({
        minLength: 2,
        select: function( event, ui ) {
            return false;
        },
        open: function() {
            $('.results .wrapper').html($(this).autocomplete("widget").html());
            $(this).autocomplete("widget").hide();
        },
        source: function( request, response ) {
            if (cache[request.term]) {
                response(cache[request.term]);
                return;
            }

            $.ajax({
                dataType : 'json',
                method : 'POST',
                url : '/Carrera/search/',
                data : {
                    q : encodeURIComponent(request.term),
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(data) {
                    var series = [];
                    for(var x in data)
                    {
                        series.push({
                            id: data[x].fields['id'],
                            nombre_serie : data[x].fields['nombre_serie'],
                            descripcion: data[x].fields['descripcion']
                        });
                    }
                    cache[request.term] = series;
                    response(series);
                },
            });
        },
        response: function(event, ui) {

            if (ui.content.length === 0) {
                $('.results .error').html('No se encontraron resultados').show();
                $('.results .wrapper').empty();
            }
            else
                $('.results .error').empty().hide();
        }
    }).autocomplete('instance')._renderItem = function(ul, item) {

        var serie_tmpl = $('<div />')
                        .addClass('Serie')
                        .append('<a href="/" />').find('a').addClass('nombre_serie').html(item.nombre_serie)
                        .parent()
                        .append('<span class="id"><strong>id:</strong><span></span></span>')
                        .find('.id > span').append(item.id)
                        .parent().parent()
                        .append('<span class="descripcion"><strong>Descripcion:</strong><span></span></span>')
                        .find('.descripcion > span').append(item.descripcion)
                        .parent().parent();

        return $('<div></div>')
            .data('item.autocomplete', item)
            .append(serie_tmpl)
            .appendTo(ul);
    };
}

$(document).ready(__init);