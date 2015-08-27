/*
 Problema 3 del Test de diseño para LemonTech.\n
 */
$(document).ready(inicio);

// Array global
var horas = ["#", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00",
		"14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30"];

function inicio() {
    /*Método principal*/
    var citas = {
	    lunes: [
		    {nombre: 'Daniel', hora_inicio: '08:00', hora_termino: '09:00'},
		    {nombre: 'Daniel', hora_inicio: '09:30', hora_termino: '11:00'},
		    {nombre: 'Daniel', hora_inicio: '15:00', hora_termino: '16:00'},
		    {nombre: 'Daniel', hora_inicio: '17:00', hora_termino: '19:30'}
	    ],
	    martes: [
		    {nombre: 'Daniel', hora_inicio: '08:00', hora_termino: '09:00'},
		    {nombre: 'Daniel', hora_inicio: '11:30', hora_termino: '12:00'},
		    {nombre: 'Daniel', hora_inicio: '15:00', hora_termino: '16:00'},
		    {nombre: 'Daniel', hora_inicio: '17:00', hora_termino: '19:30'}
	    ],
	    miercoles: [
		    {nombre: 'Daniel', hora_inicio: '08:00', hora_termino: '09:00'},
		    {nombre: 'Daniel', hora_inicio: '10:30', hora_termino: '12:00'},
		    {nombre: 'Daniel', hora_inicio: '15:00', hora_termino: '16:00'},
		    {nombre: 'Daniel', hora_inicio: '17:00', hora_termino: '19:30'}
	    ],
	    jueves: [
		    {nombre: 'Daniel', hora_inicio: '08:00', hora_termino: '09:00'},
		    {nombre: 'Daniel', hora_inicio: '09:30', hora_termino: '12:00'},
		    {nombre: 'Daniel', hora_inicio: '15:00', hora_termino: '16:00'},
		    {nombre: 'Daniel', hora_inicio: '17:00', hora_termino: '19:30'}
	    ],
	    viernes: [
		    {nombre: 'Daniel', hora_inicio: '08:00', hora_termino: '09:00'},
		    {nombre: 'Daniel', hora_inicio: '09:30', hora_termino: '12:00'},
		    {nombre: 'Daniel', hora_inicio: '15:00', hora_termino: '16:00'},
		    {nombre: 'Daniel', hora_inicio: '17:00', hora_termino: '19:30'}
	    ],
	} 
	
    cargarJSON(citas)
}

function cargarJSON(jsonData) {
    /*Método encarcado de identificar el día y rellenar las citas.*/
    crearDivs(jsonData);
    
    /*Con un poco más de tiempo creo que podría encontrar una solución mejor*/
    $.each(jsonData["lunes"], function (ind, citas) {
	rellenarCitas(citas, "Lunes");
    }); 
    
    $.each(jsonData["martes"], function (ind, citas) {
	rellenarCitas(citas, "Martes");
    }); 
    
    $.each(jsonData["miercoles"], function (ind, citas) {
	rellenarCitas(citas, "Miercoles");
    }); 
    
    $.each(jsonData["jueves"], function (ind, citas) { 
	rellenarCitas(citas, "Jueves");
    }); 
    
    $.each(jsonData["viernes"], function (ind, citas) { 
	rellenarCitas(citas, "Viernes");
    }); 
}

function rellenarCitas(cita, dia) {
    /*Método encargado de calcular los bloques de cada cita y asignarle el nombre en el div correspondiente a la hora.*/
    var hora_inicio = new Date("August 15, 1977 " + cita.hora_inicio + ":00"); // Wow!
    var hora_fin = new Date("August 15, 1977 " + cita.hora_termino + ":00"); // Wow!
    
    var intervaloMinutos = (((hora_fin - hora_inicio) / 1000) / 60);
    var bloques = intervaloMinutos / 30;
    var indexHora = horas.indexOf(cita.hora_inicio);
    
    
    for(var n = indexHora ; n < indexHora + bloques ; n++ ) {
	var id = "#" + horas[n].replace(':', '') + dia;
	$(id).append(cita.nombre);
	$(id).css("background-color", "#b0f3ef");
    }
    
}

function crearDivs(jsonData) {
    /*Método encargao de crear los divs asignadole un id único.*/
    var dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];
    
    $(".columna_hora").each(function (index) {
	var columna = $(this)
	horas.some(function(element, index, array) {
	    columna.append("<div class=\"bloque\">" + element +"</div>");
	});
    });
    
    $(".columna_dia").each(function (indexColumna) {
	var columna = $(this)
	var dia = dias[indexColumna]

	columna.append("<div class=\"cabecera\">" + dia +"</div>");
	horas.some(function(element, index, array) {
	    if(index != 0) {
		if(index < horas.length-1) {
		    columna.append("<div id=\"" + element.replace(':', '') + dia + "\" class=\"bloque\"> </div>");
		}
	    }
	});
    });
}


