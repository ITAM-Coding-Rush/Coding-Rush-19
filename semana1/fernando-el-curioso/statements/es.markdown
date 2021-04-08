# Descripción

Fernando tiene localizadas varias tiendas a su alrededor donde puede ir a comprar plátanos. Se sabe que Fernando puede viajar en línea recta dadas sus habilidades de mono y que además su velocidad es constante de $30 \frac{km}{h}$.

Siendo curioso, se pregunta cuánto tiempo le tomaría llegar desde la tienda más cercana de su casa a la más lejana de su casa.

La distancia entre dos puntos $(x_1, y_1)$ y $(x_2, y_2)$ está dada por  $$\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

La casa de Fernando se encuentra en la coordenada $(0, 0)$.

# Entrada

En la primera línea, un número entero $n$ que representa el número de tiendas a su alrededor.

En las siguientes $2*n$ líneas vendrán parejas de enteros $x_i$ y $y_i$ que representa la coordenada de la $i$-ésima tienda.

# Salida

Un número decimal positivo, la distancia entre la tienda más cercana a la casa de Fernando y la más lejana.

Deberás imprimir la respuesta con 6 cifras de precisión en los decimales.

Nota: para redondear un número $x$ a seis decimales puedes usar la función `round(x, 6)`.

# Ejemplo

||examplefile
sample
||description
Hay 3 tiendas de plátanos alrededor de la casa de Fernando ubicados en las posiciones $(0, 1)$, $(0, 31)$ y $(-2, 0)$.

La tienda más cercana es la que se encuenta en la posición $(0, 1)$, con una distancia desde la casa de Fernando de $\sqrt{(0 - 0)^2 + (1 - 0)^2} = 1$.

La tienda más lejana es la que se encuentra en la posición $(0, 31)$ con una distancia de 31.

La distancia entre la tienda más cercana y la más lejana es entonces de $\sqrt{(0 - 0)^2 + (31 - 1)^2} = 2$.

Finalmente, Fernando recorrería esos 30km en exactamente 1 hora.

||examplefile
sample2
||end

# Límites

- $2 \leq n \leq 100,000$
- $-10^{9} \leq x_i, y_i \leq 10^{9}$
- Todas las tiendas estarán a una distancia distinta de la casa de Fernando.

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>