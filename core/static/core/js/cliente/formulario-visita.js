$(document).ready(function() {

    function buildList(){

        const url = 'http://127.0.0.1:8000/cliente-api/formulario/list/';

        $.ajax({
            type: 'GET',
            url: url,
            dataType: 'json',
            success: function(data){
                if (data.length > 0){
                    const list = $('#tbody-list');

                    data.forEach(formularioVisita => {
                        formularioVisita.item.forEach(item => {
                            const fila = $('<tr>');
                            fila.append($('<td>').text(item.id));
                            fila.append($('<td>').text(item.fkElementoRevision));
                            fila.append($('<td>').text(item.se_cumple));
                            list.append(fila);
                        });
                    });
                        
                } else {
                    console.log('No se encontraron resultados.');                    
                }
                console.log(data);
            },
            error: function() {
                console.log('Error al cargar los datos');
            }
        });
    };

    buildList();
});