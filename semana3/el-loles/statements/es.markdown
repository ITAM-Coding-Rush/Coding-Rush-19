# Descripción
En la actualidad hay algunos hombres a los que se les conoce como _Los fifas_, pero tu amigo Serra prefiere ser conocido como _El loles_ ya que es fan de _League of Legends_. Como le gusta jugar demasiado a este juego, descubrió la fórmula matemática para saber cuántos golpes del enemigo puedes resisitir antes de morir dependiendo de la armudara que tenga tu personaje y su vida actual. Ese resultado está dado por dos fórmulas: la primera, para calcular la vida efectiva de su personaje; y la segunda, para saber cuántos golpes aguanta con esa vida efectiva.

La fórmula de la vida efectiva es: **Ve = Vi * ( (100 + Ar) / 100 )**. Donde Vi es la vida inicial y Ar es la armadura total del personaje, Vi y Ar siempre son numeros enteros.

La cantidad de golpes que aguanta el personaje está dado por: __Resistencia = Ve / Dg__. Donde Ve es la vida efectiva del personaje que recibe el daño y Dg es el daño del personaje que te está atacando, Dg siempre es numero entero.

Serra está tan obsesionado que te pide que le ayudes a hacer un programa donde él te dirá los __N__ personajes de su equipo, su vida y su armadura. Después los __N__ personajes del equipo contrario con sus respectivos daños. Él quiere saber el número de golpes con 2 decimales que pueden soportar los __M__ personajes de su equipo contra los del equipo contra los del equipo contrario, ya que así sabe si tendrá chance de escapar.

# Entrada

Un numero N que representa la cantidad de personajes de cada uno de los equipos.

N tercias de líneas del equipo de Serra en el siguiente orden: nombre del personaje, vida inicial y armadura total.

N parejas de líneas del equipo contrario en el siguiente orden: nombre del personaje y daño.

Un número M que es la cantidad de resultados de enfrentamientos.

Finalmente M parejes en el siguiente orden: nombre del personaje del equipo de Serra y nombre del personaje del equipo contrario.

# Salida

La cantidad de golpes con dos decimales que aguanta el personaje en cada enfrentamiento de los que te proporciona Serra, además en caso de no encuentrar un personaje en cualquiera de los equipos devolverás "Match imposible".


# Ejemplo


Entrada  |  Salida | Descripción
---------|---------|----------------
2        |  17.57           | Dada la fórmula podemos observar que Teemo cuenta con una vida efectiva de 3250 y Zed con una vida efectiva de 1925 por lo que en el match entre Teemo y Caitlyn, Teemo solo aguanta 17.57 golpes, redondeado a dos decimales, el match Teemo Samira, Teemo aguanta 17.11 golpes de Samira. Si hacemoos lo mismo con Zed, el match Zed vs Caitlyn, Zed unicamente resiste 10.41 golpes y finalmente Zed vs Samira, Zed resiste 10.13 golpes.
Teemo    |  17.11           | 
1300     |  10.41           |
150      |  10.13           |
Zed      |                  | 
1100     |                  |
75       |                  |
Caitlyn  |                  |
185      |                  | 
Samira   |                  |
190      |                  |
4        |                  |
Teemo    |                  |
Caitlyn  |                  | 
Teemo    |                  |
Samira   |                  |
Zed      |                  |
Caitlyn  |                  | 
Zed      |                  |
Samira   |                  |
---------|------------------|-----------------
4        |  40.0            | El match imposibe es debido a que Kindred es del equipo rival y no del equipo de Serra
Volibear |  Match imposible |
1800     |  22.4            |
300      |                  |
Udyr     |                  |
2000     |                  |
180      |                  |
Warwick  |                  |
1950     |                  |
250      |                  |
Rell     |                  |   
1500     |                  |
280      |                  |
Kindred  |                  |
220      |                  |
Ashe     |                  |
215      |                  |
Zed      |                  |
250      |                  |
Sett     |                  |
180      |                  |
3        |                  |
Volibear |                  |
Sett     |                  |
Kindred  |                  |
Warwick  |                  |
Udyr     |                  |
Zed      |                  |

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>