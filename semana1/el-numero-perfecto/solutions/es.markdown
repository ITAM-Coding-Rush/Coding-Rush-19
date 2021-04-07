# El número perfecto - Solución

Para obtener 90 puntos, basta con hacer un _for_ de $1$ a $n-1$ buscando los divisores de $n$. Si un número es divisor de $n$, lo añadimos a una variable que tenga la suma de todos los divisores.

Ahora bien, hacer un _for_ hasta $n-1$ es muy tardado y dará _Time limit exceeded (TLE)_ para los otros 10 puntos. Para obtenerlos, hay que darnos cuenta que si $x$ divide a $n$, entonces $n / x$ también divide a $n$. Es decir, los divisores vienen en "parejas". Por ejemplo, para $28$, sus divisores son 1 y 28, 2 y 14, y 4 y 7. 

Una vez notado esto, podemos ver que si juntamos en parejas de divisores, el número más chico en la pareja es menor o igual a la raíz de $n$. Así, podemos reducir el _for_ hasta la raíz de $n$, en lugar de hasta $n$. Esto es una gran mejora en la complejidad del algoritmo y dará los 100 puntos.