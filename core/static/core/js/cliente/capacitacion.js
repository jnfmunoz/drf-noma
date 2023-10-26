$(document).ready(function(){
    
    function buildList(){

        const url = 'http://127.0.0.1:8000/cliente-api/capacitacion/list/';

        fetch(url)
            .then((response) => response.json())
            .then(function(data){
                const list = $('#tbody-list');
                let capacitacionList = '';
                for (let i = 0; i < data.length; i++) {
                    const capacitacion = data[i];
                    const fechaCapacitacion = capacitacion.fecha_capacitacion === null ? "Sin Asignar" : capacitacion.fecha_capacitacion;
                    
                    capacitacionList = capacitacionList + `<tr class="col-12">
                                                                <td>${capacitacion.id}</td>
                                                                <td>${fechaCapacitacion}</td>
                                                                <td>${capacitacion.fkProfesional}</td>
                                                                <td>${capacitacion.direccion}</td>                
                                                                <td>${capacitacion.fkEstadoCapacitacion}</td>
                                                                <td>                                                                
                                                                    <a href="/cliente/capacitacion/detail/${capacitacion.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                                                </td>
                                                            </tr>`
                };
            list.empty();
            list.append(capacitacionList);
            });
    };

    function buildDetail(){

        let url = window.location.href;
        let parts = url.split('/');
        let id = parts[parts.length - 2];

        let apiURL = 'http://127.0.0.1:8000/cliente-api/capacitacion/detail/' + id + '/';

        $.ajax({
            url: apiURL,
            type: 'GET',
            dataType: 'json',
            success: function(data){

                // Accede al campo JSON y conviértelo en una cadena
                var jsonFieldData = data.lista_asist;
                var jsonString = JSON.stringify(jsonFieldData);


                let asistentes = data.lista_asist;

                $('#id').text('N°: ' + data.id );
                $('#descripcion').text('Tema: ' + data.descripcion);
                $('#fecha-capacitacion').text('Fecha Capacitación: ' + data.fecha_capacitacion);
                $('#profesional').text('Capacitador: ' + data.fkProfesional);
                $('#direccion').text('Dirección: ' + data.direccion);
                $('#comuna').text('Comuna: ' + data.fkComuna);
                $('#cant-asistente').text('Cantidad de asistentes: ' + data.cant_asistente);
                // $('#lista-asist').text('Listado asistentes: ' + jsonString);
                // $('#lista-asist').html('Listado asistentes: ' + jsonString);
                $('#estado-capacitacion').text('Estado: ' + data.fkEstadoCapacitacion);

                // Limpia la lista de asistentes existente
                $('#lista-asist').empty();

                if (asistentes && asistentes.length > 0) {
                    let table = $('<table>');
                    table.addClass('table'); // Agrega clases CSS si es necesario

                    // Encabezado de la tabla
                    table.append('<thead><tr><th>Nombre</th><th>Edad</th><th>Dirección</th><th>Teléfono</th><th>Email</th></tr></thead>');

                    // Cuerpo de la tabla
                    let tbody = $('<tbody>');
                    $.each(asistentes, function (index, asistente) {
                        let row = $('<tr>');
                        row.append('<td>' + asistente.nombre + '</td>');
                        row.append('<td>' + asistente.edad + '</td>');
                        row.append('<td>' + asistente.dirección + '</td>');
                        row.append('<td>' + asistente.teléfono + '</td>');
                        row.append('<td>' + asistente.email + '</td>');
                        tbody.append(row);
                    });

                    table.append(tbody);
                    $('#lista-asist').append(table);
                } else {
                    $('#lista-asist').text('No se han registrado asistentes para esta capacitación.');
                }

                console.log(data);

            },
        });
    };

    buildList();
    buildDetail();
});
