function setCookie(cname,cvalue){
	// cname es el nombre de la cookie que ponemos en los html, y cvalue el valor que le damos
	var d = new Date();
	// Numero de dias hasta que expira la cookie desde la fecha actual
	var exdays = 30;
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	var expires = "expires=" + d.toGMTString();
	// JavaScript puede crear, leer y borrar las cookies con la propiedad document.cookie
	// Creamos la cookie:
	document.cookie = cname + "=" + cvalue + "; " + expires;
	addCart(cvalue);
}


function getCookie(cname){
	// Toma el nombre de la cookie como parametro (cname)
	// Creamos una variable (name) con el texto que se desea buscar (cname + “=”)
	var name = cname + "=";
	// Usamos document.cookie.split para encontrar un punto y coma en la matriz ca (ca = document.cookie.split (‘;’))
	var ca = document.cookie.split(';');
	// Recorremos en un bucle la matriz y lee cada valor. 
	// Si encuentra la clave y valor correspondientes (c.indexOf(name) == 0), devuelve la cookie, y si no es asi devuelve la cadena sin nada.
	for(i=0; i<ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') {// Si hay un espacio se elimina
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {//Si se encuentra la cookie se devuelve
			return c.substring(name.length, c.length);
		}
	}
	return "";
}


function printCookies(){
	// Imprimimos el contenido de la cookie
	document.getElementById('cookies').innerHTML = document.cookie;
}	


function deleteCookie(cname){
	// Borramos la cookie
	document.cookie = cname + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT';
}


function addCart(cvalue){
	var contenido;
	if(cvalue == 'ElLaberintoDeLaRosa'){
		contenido = 'Libro El laberinto de la rosa';
	}else if(cvalue == 'ElNombreDelViento') {
		contenido = 'Libro El nombre del viento';
	}else if(cvalue == 'LosJuegosDelHambre'){
		contenido = 'Libro los juegos del hambre';
	}else if(cvalue == 'MajorLazer') {
		contenido = 'Disco de Major Lazer';
	}else if(cvalue == 'AlanWalker'){
		contenido = 'Disco (single) de Alan Walker';
	}else if(cvalue == 'Tal') {
		contenido = 'Disco de Tal';
	}else if(cvalue == 'Alma'){
		contenido = 'Bici Orbea Alma';
	}else if(cvalue == 'Grow') {
		contenido = 'Bici Orbea Grow';
	}else if(cvalue == 'Orca'){
		contenido = 'Bici Orbea Orca';
	}
	document.getElementById('carrito').innerHTML = 'Has añadido ' + contenido + ' al carrito.'
}

