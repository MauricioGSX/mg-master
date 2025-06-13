document.addEventListener('DOMContentLoaded', function() {
    // Selecciona los elementos <link> con rel="icon" o rel="shortcut icon"
    var iconLinks = document.querySelectorAll("link[rel='icon'], link[rel='shortcut icon']");

    // Elimina cada uno de los iconos seleccionados
    iconLinks.forEach(function(iconLink) {
        iconLink.parentNode.removeChild(iconLink);
    });
});
