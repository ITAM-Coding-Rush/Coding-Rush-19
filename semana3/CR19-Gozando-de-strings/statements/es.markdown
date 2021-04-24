# Descripción

Qaqo tiene un strings de 1s y 0s. Ella puede realizar la siguiente operación en la cadena cualquier número de veces de quiera:

- Tomar un caracter en el arreglo e invertir su valor; es decir, si el caracter era "0" lo cambia por "1" o viceversa.

Qaqo llama a la cadena _bonita_ si la cadena no contiene "101" ni "010" como **subsecuencia**. Una subsecuencia de una cadena es aquella que se puede formar si eliminamos ciertos caracteres cualesquiera de ellos. Por ejemplo, "1001" contiene "101" como subsecuencia, por lo tanto no es una cadena bonita.

Ayuda a Qaqo a saber cuál es el mínimo número de operaciones que debe hacer para hacer la cadena bonita. Qaqo tendrá que responder esto para varias cadenas.

# Entrada

En la primera línea un entero $T$, el número de cadenas que que Qaqo quiere hacer bonitas.

En cada una de las siguientes $T$ líneas vendrá una cadena binaria $s$.

# Salida

Para cada cadena, imprime el mínimo número de operaciones necesarias para hacerla una cadena bonita.

# Ejemplo

||examplefile
sample
||end

# Límites

- $1 \leq T \leq 100$
- $1 \leq |s| \leq 1,000$
