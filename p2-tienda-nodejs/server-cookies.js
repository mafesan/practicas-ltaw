// Servidor de node.js

// Queremos crear un servidor HTTP que acepte solicitudes desde un cliente web, por eso creamos:
var http = require('http');

// Usamos fs para interactuar con el sistema de ficheros.
var fs = require('fs');

// El modulo path proporciona utilidades para trabajar con ficheros y rutas de directorios
var path = require('path');

var mime_types = {
	'.js' : 'text/javascript',
	'.html' : 'text/html',
	'.css' : 'text/css',
	'.jpg' : 'image/jpg',
	'.png' : 'image/png',
	'.jpeg' : 'image/jpeg',
	'json' : 'application/json',
	'.mp3' : 'audio/mpeg',
	'.mp4' : 'video/mp4'
};

// Creamos el servidor que escucha en el puerto 8080

var server = http.createServer(function(request, response) {
    // Obligo a que si el pathname es / se guarde index.html, si no se guardará el pathname que aparezca
	var pathname = '.' + ((request.url=='/') ? '/index.html' : request.url);
	// Obtenemos la extension del archivo
	var extension = path.extname(pathname);
	// query: La parte de cualquier 'parámetro' de la cadena de consulta, o un parser de un objeto de cadena de consulta.
	//La query la podemos usar para interpretar datos de la request
	var query = request.url.search;//query + ?
	// Obtenemos el contentType en funcion de la extension del archivo
   	var contentType = mime_types[extension];
	// Cabeceras
	var headers = request.headers;
	// Cuerpo
	var body = [];
	var responseBody = 'Tu carrito contiene:\n';

	// Comprobamos errores 
	request.on('error', function(err){
		console.error(err);
	}).on('data', function(chunk){
		body.push(chunk);
	}).on('end', function(){	
		// Concatenamos el body
		body = Buffer.concat(body).toString();

		console.log('<-- Se ha recibido una petición:\n	HEADERS: ' + JSON.stringify(headers) + '\n' + '	BODY: ' + body);
		console.log('	URL RECIBIDA: ' + JSON.stringify(request.url));
		console.log('	COOKIE RECIBIDA: ' + headers.cookie);
		console.log('	QUERY RECIBIDA: ' + query + '\n');

		// Miramos si han enviado el carrito
		if (query == '?'){
			// Vamos a enviar el contenido del carrito
			responseQuery(headers, responseBody);
		}else{
			showResponse(pathname, contentType, request, response, headers);
		}
	});
}).listen(8080);


console.log('Server running at http://127.0.0.1:8080/');


function showResponse(pathname, contentType, request, response, headers){
	// Variable para saber si esta identificado el usuario
	var found = false;

	// Comprobamos que la ruta del archivo exista, para ello usamos el modulo fs
	fs.exists(pathname,function(exist){
		if(exist){
			// Si existe el archivo llamamos al método readFile para leer su contenido.
			// El método readFile tiene dos parámetros, el primero es el nombre del archivo HTML a leer (que debemos indicar siempre todo el path) 
			// y el segundo parámetro es una función anónima que tiene dos parámetros que son si hubo error y el contenido del archivo.
			fs.readFile(pathname,function(error,content){
				if(error){
					// El codigo 500 significa: Error interno del servidor
					response.statusCode = 500;
					response.setHeader('Content-Type','text/plain');
					response.write("Internal error");
					response.end();
					console.log('Error 500. Internal error');
				}else{
					// Fecha de expiracion
					var expires = expiresCookie();
					// Cookie
					var cookie = request.headers["cookie"]

					//No existe la cookie
					if (typeof(cookie) == "undefined"){
						var username = randomStr();
						var cart = JSON.stringify([]);
						// Codigo de respuesta 200 OK
						response.writeHead(200,{
        					"Set-Cookie": username + "=" + cart + ";" + expires,
        					"content-type": contentType
        				});
					}else{
						response.writeHead(200,{
        					'content-type' : contentType
        				});
					}
        			response.write(content);
        			response.end();

      				console.log("RECURSO ENVIADO!");
				}
			});
		}else{
			// Usamos un statusCode 404 porque no se encuentra la fuente
			response.statusCode = 404;
			response.setHeader('Content-Type','text/plain');
			response.write('Content not found');
			response.end();
			console.log('Error 404. Content not found.');
		}
	});
}


function responseQuery(headers, responseBody){
	// Si han enviado el carrito
	// Las cookies estan almacenadas en headers.cookie. Recortamos el string de cookies para obtener el par de valores-clave con split
	var cookies = headers.cookie.split(';');
	for (i = 0; i < cookies.length; i++){
		// Recortamos la cookie por split('=')
		var field = cookies[i].split('=');
		console.log("field " + field);
		// Si el primer caracter es un espacio se elimina
		while (field[0].charAt(0)==' '){
			field[0] = field[0].substring(1);
		}
		if (field[0] != 'username'){
			responseBody = responseBody + field[1] + ' \n'
		}
	}
	// Enviamos el contenido del carrito
	response.writeHead(200, 'text/plain');
	response.end(responseBody);
	console.log('Se ha enviado el contenido del carrito: ' + responseBody);
}


function expiresCookie(){
	var d = new Date();
	// Caduca en 30 dias
	exdays = 30;
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	var expires = d.toGMTString();
	return expires;
}


function randomStr(){
	// Generamos cadenas aleatorias de longitud 5 (identificador de usuario generado al azar)
    var text = "";
	// Posibles valores
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for( var i=0; i < 5; i++ ){
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}
