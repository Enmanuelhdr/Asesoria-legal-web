// Función para cargar y mostrar los datos desde el archivo JSON
function mostrarAsesorias() {
    // Ruta del archivo JSON
    var jsonUrl = "data/asesorias/asesoria.json";

    // Obtener el contenedor de asesorías
    var asesoriasContainer = document.getElementById("asesorias-container");

    // Realizar una solicitud HTTP para obtener los datos del JSON
    fetch(jsonUrl)
        .then(response => response.json())
        .then(data => {
            data.forEach(asesoria => {
                // Crear elementos HTML
                var div = document.createElement("div");
                div.className = "col-12 col-md-6 col-lg-4";

                var img = document.createElement("img");
                img.src = asesoria.imagen;
                img.alt = "Imagen de asesoría";

                var h2 = document.createElement("h2");
                h2.className = "fw-normal";
                h2.textContent = asesoria.titulo;

                var p = document.createElement("p");
                p.className = "fw-semibold";
                p.textContent = asesoria.descripcion;

                // Agregar elementos al contenedor
                div.appendChild(img);
                div.appendChild(h2);
                div.appendChild(p);
                asesoriasContainer.appendChild(div);
            });
        })
        .catch(error => {
            console.error("Error al cargar los datos:", error);
        });
}

// Llamar a la función cuando la página web se abra
mostrarAsesorias();