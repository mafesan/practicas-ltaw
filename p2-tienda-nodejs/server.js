// Practica tienda con NodeJS
// Miguel Angel Fernandez Sanchez
// Para arrancar server: $ nodejs server.js

var http = require('http');
var fs = require('fs');
var path = require('path');

var mime_types = {
	'.js' : 'text/javascript',
	'.html' : 'text/html',
	'.css' : 'text/css',
	'.jpg' : 'image/jpg',
	'.png' : 'image/png',
	'.jpeg' : 'image/jpeg',
	'.mp3' : 'audio/mpeg',
	'.mp4' : 'video/mp4'
};


// Creamos el servidor que escucha en el puerto 8080
var server = http.createServer(function(request, response) {
    // Mensajes de debug
    console.log("New request: " + request.url);
    // Si el pathname es / , se guarda index.html, si no se guardará el pathname que aparezca
	var pathname = '.' + ((request.url=='/') ? '/index.html' : request.url);
	var extension = path.extname(pathname);
   	var contentType = mime_types[extension];
    console.log(extension);
    console.log(pathname);
    console.log(contentType);
	// Si nos viene un GET, llamamos a la funcion showResponse
	if (request.method == "GET"){
		showResponse(pathname, contentType, request, response);
	}
}).listen(8080);

console.log('Server running at http://127.0.0.1:8080/');

function showResponse(pathname, contentType, request, response){
	// Comprobamos que la ruta del archivo exista, para ello usamos el modulo fs
	fs.exists(pathname,function(exist){
		if(exist){
			// readFile tiene 2 parámetros: 1- nombre del archivo HTML a leer (indicar todo el path)
			// y el 2 es una función anónima que tiene dos param.: si hubo error y el contenido del archivo
			fs.readFile(pathname,function(error,content){
				if(error){
					// 500: Internal Server Error
					response.statusCode = 500;
					response.setHeader('Content-Type','text/plain');
					response.write("Internal error");
					response.end();
				}else{
					// 200 OK
					response.writeHead(200,{'Content-Type': contentType});
					response.write(content);
					response.end();
				}
			});
		}else{
			// 404 not found
			response.statusCode = 404;
			response.setHeader('Content-Type','text/plain');
			response.write('Content not found');
			response.end();
		}
	});
}
