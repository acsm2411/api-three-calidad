# api-three-calidad

Este microservicio es el encargado de realizar la busqueda del role y expirationDate para un encryptedToken dado.

### Autor

[Andres Camilo Silva Morales](https://github.com/acsm2411)

### Prerrequisitos

1. Contar con [Python 3](https://www.python.org/downloads/) instalado en la computadora donde se ejecutara la API.
2. Descargar las dependencias del proyecto utilizando el siguiente comando (estando ubicado en la carpeta del proyecto):

```bash
pip3 install -r requirements.txt
```

3. [Postman](https://www.postman.com/downloads/) en caso de que se quieran realizar pruebas utilizando este software (opcional).

### ¿Como ejecutar la app local?

Ejecutar el siguiente comando:

```bash
uvicorn main:app --reload --port=<puerto>
```

Donde `<puerto>` debe ser reemplazado por un numero de puerto (Debe ser diferente para cada API para evitar colisiones).

### ¿Como probar la app localmente?

Tenemos dos posibilidades para realizar pruebas con nuestra app:

1. Utilizando Swagger

Para esto, simplemente debemos acceder a la ruta /docs de nuestra API en ejecucion y se nos mostrara la pagina de swagger con todos los endpoints listos para probar.

![image](https://user-images.githubusercontent.com/30994170/185980310-9bb1e74b-0c29-4568-9808-6dc7570a4a18.png)

2. Accediendo a los endpoints directamente

Podemos acceder directamente al endpoint correspondiende de nuestra API y escribir valores en la URL para hacer nuestras pruebas.

![image](https://user-images.githubusercontent.com/30994170/185980760-6617feec-7f65-447a-87fa-59edc950438c.png)

3. Con Postman

Para esto, debemos agregar la request con la ruta de nuestra API y enviarle el valor de path necesario:

![image](https://user-images.githubusercontent.com/30994170/185980463-6f8f478a-a9ca-4af0-be29-17d51d5927e4.png)

Algunos valores de prueba:

* f204ed512ed0bb512f20a4708f2928a288915e45
* 708f8f8e7439026a58f813c4d8ac87962f72461e
* e1355af1e0d8b4223e0a3972bf14a3421f5c407e
* b456a1e07f8d0e0dc9756d9d8fa4c63eba1eac04
* 809e17cf4eee89fba65f6e83012648eb992667fa

### ¿Como abrir la app cuando está en ejecución?

Para abrir la app luego de su ejecución, accedemos a la siguiente ruta en el navegador de preferencia:

`http://localhost:<puerto>`

Donde `<puerto>` debe ser reemplazado por el numero de puerto escogido durante el comando de ejecución o 8000 por defecto.
