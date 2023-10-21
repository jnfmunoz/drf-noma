$(document).ready(function(){

    function buildList(){
        const url = 'http://127.0.0.1:8000/cliente-api/accidente/list/';

        fetch(url)
            .then((response) => response.json())
            .then(function(data) {
                const list = $('#tbody-list');
                let accidenteList = '';
                for(let index = 0; index < data.length; index++) {
                    const accidente = data[index];
                    
                    // Por caída, Por exposición o contacto, Por sobreesfuerzo o golpes, Por movimientos repetitivos
                    let tipoAccidente = "";
                    if(accidente.tipo_accidente === 1) {
                        tipoAccidente = "Por Caída";
                    }
                    else if(accidente.tipo_accidente === 2){
                        tipoAccidente = "Por exposición o contacto";
                    }
                    else if(accidente.tipo_accidente === 3){
                        tipoAccidente = "Por sobreesfuerzo o golpes";
                    }
                    else if(accidente.tipo_accidente === 4){
                        tipoAccidente = "Por movimientos repetitivos";
                    }

                    // console.log(accidente); /cliente/asesoria/update/${asesoria.id} 
                    accidenteList  =    accidenteList + `<tr class="col-12">
                                                            <td>${accidente.fecha_accidente}</td>
                                                            <td>${accidente.descripcion}</td>
                                                            <td>${accidente.cantidad_involucrados}</td>
                                                            <td>${tipoAccidente}</td>
                                                            <td>                                                                
                                                                <a href="/cliente/accidente/update/${accidente.id}/" class="btn btn-outline-warning btn-warning text-dark">Actualizar</a>
                                                                <a href="/cliente/accidente/detail/${accidente.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>                  
                                                            </td>
                                                        </tr>`;
                };
            list.empty();
            list.append(accidenteList);
        });
    };

    let btnNewAccidente = $("#btnNewAccidente");

    btnNewAccidente.click(function(){        
        // Combobox
        let tipoAccidente = $("#comboTipoAccidente").val();

        // Valores de los campos de entrada
        let fecha_accidente = $("#fecha_accidente").val(); 
        let cantidad_involucrados = $("#cantidad_involucrados").val();
        let descripcion = $("#descripcion").val();

        var dataToSend = {
            "fecha_accidente" : fecha_accidente,
            "cantidad_involucrados" : cantidad_involucrados,
            "descripcion" : descripcion,
            "tipo_accidente" : tipoAccidente
        };

        let url = "http://127.0.0.1:8000/cliente-api/accidente/new/";

        Swal.fire({
            title: "Nueva Accidente",
            text: "¿Deseas registrar un nuevo accidente?",
            icon: "question",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Sí, enviar",
            cancelButtonText: "Cancelar"
            }).then((result) => {
            if (result.isConfirmed) {
                // El usuario hizo clic en "Aceptar", enviar la solicitud POST aquí
                $.ajax({
                    type: "POST",
                    url: url,
                    data: JSON.stringify(dataToSend),
                    contentType: "application/json",
                    beforeSend: function(xhr, settings) {
                        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                    },
                    success: function(response) {
                        console.log("Respuesta:", response);
                    },
                    error: function(error) {
                        console.error("Error:", error);
                    }
                })
                .done(function(response) {
                    // La solicitud POST se completó con éxito
                    Swal.fire("¡Éxito!", "Solicitud POST exitosa: " + response, "success");
                    
                    // Redirigir a la página de listado (reemplaza con la URL deseada)
                    window.location.href = "/cliente/accidente/list/";
                    })
                    .fail(function(jqXHR, textStatus, errorThrown) {
                    // La solicitud POST falló
                    Swal.fire("Error", "Error en la solicitud POST: " + textStatus, "error");
                    });
                }
            });
    });

    function buildDetail(){
        let url = window.location.href;
        let parts = url.split("/");
        let id = parts[parts.length - 2];

        let apiUrl = 'http://127.0.0.1:8000/cliente-api/accidente/detail/' + id + '/';

        $.ajax({
            url: apiUrl,
            type: "GET",
            dataType: "json",
            success: function(data) {
                $('#id').text('N° Accidente: '+ data.id);        
                $('#fecha-accidente').text('Fecha Accidente: ' +data.fecha_accidente);   
                $('#cantidad-involucrados').text('Cantidad de Involucrados: '+ data.cantidad_involucrados);
                $('#descripcion').text('Informe Situación: '+ data.descripcion);
                $('#tipo-accidente').text('Tipo Accidente: '+ data.tipo_accidente);
            },
        })
    };

    function buildUpdate(){
        let url = window.location.href;
        let parts = url.split('/');
        let id = parts[parts.length -2]

        let apiURL = 'http://127.0.0.1:8000/cliente-api/accidente/update/' + id + '/';

        $.ajax({
            url: apiURL,
            type: 'GET',
            dataType: 'json',
            success: function(data){

                $('#id_update').text('N° Accidente: ' + data.id);
                $('#fecha_accidente_update').val(data.fecha_accidente);
                $('#cantidad_involucrados_update').val(data.cantidad_involucrados);
                $('#descripcion_update').text(data.descripcion);
                $('#comboTipoAccidente_update').val(data.tipo_accidente);
            },
        });

        $('#accidenteFormUpdate').submit(function(event) {
            event.preventDefault();

            let formData = {
                fecha_accidente: $('#fecha_accidente_update').val(),
                cantidad_involucrados: $('#cantidad_involucrados_update').val(),
                descripcion : $('#descripcion_update').val(),
                tipo_accidente : $('#comboTipoAccidente_update').val(),
            }
            
            Swal.fire({
                title: "Actualizar Accidente",
                text: "¿Deseas actualizar registro de accidente?",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Sí, enviar",
                cancelButtonText: "Cancelar"
                }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        type: 'PUT',
                        url: apiURL,
                        data: JSON.stringify(formData),
                        contentType: "application/json",
                        beforeSend: function(xhr, settings) {
                            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                        },
                        success: function(response) {
                            // console.log("Respuesta:", response);
                            console.log("Éxito");
                        },
                        error: function(error) {
                            console.error("Error:", error);
                        }
                    })
                    .done(function(response){                                    
                        Swal.fire({
                            icon: "success",
                            title: "¡Éxito!",
                            text: "Modificación de accidente exitosa",
                            showConfirmButton: false,
                            timer: 2000,                                                                    
                            });                            
                            setTimeout(function() {                                
                                window.location.href = "/cliente/accidente/list/";
                            }, 2050);
                    })
                    .fail(function(jqXHR, textStatus, errorThrown) {
                        Swal.fire({
                            icon: "error",
                            title: "Ops!",
                            text: "Error en la actualización de solicitud",
                            showConfirmButton: false,
                            timer: 2000,
                        });
                    });
                }
            });
        });
    };

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            var cookies = document.cookie.split(";");
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    buildList();
    buildDetail();
    buildUpdate();
});