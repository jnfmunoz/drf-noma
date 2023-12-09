$(document).ready(function(){

    function buildList(){
        
        const url = 'http://127.0.0.1:8000/cliente-api/visita/list/'

        fetch(url)
            .then((response) => response.json())
            .then(function(data) {
                const list = $('#tbody-list');
                let visitaList = '';
                for(let index = 0; index < data.length; index++) {
                    const visita = data[index];
                    
                    visitaList = visitaList +   `<tr class="col-12">
                                                    <td class="col-2">${visita.fecha_inicio}</td>
                                                    <td class="col-2">${visita.fecha_termino}</td>
                                                    <td class="col-2">${visita.direccion}</td>
                                                    <td class="col-2">${visita.fkComuna}</td>
                                                    <td class="col-2">${visita.fkEstadoVisita}</td>
                                                    <td class="col-2">                                                    
                                                        <a href="/cliente/visita/detail/${visita.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                                    </td>                                                        
                                                </tr>`

                };
                list.empty();
                list.append(visitaList);
            });
    };

    function buildDetail(){

        let url = window.location.href;
        let parts = url.split('/');
        let id = parts[parts.length - 2];

        let apiURL = 'http://127.0.0.1:8000/cliente-api/visita/detail/' + id + '/';

        $.ajax({
            url: apiURL,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                $('#fecha_inicio').text('Fecha Inicio: ' + data.fecha_inicio);
                $('#fecha_termino').text('Fecha Termino: ' + data.fecha_termino);                
                $('#profesional').text('Profesional Asignado: ' + data.fkProfesional);                
                $('#estado').text('Estado Visita: ' + data.fkEstadoVisita);
                $('#direccion').text('Dirección: ' + data.direccion);
                $('#comuna').text('Comuna: ' + data.fkComuna);
                $('#descripcion').text('Observaciones: ')
            },
        })
    }

    $('form').submit(function(event){
        event.preventDefault();

        // Obtener los valores de las fechas
        let fechaInicio = $('#fechainicio').val();
        let fechaTermino = $('#fechatermino').val();

        // console.log(fechaInicio, fechaTermino);

        // Realizar petición AJAX
        $.ajax({
            url: 'http://127.0.0.1:8000/cliente-api/visita/list/',
            method: 'GET',
            data: {
                search: fechaInicio + ',' + fechaTermino
            },
            success: function(data) {
                // Limpiar la tabla antes de agregar los nuevos resultados
                $('#tbody-list').empty();

                if(data.length === 0){
                    let noResultsRow = '<tr class="col-12"><td colspan="6" class="text-center">Sin resultados</td></tr>';
                    $('#tbody-list').append(noResultsRow);
                }
                else{
                    // Iterar sobre los resultados y agregarlos a la tabla
                    $.each(data, function(index, visita){
                        
                        const fechaTermino = visita.fecha_termino === null ? "Sin Asignar" : visita.fecha_termino;
                        let row = `<tr class="col-12">
                                        <td class="col-2">${visita.fecha_inicio}</td>
                                        <td class="col-2">${fechaTermino}</td>
                                        <td class="col-2">${visita.direccion}</td>
                                        <td class="col-2">${visita.fkComuna}</td>
                                        <td class="col-2">${visita.fkEstadoVisita}</td>
                                        <td class="col-2">                                                    
                                            <a href="/cliente/visita/detail/${visita.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                        </td>                                                        
                                    </tr>`;
                        $('#tbody-list').append(row);
                    });
                }
            },
            error: function(error) {
                console.error('Error en la petición AJAX: ' + error);
            }
        });

    });

    buildDetail();
    buildList();
});