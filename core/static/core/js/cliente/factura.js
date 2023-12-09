$(document).ready(function(){

    function buildList() {
        
        const url = 'http://127.0.0.1:8000/cliente-api/factura/list/';

        fetch(url)
            .then((response) => response.json())
            .then(function(data) {
                const list = $('#tbody-list');
                let facturaList = '';
                for(let index = 0; index < data.length; index++) {
                    const factura = data[index];

                    const estadoPago = factura.pagada ? 'Pagada' : 'Pendiente de Pago';
                    
                    facturaList = facturaList + `<tr class="col-12">
                                                    <td class="col-2">${factura.id}</td>
                                                    <td class="col-2">${factura.fecha_emision}</td>
                                                    <td class="col-2">${factura.fecha_vencimento}</td>
                                                    <td class="col-2">${factura.total_factura}</td>
                                                    <td class="col-2">${estadoPago}</td>
                                                    <td class="col-3">
                                                        <a href="/cliente/factura/detail/${factura.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                                    </td>                                                                        
                                                </tr>`;                                                                                
                };
            list.empty();
            list.append(facturaList);
            });
    };

    function buildDetail(){
        
        let url = window.location.href;
        let parts = url.split('/');
        let id = parts[parts.length - 2];

        let apiURL = 'http://127.0.0.1:8000/cliente-api/factura/detail/' + id + '/';

        $.ajax({
            url: apiURL,
            type: 'GET',
            dataType: 'json',
            success: function(data){

                const estadoPago = data.pagada ? 'Pagada' : 'Pendiente de Pago';

                $('#id').text('N° Factura: ' + data.id );
                $('#fecha_emision').text('Fecha Emisión: ' + data.fecha_emision);
                $('#fecha_vencimento').text('Fecha Vencimiento: '+ data.fecha_vencimento);
                $('#total_factura').text('Total Factura: '+ data.total_factura);
                // $('#pagada').text('Estado: '+ data.pagada);
                $('#pagada').text('Estado: '+ estadoPago);
            },
        });
    };

    $('form').submit(function(event) {
        event.preventDefault();

        let fechaEmision = $('#fecha_emision').val();
        let fechaVencimento = $('#fecha_vencimento').val();

        // console.log(fechaEmision, fechaVencimento)

        $.ajax({
            url: 'http://127.0.0.1:8000/cliente-api/factura/list/',
            method: 'GET',
            data: {
                search: fechaEmision + ',' + fechaVencimento
            },
            success: function(data){
                $('#tbody-list').empty();

                if(data.length === 0) {
                    let noResultsRow = '<tr class="col-12"><td colspan="6" class="text-center">Sin resultados</td></tr>';
                    $('#tbody-list').append(noResultsRow);
                }
                else{
                    $.each(data, function(index, factura){
                        
                        const estadoPago = factura.pagada ? 'Pagada' : 'Pendiente de Pago';
                        let row = `<tr class="col-12">
                                        <td class="col-2">${factura.id}</td>
                                        <td class="col-2">${factura.fecha_emision}</td>
                                        <td class="col-2">${factura.fecha_vencimento}</td>
                                        <td class="col-2">${factura.total_factura}</td>
                                        <td class="col-2">${estadoPago}</td>
                                        <td class="col-3">
                                            <a href="/cliente/factura/detail/${factura.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                        </td>                                                                        
                                    </tr>`;
                        
                        $('#tbody-list').append(row);
                    });
                }
            },
            error: function(error){
                console.error('Error en la petición AJAX',error);
            }
        });
    });

    buildList();
    buildDetail();
});