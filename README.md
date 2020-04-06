# Tarea Flask

* La página principal debe mostrar una página donde ponga vuestro nombre y una lista de enlaces a las diferentes páginas (para probar como funcionan). Cada una de las páginas deberá tener un enlace a la página principal.
* Página potencia: Se accede con la URL /potencia/base/exponente (siendo base y exponente dos números enteros). Se muestra una página dinámica donde se muestra un título "Calcular potencia", se muestra la base y el exponente y se muestra el resultado:
	Si el exponente es positivo, el resultado es la potencia.
	Si el exponente es 0, el resultado es 1.
	Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo.
* Página cuenta letras: Se accede con la URL /cuenta/palabra/letra (siendo palabra y letra dos cadenas cualquiera). Si la letra no es una cadena con un carácter se devuelve un error 404. Se muestra una página donde hay un título "Cuanta letras", y muestra el siguiente mensaje "En la palabra ********* aparece *** veces el carácter ***".
* Página libros: A esta página se entra con la URL /libro/codigo (siendo código un número entero). Tienes que buscar el código en el fichero libros.xml y debes mostrar una página con un título "Biblioteca" y el nombre del libro y el autor. Si no existe el código debe devolver una respuesta 404.
