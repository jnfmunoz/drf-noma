$(document).ready(function(){

    function buildList() {

        const url = 'http://127.0.0.1:8000/cliente-api/asesoria/list/'

        fetch(url)
            .then((response) => response.json())
            .then(function (data){
                const list = $('#tbody-list');
                let asesoriaList = '';
                for(let index = 0; index < data.length; index++){
                    const asesoria = data[index];
                    const fechaTermino = asesoria.fecha_termino === null ? "Sin Asignar" : asesoria.fecha_termino;

                    asesoriaList = asesoriaList +   `<tr class="col-12">
                                                        <td class="col-2">${asesoria.fecha_creacion}</td>
                                                        <td class="col-2">${fechaTermino}</td>
                                                        <td class="col-2">${asesoria.tipo_asesoria}</td>
                                                        <td class="col-2">${asesoria.estado_asesoria}</td>
                                                        <td class="col-3">
                                                            <a href="/cliente/asesoria/update/${asesoria.id}/" class="btn btn-outline-warning btn-warning text-dark">Actualizar</a>                                                        
                                                            <a href="/cliente/asesoria/detail/${asesoria.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                                        </td>                                                        
                                                    </tr>`
                };
            list.empty();
            list.append(asesoriaList);
            });
    };

    let btnNewAsesoria = $("#btnNewAsesoria");

    btnNewAsesoria.click(function(){
        // Obtiene el valor seleccionado del combo box
        let tipoAsesoria = $("#comboTipoAsesoria").val();
        
        // Obtiene los valores de los campos de entrada
        // let descripcion = $("#descripcion").val();
        let nombre_fiscalizador = $('#nombre_fiscalizador').val();
        let numero = $("#numero_fiscalizador").val();
        let email = $("#email").val();

        // Validaciones
        if(nombre_fiscalizador.length <= 5){
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "El nombre del fiscalizador es muy corto!",
                showConfirmButton: false,
                timer: 5000,
            });
            return
        }

        if (numero.length < 12 || numero.length > 12) {
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "El número del fiscalizador es inválido!",
                showConfirmButton: false,
                timer: 5000,
            });
            return;
        }
        
        if (numero.substring(0,4) !== "+569") {
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "El número del fiscalizador es inválido, asegúrate de que empiece con +569",
                showConfirmButton: false,
                timer: 5000,
            });
            return;
        }

        // Crea un objeto con los datos que deseas enviar en la solicitud POST
        var dataToSend = {
            // "descripcion": descripcion,
            "nombre_fiscalizador": nombre_fiscalizador,
            "numero_fiscalizador": numero,
            "email": email,
            "tipo_asesoria": tipoAsesoria
        };

        // URL de la API a la que deseas hacer la solicitud POST
        let url = 'http://127.0.0.1:8000/cliente-api/asesoria/new/'
                
        //Mostrar un cuadro de diálogo de confirmación
        Swal.fire({
            title: "Nueva Asesoría",
            text: "¿Deseas enviar una nueva solicitud?",
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
                        // console.log("Respuesta:", response);
                    },
                    error: function(error) {
                        console.error("Error:", error);
                    }
                })
                .done(function(response) {
                    // La solicitud POST se completó con éxito
                    Swal.fire({
                        icon: "success",
                        title: "¡Éxito!",
                        text: "Solicitud de asesoría agregada con éxito",
                        showConfirmButton: false,
                        timer: 2000,                                                                    
                    });
                    setTimeout(function() {
                        // Redirigir a la página de listado (reemplaza con la URL deseada)
                        window.location.href = "/cliente/asesoria/list/";
                    }, 2050);
                    
                })
                .fail(function(jqXHR, textStatus, errorThrown) {
                    // La solicitud POST falló
                    Swal.fire({
                        icon: "error",
                        title: "Ops!",
                        text: "Error al enviar solicitud",
                        showConfirmButton: false,
                        timer: 2000,     
                    });
                });
                }
            });
        // Realiza la solicitud POST
        // $.ajax({
        //     type: "POST",
        //     url: url,
        //     data: JSON.stringify(dataToSend),
        //     contentType: "application/json",
        //     beforeSend: function(xhr, settings) {
        //         xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        //     },
        //     success: function(response) {
        //         console.log("Respuesta:", response);
        //     },
        //     error: function(error) {
        //         console.error("Error:", error);
        //     }
        // });

        // if (confirm("¿Estás seguro de que deseas enviar el formulario?")) {
        //     // El usuario hizo clic en "Aceptar", enviar la solicitud POST aquí
        //     // Realiza la solicitud POST
        //     $.ajax({
        //         type: "POST",
        //         url: url,
        //         data: JSON.stringify(dataToSend),
        //         contentType: "application/json",
        //         beforeSend: function(xhr, settings) {
        //             xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        //         },
        //         success: function(response) {
        //             console.log("Respuesta:", response);
        //         },
        //         error: function(error) {
        //             console.error("Error:", error);
        //         }
        //     })
        //     .done(function(response) {
        //         // La solicitud POST se completó con éxito
        //         // incorportar en vez de las alert SweetAlert2
        //         alert("Solicitud POST exitosa: " + response);

        //         // Redirigir la página de listado
        //         window.location.href = "/cliente/list/";
        //     })
        //     .fail(function(jqXHR, textStatus, errorThrown) {
        //         // La solicitud POST falló
        //         alert("Error en la solicitud POST: " + textStatus);
        //       });
        // } 
        // else {
        //     // El usuario hizo clic en "Cancelar", no se envía la solicitud POST
        //     alert("Solicitud POST cancelada.");
        // }
    });

    function buildDetail(){
        // Extraer la ID de la URL de forma dinámica
        var url = window.location.href;
        var parts = url.split('/');
        var id = parts[parts.length - 2]

        if(!isNaN(id)){ // Verificar si la id es un numero
            // Construir la URL del endpoint de API con la id dinamica
            let apiURL = 'http://127.0.0.1:8000/cliente-api/asesoria/detail/' + id + '/';
               
            $.ajax({
                url: apiURL,
                type: 'GET',
                dataType: 'json',
                success: function(data){
                    $('#id').text('N° Solicitud: ' + data.id);
                    $('#fecha-inicio').text('Fecha Inicio: ' + data.fecha_creacion);

                    if(data.descripcion == null){
                        $('#descripcion').text('Observaciones: No se han realizado observaciones');    
                    }
                    else{
                        $('#descripcion').text('Observaciones: ' + data.descripcion);
                    }
                    
                    if(data.fecha_termino == null){
                        $('#fecha-termino').text('Fecha Término: Sin Asignar');
                    } 
                    else{
                        $('#fecha-termino').text('Fecha Término: ' + data.fecha_termino);
                    }
                    
                    if(data.tipo_asesoria === 1){
                        $('#tipo-asesoria').text('Tipo de Asesoría: Accidente');                        
                    }
                    else if(data.tipo_asesoria === 2) {
                        $('#tipo-asesoria').text('Tipo de Asesoría: Fiscalización');
                    }
                    else{
                        $('#tipo-asesoria').text('Tipo de Asesoría: Desconocido');
                    }

                    if(data.estado_asesoria === 1){
                        $('#estado-asesoria').text('Estado: Ingresada');
                    }
                    else if(data.estado_asesoria === 2){
                        $('#estado-asesoria').text('Estado: En Curso');
                    }
                    else if(data.estado_asesoria === 3){
                        $('#estado-asesoria').text('Estado: Finalizada');
                    }
                    else if(data.estado_asesoria === 4){    
                        $('#estado-asesoria').text('Estado: Aprobada');
                    }
                    else if(data.estado_asesoria === 5){
                        $('#estado-asesoria').text('Estado: Rechazada');
                    }                    
                    
                    if(data.fkProfesional == null){
                        $('#profesional').text('Profesional: Sin Asignar');
                    } 
                    else{
                        $('#profesional').text('Profesional: ' + data.fkProfesional);
                    }

                    $('#nombre-fiscalizador').text('Nombre Fiscalizador: ' + data.nombre_fiscalizador);
                    $('#numero-fiscalizador').text('Número de teléfono: ' + data.numero_fiscalizador);
                    $('#email-fiscalizador').text('Correo electrónico: ' + data.email);
                },
                // error: function(error){
                //     console.log('Error al cargar el detalle de la asesoria ');
                // }
            });
        } 
        // else {
        //     console.log('id no valida');
        // };
    };

    function buildUpdate(){
        // Extraer la ID de la URL de forma dinámica
        var url = window.location.href;
        var parts = url.split('/');
        var id = parts[parts.length - 2]
        
        // Realiza una solicitud GET para cargar los datos de la solicitud de asesoría
        // Construir la URL del endpoint de API con la id dinamica
        let apiURL = 'http://127.0.0.1:8000/cliente-api/asesoria/update/' + id + '/';
            
        $.ajax({
            url: apiURL,
            type: 'GET',
            dataType: 'json',
            success: function(data){            
                
                // Rellena los campos del formulario con los datos obtenidos
                $('#id_update').text('N° Solicitud: ' + data.id);
                $('#comboTipoAsesoria_update').val(data.tipo_asesoria);
                $('#descripcion_update').text(data.descripcion);
                $('#nombre_fiscalizador_update').val(data.nombre_fiscalizador);
                $('#numero_fiscalizador_update').val(data.numero_fiscalizador);
                $('#email_update').val(data.email);
            },
            // error: function(error){
            //     console.log('Error al cargar el detalle de la asesoria ');
            // }
        });

        // Maneja el envío del formulario
        $('#asesoriaFormUpdate').submit(function(event){
            event.preventDefault(); // Evita que el formulario se envía de forma predeterminada

            // obtener los datos del formulario
            var formData = {
                descripcion: $('#descripcion_update').val() ,
                nombre_fiscalizador: $('#nombre_fiscalizador_update').val(),
                numero_fiscalizador: $('#numero_fiscalizador_update').val(),
                email: $('#email_update').val(),
                tipo_asesoria: $('#comboTipoAsesoria_update').val()
            }
            
            //Mostrar un cuadro de diálogo de confirmación
            Swal.fire({
                title: "Actualizar solicitud Asesoría",
                text: "¿Deseas actualizar la solicitud?",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Sí, enviar",
                cancelButtonText: "Cancelar"
                }).then((result) => {
                if (result.isConfirmed) {
                    // El usuario hizo clic en "Aceptar", enviar la solicitud PUT aquí
                    $.ajax({
                        type: 'PUT',
                        url: apiURL,
                        data: JSON.stringify(formData),
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
                .done(function(response){
                    // La solicitud PUT se completó con éxito
                    Swal.fire({
                        icon: "success",
                        title: "¡Éxito!",
                        text: "Actualización de solicitud exitosa",
                        showConfirmButton: false,
                        timer: 2000,                                                                    
                    });
                    // "¡Éxito!", "Solicitud PUT exitosa: " + response, "success"
                    // Establece un temporizador para redirigir después de 2 segundos (2000 ms)
                    setTimeout(function() {
                        // Redirigir a la página de listado (reemplaza con la URL deseada)
                        window.location.href = "/cliente/asesoria/list/";
                    }, 2050);
                })
                .fail(function(jqXHR, textStatus, errorThrown) {
                    // La solicitud POST falló
                    Swal.fire({
                        icon: "error",
                        title: "Ops!",
                        text: "Error en la actualización de solicitud",
                        showConfirmButton: false,
                        timer: 2000,     
                    });
                    //"Error en la actualización de solicitud");
                });
                }
            });
        });     
    };

    $('form').submit(function(event) {
        event.preventDefault();

        // Obtener los valores de las fechas
        var fechaInicio = $('#fechainicio').val();
        var fechaTermino = $('#fechatermino').val();

        // console.log(fechaInicio, fechaTermino)

        // Realizar petición AJAX
        $.ajax({
            url: 'http://127.0.0.1:8000/cliente-api/asesoria/list/',
            method: 'GET',
            data: {
                search: fechaInicio + ',' + fechaTermino
            },
            success: function(data) {
                // Limpiar la tabla antes de agregar los nuevos resultados
                $('#tbody-list').empty();
                    
                if(data.length === 0){
                    // Si no hay resultados, mostrar un mensaje en la tabla
                    let noResultsRow = '<tr class="col-12"><td colspan="5" class="text-center">Sin resultados</td></tr>';
                    $('#tbody-list').append(noResultsRow);
                }
                else{
                    // Iterar sobre los resultados y agregarlos a la tabla
                    $.each(data, function(index, asesoria) {

                        const fechaTermino = asesoria.fecha_termino === null ? "Sin Asignar" : asesoria.fecha_termino;
                        var row = `<tr class="col-12">
                                        <td class="col-2">${asesoria.fecha_creacion}</td>                                        
                                        <td class="col-2">${fechaTermino}</td>
                                        <td class="col-2">${asesoria.tipo_asesoria}</td>
                                        <td class="col-2">${asesoria.estado_asesoria}</td>
                                        <td class="col-3">
                                            <a href="/cliente/asesoria/update/${asesoria.id}/" class="btn btn-outline-warning btn-warning text-dark">Actualizar</a>                                                        
                                            <a href="/cliente/asesoria/detail/${asesoria.id}/" class="btn btn-outline-info btn-info text-dark">Ver Más</a>
                                        </td>                                                        
                                    </tr>`;

                        $('#tbody-list').append(row);                    
                    });
                }
            },
            error: function(error){
                console.log('Error en la petición AJAX: ', error);
            }    
        });
    });

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