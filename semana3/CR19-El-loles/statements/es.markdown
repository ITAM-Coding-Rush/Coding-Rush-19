# Descripción

En la actualidad hay algunos hombres a los que se les conoce como _Los fifas_, pero tu amigo Serra prefiere ser conocido como _El loles_ ya que es fan de _League of Legends_. Como le gusta jugar demasiado a este juego, descubrió la fórmula matemática para saber cuántos golpes del enemigo puedes resisitir antes de morir dependiendo de la armudara que tenga tu personaje y su vida actual. Ese resultado está dado por dos fórmulas: la primera, para calcular la vida efectiva de su personaje; y la segunda, para saber cuántos golpes aguanta con esa vida efectiva.

La fórmula de la vida efectiva es: $V_e = V_i * ( \frac{100 + A_r}{100} )$. Donde $V_i$ es la vida inicial y $A_r$ es la armadura total del personaje, $V_i$ y $A_r$ siempre son numeros enteros.

La cantidad de golpes que aguanta el personaje está dado por: $Resistencia = \frac{V_e}{D_g}$. Donde $V_e$ es la vida efectiva del personaje que recibe el daño y $D_g$ es el daño del personaje que te está atacando, $D_g$ siempre es numero entero.

Serra está tan obsesionado que te pide que le ayudes a hacer un programa donde él te dirá los $N$ personajes de su equipo, su vida y su armadura. Después los $N$ personajes del equipo contrario con sus respectivos daños. Él quiere saber el número de golpes con 2 decimales que pueden soportar los $M$ personajes de su equipo contra los del equipo contra los del equipo contrario, ya que así sabe si tendrá chance de escapar.

# Entrada

Un numero $N$ que representa la cantidad de personajes de cada uno de los equipos.

$N$ tercias de líneas del equipo de Serra en el siguiente orden: nombre del personaje, vida inicial y armadura total.

$N$ parejas de líneas del equipo contrario en el siguiente orden: nombre del personaje y daño.

Un número $M$ que es la cantidad de resultados de enfrentamientos.

Finalmente $M$ parejes en el siguiente orden: nombre del personaje del equipo de Serra y nombre del personaje del equipo contrario.

# Salida

La cantidad de golpes con **dos decimales de precisión** que aguanta el personaje en cada enfrentamiento de los que te proporciona Serra, además en caso de no encuentrar un personaje en cualquiera de los equipos devolverás "Match imposible".

# Ejemplo

||examplefile
sample
||description
Dada la fórmula podemos observar que Teemo cuenta con una vida efectiva de 3250 y Zed con una vida efectiva de 1925 por lo que en el match entre Teemo y Caitlyn, Teemo solo aguanta 17.57 golpes, redondeado a dos decimales, el match Teemo Samira, Teemo aguanta 17.11 golpes de Samira. Si hacemoos lo mismo con Zed, el match Zed vs Caitlyn, Zed unicamente resiste 10.41 golpes y finalmente Zed vs Samira, Zed resiste 10.13 golpes.
||examplefile
sample2
||description
El match imposibe es debido a que Kindred es del equipo rival y no del equipo de Serra.
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
