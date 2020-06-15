$(document).ready(function () {
    // Boton para añadir un campo para registrar las personas
    $('#add_person').click(function (e) {
      e.preventDefault();
      $('#persons').append('<div class="row col-sm-10"><input type="text" class="form-control mt-2" name="persona[]" placeholder="Ingrese el nombre" required><a href="#" class="btn btn-danger remover_person">-</div>');
    });
  
    // Remover campo persona
    $('#persons').on('click', '.remover_person', function (e) {
      e.preventDefault();
      $(this).parent('div').remove();
    });
  
    // Boton para añadir un campo para registrar los lugares
    $('#add_lugar').click(function (e) {
      e.preventDefault();
      $('#lugares').append('<div class="row col-sm-10"><input type="text" class="form-control mt-2" name="lugares[]" placeholder="Ingrese el lugar visitado" required><a href="#" class="btn btn-danger remover_lugar">-</div>');
    });
  
    // Remover lugares
    $('#lugares').on('click', '.remover_lugar', function (e) {
      e.preventDefault();
      $(this).parent('div').remove();
    });
  
    // Evento del boton enviar
    $('#enviar').click(function (e) {
      e.preventDefault();
      alert('El formulario se ha enviado');
    });
  });