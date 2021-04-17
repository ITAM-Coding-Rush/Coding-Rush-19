# Descripción

¡Yosshua ha retado Carlos a un juego de memoria! Él le va a dar a Carlos una lista con muchas palabras y el reto es ver si puede recordar qué palabra está en cierta posición. Fácil, ¿no? ¡El problema es que va a hacer muchas preguntas de este tipo! Ayuda a Carlos a hacer un programa que le ayude a superar el reto.

# Entrada

En la primera línea un entero $n$, el número de palabras que debe recordar Carlos. En las siguientes $n$ líneas, las $n$ palabras de la lista (como Yosshua es programador, la primera palabra está en la posición 0). Después un número $p$, el número de preguntas que hará Yosshua. Finalmente, $p$ líneas, en cada una, la posición de la lista por la que pregunta Yosshua (se garantiza que es una posición válida).

# Salida

$p$ líneas, una por cada pregunta que hace Yosshua, conteniendo la palabra que corresponde a la pregunta
número $p$.

# Ejemplo

||examplefile
sample
||description
Tenemos la lista: crack (posición 0), bello (posición 1) y campeon (posición 2). Yosshua hace 5 preguntas. Las preguntas y su respuesta son: 0-crack, 1-bello, 2-campeon, 1-bello, 0-crack.
||end

# Límites

- $1 \leq n \leq 100000$
- $1 \leq p \leq 1000$

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
