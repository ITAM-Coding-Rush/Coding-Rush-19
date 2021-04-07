# Descripción

Sebastián tienen una afición sobrehumana con los números. En particular, le apasionan los _números perfectos_.

Un número perfecto es aquél en el que la suma de sus divisores positivos (sin incluirse a sí mismo) da como resultado el mismo número. Por ejemplo, el número $28$ es un número perfecto, pues $28 = 1 + 2 + 4 + 7 + 14$.

Dada la existencia de tantos números y el tiempo limitado de Sebastián (también llamado _flojera_), necesita un programa que al ingresar un número entero positivo y le indique si es o no un número perfecto.

# Entrada

Un entero positivo $n$.

# Salida

Deberás imprimir (sin comillas) "Es perfecto" si $n$ es un número perfecto o "No es perfecto" en caso contrario.

# Ejemplo

||examplefile
sample
||examplefile
sample2
||end

# Límites

- $1 \leq n \leq 10^10$

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>

<details><summary>Hint</summary>
Recordar que `n % x` te da el residuo de dividir `n` entre `x`.
</details>
