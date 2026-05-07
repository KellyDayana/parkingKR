// Script para calcular cobro automáticamente
function calcularCobro(button) {
    // Obtener valores del formulario
    const pagoSelect = document.getElementById('id_pago');
    const tarifaSelect = document.getElementById('id_tarifa');
    
    if (!pagoSelect.value || !tarifaSelect.value) {
        alert('Por favor selecciona un Pago y una Tarifa');
        return;
    }
    
    // Crear un formulario temporal para enviar datos
    const form = document.querySelector('form');
    
    // Enviar el formulario (Django manejará el cálculo en save_model)
    form.submit();
}

// Cuando se carga la página, mostrar los cálculos
document.addEventListener('DOMContentLoaded', function() {
    const pagoSelect = document.getElementById('id_pago');
    const tarifaSelect = document.getElementById('id_tarifa');
    
    // Actualizar cuando cambie el pago o tarifa
    if (pagoSelect) {
        pagoSelect.addEventListener('change', function() {
            mostrarCalculoAutomatico();
        });
    }
    
    if (tarifaSelect) {
        tarifaSelect.addEventListener('change', function() {
            mostrarCalculoAutomatico();
        });
    }
});

function mostrarCalculoAutomatico() {
    // Este es un placeholder - el cálculo real se hace en el servidor
    console.log('Pago y tarifa seleccionados - el cálculo se realizará al guardar');
}
