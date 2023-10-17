$(document).ready(function(){

    function buildList() {
        // const url = 'http://127.0.0.1:8000/cliente-api/list-asesoria-cliente-api/';
        const url = 'http://127.0.0.1:8000/cliente-api/asesoria/list/'

        fetch(url)
            .then((response) => response.json())
            .then(function (data){
                const list = $('#tbody-list');
                let asesoriaList = '';
                for(let index = 0; index < data.length; index++){
                    const asesoria = data[index];

                    asesoriaList = asesoriaList +   `<tr class="col-12">
                                                        <td class="col-2"></td>
                                                        <td class="col-2">${asesoria.fecha_termino}</td>
                                                        <td class="col-2">${asesoria.tipo_asesoria}</td>
                                                        <td class="col-2">${asesoria.estado_asesoria}</td>
                                                        <td class="col-3">
                                                            <a href="" class="btn btn-warning btn-sm">Update</a>                                                        
                                                            <a href="/cliente/asesoria/detail/${asesoria.id}" class="btn btn-info btn-sm">Ver Más</a>
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
        let descripcion = $("#descripcion").val();
        let nombre_fiscalizador = $('#nombre_fiscalizador').val();
        let numero = $("#numero_fiscalizador").val();
        let email = $("#email").val();

        // Crea un objeto con los datos que deseas enviar en la solicitud POST
        var dataToSend = {
            "descripcion": descripcion,
            "nombre_fiscalizador": nombre_fiscalizador,
            "numero_fiscalizador": numero,
            "email": email,
            "tipo_asesoria": tipoAsesoria
        };

        // URL de la API a la que deseas hacer la solicitud POST
        let url = 'http://127.0.0.1:8000/cliente-api/asesoria/new/'
        
        
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
                window.location.href = "/cliente/asesoria/list/";
              })
              .fail(function(jqXHR, textStatus, errorThrown) {
                // La solicitud POST falló
                Swal.fire("Error", "Error en la solicitud POST: " + textStatus, "error");
              });
            }
          });
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
                    $('#id').text('Número de solicitud: ' + data.id);
                    $('#fecha-inicio').text('Fecha Inicio: ' + data.fecha_creacion);
                    
                    if(data.fecha_termino == null){
                        $('#fecha-termino').text('Fecha Término: Sin Asignar');
                    } 
                    else{
                        $('#fecha-termino').text('Fecha Término: ' + data.fecha_termino);
                    }
                    
                    $('#tipo-asesoria').text('Tipo de Asesoría: ' + data.tipo_asesoria);
                    $('#estado-asesoria').text('Estado: ' + data.estado_asesoria);
                    
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
                error: function(error){
                    console.log('Error al cargar el detalle de la asesoria ');
                }
            });
        } else {
            console.log('id no valida');
        };
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
});