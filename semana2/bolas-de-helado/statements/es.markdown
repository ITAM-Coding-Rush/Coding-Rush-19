# Descripción

Andrea ama el helado y el pasado 12 de abril (día internacional del helado) hizo una fiesta de helados con sus amigos. Como la fiesta fue
con sana distanica Andrea tuvo que preguntar a sus amigos cuántas bolas de helado querían con anticipación. 
Haz un programa que reciba el número de amigos que Andrea invitará a su casa seguido de la cantidad de bolas de helado que quieren (solo pueden entre 0-10 bolas de helado)
Regresa la cantidad de personas que quieren una bola, dos bolas... y así sucesivamente para que Andrea sepan cuánto helado comprar.
# Entrada

Un número entero que respresenta los $n$ amigos de Andre. Seguido de $n$ enteros (de 0 a 10) que representan las bolas de helado que quiere cada amigo.

# Salida

Por cada número de bolas de helado debes imprimir una línea que indique el número de veces que se pidió esa cantidad de bolas. Mira la salida de ejemplo para más detalles.

# Ejemplo

||input
3
4
5
2         
||output
0 scoops: 0
1 scoops: 0
2 scoops: 1
3 scoops: 0
4 scoops: 1
5 scoops: 1
6 scoops: 0
7 scoops: 0
8 scoops: 0
9 scoops: 0
10 scoops: 0
||input
15
1
5
7
8
6
9
1
0
3
4
7
5
6
2
10       
||output
0 scoops: 1
1 scoops: 2
2 scoops: 1
3 scoops: 1
4 scoops: 1
5 scoops: 2
6 scoops: 2
7 scoops: 2
8 scoops: 1
9 scoops: 1
10 scoops: 1
||end
<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>