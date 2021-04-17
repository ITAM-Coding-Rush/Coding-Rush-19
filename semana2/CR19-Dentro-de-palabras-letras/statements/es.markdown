# Descripción

Lorena estaba tan aburrida que no tenía ganas de hacer nada, ni siquiera su tarea. Después de pasearse por su casa un buen rato, encontró un libro con sopas de letras para hacer. Cuando acabó de resolver uno de los sopas de letras se le ocurrió crear un programa que contara la cantidad de veces que aparece una letra sí y sólo sí la palabra empieza con cierta letra.

Pero Lorena no se podía distraer de sus estudios y te pide ayuda para crear el programa.

# Entrada

La entrada consistirá de tres líneas (cada número es una línea):
1. Una cadena de texto que será la palabra a revisar.
2. Una letra que será el inicio de la palabra.
3. Una letra que será la que contaremos.

**NOTA**: Debe considerarse que la letra inicial no se cuenta aunque sea la misma que la letra a contar.

# Salida

El número de veces que aparece la letra indicada en la palabra.
# Ejemplo

||examplefile
sample
||description
La inicial que queremos es la letra 'L' y la cantidad de 'A' que hay después de la 'L' solo es una.
||examplefile
sample2
||description
No se considera la primer letra para el conteo. En este caso, después de la primer letra (que es una 'A'), sólo hay una 'A'.
||examplefile
sample3
||description
Como la palabra no inicia con la letra 'F' no contará las letras 'A'.
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>