var http = require('http');
var url = require('url');
var fs = require('fs');
var mime_types = {
	'js' : 'text/javascript',
	'html' : 'text/html',
	'css' : 'text/css',
	'jpg' : 'image/jpg',
	'json' : 'application/json',
	'mp3' : 'audio/mpeg'
};
var resultado;
var my_datos = [];

http.createServer(function(request, response){
	var pathname; // el nombre del archivo que se va a enviar
	var pathname_req = url.parse(request.url).pathname; // Sacamos el nombre del achivo que se esta solicitando
	if (["/", "/formulario"].indexOf(pathname_req) !== -1) {
		pathname = "/index.html"
	}else{
		pathname = pathname_req;
	}

	var ruta_a_archivo = 'contenido/' + pathname; //ruta del archivo que se va a enviar
	var body = [];
	var headers = request.headers;
	var identificado = false;  // se ha identificado al usuario (mediante las coockies que se mandan)

	request.on('error', function(err) {
		console.error(err);
	}).on('data', function(chunk) {
		body.push(chunk);
	}).on('end', function() {
		body = Buffer.concat(body).toString();

		console.log("=======")
		console.log("Me llega esta peticion: " + url.parse(request.url).pathname)
		console.log("Envio esto: " + pathname);
		console.log("Este es el cuerpo de la peticion: " +body)


		if (pathname == '/ajax/'){ //Se recibe cuando se introducen numeros en ambos campos en el html

			var query = url.parse(request.url).query; //query + ?
			peticion = query.split(':');

			var my_var1 = peticion[0];
			var my_var = peticion[1];
			var my_var2 = peticion[2];
			// console.log(my_var1 + ' ' + my_var + ' ' + my_var2);

			if (my_var=='opcion1'){
				resultado = parseInt(my_var1) + parseInt(my_var2);
			}else if(my_var=='opcion2'){
				resultado = parseInt(my_var1) - parseInt(my_var2);
			}else if(my_var=='opcion3'){
				resultado = parseInt(my_var1) * parseInt(my_var2);
			}else if(my_var=='opcion4'){
				resultado = parseInt(my_var1) / parseInt(my_var2);
			}
			var obj = JSON.parse('{"resultado":""}');
			obj.resultado=resultado;

			// console.log('	RESPUESTA AJAX: ' + JSON.stringify(obj) + '\n');
			response.writeHead(200, 'text/plain');
			var responseBodyJson = JSON.stringify(obj);
			response.end(responseBodyJson);

		}else{
			if (body.length > 0){ //Viene el formulario relleno con el metodo post,
				var str = body.split('&');
				var id = makeid();
				for (i = 0; i < str.length; i++) {
					var campo = str[i].split('=');
					if (campo[0]=='campo1'){
						var my_var1 = campo[1];
					}else if(campo[0]=='opcion'){
						var my_var = campo[1];
					}else if(campo[0]=='campo2'){
						var my_var2 = campo[1];
					}
				}
				var new_opcion = new nuevaOp(id,my_var1,my_var,my_var2,resultado);
				my_datos.push(new_opcion);
				for (i = 0; i < my_datos.length; i++){
					if(my_datos[i].id == id){
						// JSON.stringify(my_datos[i]));
					}
				}

			}

			// Enviar los archivos pedidos. Enviamos archivos salvo cuando cuando recibimos la peticion AJAX

			fs.exists(ruta_a_archivo, function(existe){
				if(existe){
					fs.readFile(ruta_a_archivo, function(error, contenido_archivo){
						if(error){
							response.writeHead(500, 'text/plain');
							response.end('Error 500. Error interno.');
							// console.log('Error 500. Error interno.');
						}else{
							var extension = ruta_a_archivo.split('.').pmy_var(); //se saca la extension (html, css, js, ...) para extraer el myme tipe del dic declarado antes
							var mime_type = mime_types[extension];

							var domain ='localhost';
							if (headers.cookie){ //Si hay cookies no es la primera vez que accede. Ir borrando las coockies de localhost para comprobar esto.

								identificado = true;

								console.log(headers.cookie)
								var cookies = headers.cookie.split(';');
								for (i = 0; i < cookies.length; i++) {
									var campo = cookies[i].split('=');
									while (campo[0].charAt(0)==' ') {// Si hay un espacio se elimina
										campo[0] = campo[0].substring(1);
									}
									if (campo[0] == 'username'){
										username = campo[1];
									}
								}

								// console.log('CLIENTE IDENTIFICADO: ' + username);
							}else{
								var username = makeid();
								// console.log('NUEVO CLIENTE: ' + username);
							}
							var set_cookie = 'username=' + username + '; domain=' + domain + '; path=/;';
							var res_headers = {'Content-Type': mime_type, 'Set-Cookie': set_cookie}; // IMPORTANTE: Las cabeceras van dentro de un diccionario. Esto no es del todo correcto pues el servidor envia siempre las cockies y esto no es asi.
							response.writeHead(200, res_headers);

							if (pathname == '/index.html'){ // cuando envio el index le digo si lo he idenficado o no.
								if (identificado){
									response.end('<p>Hola de nuevo ' + username + '</p>' + contenido_archivo);
								}else{
									response.end('<p>Bienvenido ' + username + '</p>' + contenido_archivo);
								}

							}else{
								response.end(contenido_archivo);
							}
						}
					});
				}else{
					response.writeHead(404, 'text/plain');
					response.end('Error 404. El enlace no existe o ha dejado de existir.');
				}
			});
		}
	});
}).listen(8080, '127.0.0.1');
// console.log('El servidor esta funcionando correctamente en http://localhost:8080/');


function makeid(){ //cinco numeros aleatorios concatenados
    var text = "";
    for( var i=0; i < 5; i++ ){
        text += Math.random()+"_";
    }
    // console.log(text)
    return text;
}

function nuevaOp(id, my_var1, my_var, my_var2, res) {
    this.id = id;
    this.campo1 = my_var1;
    this.opcion = my_var;
    this.campo2 = my_var2;
    this.resultado = res;
}
