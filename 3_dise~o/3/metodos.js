function cargarJSON(json_path) {
  $.getJSON(json_path, function(json) {
    console.log(json);
  });
  
  //console.log(document.getElementById('agenda'));
  //document.getElementById('agenda').innerHTML = "HOLI";
}