$(document).ready(function() {
    
    function buildList(){

        const url = 'http://127.0.0.1:8000/cliente-api/contrato/list/';

        fetch(url)
            .then((response) => response.json())
            .then(function(data){
                const list = $('#tbody-list');
                let contratoList = '';
                for (let i = 0; i < data.length; i++) {
                    const contrato = data[i];
                    
                    
                    contratoList = contratoList + `<tr class="col-12">
                                                                <td>${contrato.id}</td>                                                                                                                              
                                                                <td>${contrato.fecha_inicio}</td>                                                                                                                              
                                                                <td>                                                                
                                                                    <a href="/cliente/contrato/detail/${contrato.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                                                </td>
                                                    </tr>`
                };
            list.empty();
            list.append(contratoList);
            });
    };

    function buildDetail(){
        
        let url = window.location.href;
        let parts = url.split('/');
        let id = parts[parts.length - 2];

        let apiURL = 'http://127.0.0.1:8000/cliente-api/contrato/detail/' + id + '/';

        $.ajax({
            url: apiURL,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                $('#id').text('N° Contrato: ' + data.id );
                $('#fkCliente').text('Cliente: ' + data.fkCliente);
                $('#fecha_inicio').text('Fecha Inicio: ' + data.fecha_inicio);
                $('#fecha_termino').text('Fecha Término: ' + data.fecha_termino);
                $('#descripcion').text('Descripción: ' + data.descripcion);
                $('#costo_mensual').text('Costo Mensual: ' + data.costo_mensual);
                $('#costo_modificacion_formulario').text('Costo modificación formulario: ' + data.costo_modificacion_formulario);
                $('#costo_capacitacion_extra').text('Costo capacitación extra: ' + data.costo_capacitacion_extra);
                $('#costo_asesoria_extra').text('Costo Asesoría extra: ' + data.costo_asesoria_extra);
                $('#costo_actualizar_informe').text('Costo por actualizar informe: ' + data.costo_actualizar_informe);
            },
        });
    };

    buildList();
    buildDetail();
});

// /cliente/capacitacion/detail/${capacitacion.id}/