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

    buildDetail();
    buildList();
});