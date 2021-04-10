# Descripción

A Bruno no le gusta usar ninguna tarjeta de crédito o débito, por eso siempre trae dinero en efectivo. El problema es que tiene tantas monedas y billetes que nunca sabe cuánto dinero tiene.
Tú como gran amigo que eres, decides ayudarle y le dices que vas a crearle un programa que te diga cuánto dinero tiene a partir de la cantidad de billetes y monedas que tenga de cada denominación.

# Entrada

Un número entero $n$ que indique cuántas monedas y billetes tiene Bruno. Posteriormente $n$ pares de números. El primer número del par es la denominación de la moneda o billete y el segundo número es la cantidad que tienes de esa moneda o billete.

# Salida

Imprimirás el total de dinero que tiene Bruno.

||input
4
5
3
10
1
2
10
1
1
||output
46
||description
Meteremos 4 pares de números.
Tenemos 3 monedas de $5, 1 moneda de $10, 10 monedas de $2 y 1 moneda de $1.
Por lo que se tiene en total $46.
||end

# Límites

$1 \leq monedas \leq 100$

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>