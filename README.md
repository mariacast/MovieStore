Aplicación Drud Movie Store, la cual se desarrollo mediante el framework Django y
para el manejo de las API se implemento rest_framework de Django tambien.

Adjunto se encontraran los siguientes archivos
-Archivo dbdrudmovie.sql con una base de prueba que se utilizo durante el desarrollo.
-Archivo DrudMovieStore.postman_collection.json con la colección de las url de las API
con su respectivo ejemplo.
-Archivo requirements.txt con los paquetes que se usaron en el entorno virtual para que
corriera la aplicación.

La URL para acceder al login es : http://127.0.0.1:8000/login/
Usuario existente creado en la base de datos adjunta
User= admin
Pass = admin12345
O acceder a la URL http://127.0.0.1:8000/RegistrarUsuario/ para crear un usuario nuevo,
una vez logueado se redireccionara a la lista de peliculas donde se podra buscar, editar,
eliminar y agregar una nueva.
En la barra superior podra ver el nombre de usuario y el cierre de la sesión
En el menu lateral izquierdo esta el panel para acceder al modulo de usuarios para
ver el listado, editarlos o agregar uno nuevo.
