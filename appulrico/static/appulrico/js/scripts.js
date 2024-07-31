document.addEventListener('DOMContentLoaded', function() {
    // Asegúrate de que los mensajes sean accesibles en el HTML
    if (window.messages && Array.isArray(window.messages)) {
        window.messages.forEach(function(message) {
            Swal.fire({
                icon: message.tags,
                title: message.message,
                showConfirmButton: true,
                timer: 3000
            });
        });
    }
});