// Problema 1 Miguel Angel Fernandez Sanchez
function showAns() {
	var operando1 = document.getElementById('operando1').value;
	var operacion = document.getElementById('operacion').value;
	var operando2 = document.getElementById('operando2').value;
	var mi_peticion = operando1 + ':' + operacion + ':' + operando2;
	if((operando1.length > 0) && (operando2.length > 0)){
		xmlhttp=new XMLHttpRequest();
		xmlhttp.open("GET","ajax/?"+ mi_peticion,true);
		xmlhttp.send();

		xmlhttp.onreadystatechange=function() {
			if (xmlhttp.readyState==4 && xmlhttp.status==200) {
				var obj = JSON.parse(xmlhttp.responseText);
				document.getElementById('ans').innerHTML = 'El valor tentativo es' + obj.resultado;
			}
		}
	}
}
