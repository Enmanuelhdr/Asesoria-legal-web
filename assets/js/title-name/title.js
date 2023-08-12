function capitalizarPrimeraLetra(cadena) {
    return cadena.charAt(0).toUpperCase() + cadena.slice(1);
}

// Función para actualizar el título de la página con el nombre capitalizado sin la extensión del archivo
function actualizarTituloCapitalizado() {
    // Obtener el pathname de la URL (ruta relativa)
    var currentPathname = window.location.pathname;

    // Dividir la ruta en partes utilizando '/' como separador
    var pathParts = currentPathname.split('/');

    // Obtener el nombre del documento (último elemento de la ruta)
    var documentName = pathParts[pathParts.length - 1];

    // Remover la extensión del archivo (si existe)
    var nameWithoutExtension = documentName.split('.')[0];

    // Capitalizar el nombre sin extensión
    var capitalizedTitle = capitalizarPrimeraLetra(nameWithoutExtension);

    // Actualizar el título de la página con el nombre capitalizado sin la extensión
    if (capitalizedTitle === 'Index') {
        capitalizedTitle = 'Inicio';
        document.title = capitalizedTitle;
    } else {
        document.title = capitalizedTitle;
    }
    document.title = capitalizedTitle;
}

// Llamar a la función cuando la página web se abra
actualizarTituloCapitalizado();