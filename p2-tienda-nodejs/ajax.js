function showResult() {
	var op1 = document.getElementById('op1').value;
	var op = document.getElementById('op').value;
	var op2 = document.getElementById('op2').value;
	var peticion = op1 + ':' + op + ':' + op2;
	if((op1.length > 0) && (op2.length > 0)){

		xmlhttp=new XMLHttpRequest();
		xmlhttp.open("GET","ajax/?"+peticion,true); //?2:opcion:2
		xmlhttp.send();

		// La respuesta que se recibe
		xmlhttp.onreadystatechange=function() {
			if (xmlhttp.readyState==4 && xmlhttp.status==200) {
				var obj = JSON.parse(xmlhttp.responseText);
				document.getElementById('resultado').innerHTML = 'AJAX Result ' + obj.resultado;
			}
		}

	}
}
