# Descripción

Lorena un día estaba sola en su casa y no tenía ganas de hacer tarea, ni quehacer, ni nada. Encontró un libro con sopas de letras para
pasar el rato. Se le ocurrió la idea de contar cuántas palabras (aunque no tengan sentido) inician con L y terminan con A (escogió esas
letras por su nombre) dentro de otra palabra. Por ejemplo, su nombre solo tiene 1 sub-palabra que es su mismo nombre; "LATA" tiene 2
sub-palabras "LA" y "LATA".

# Entrada
Una cadena de texto escrita en mayúsculas.

# Salida
Un número entero que diga la cantidad de sub-palabras que hay en la cadena ingresada.

# Ejemplo
||input
LORENA
||output
1
||description
En este caso solo hay una sub-palabra que es la misma palabra. ||input
LATA
||output
2
||description
Esta palabra tiene dos sub-palabras que son LA y LATA
||input
LATINOAMERICA
||output
3
||description
Las tres sub-palabras son LA, LATINOA y LATINOAMERICA
||input
MALETA
||output
1
||description
La única sub-palabra es LETA
||end

<details>
	<summary>
		Revisa la 'plantilla.py'
	</summary>
	{{plantilla.py}}
</details>