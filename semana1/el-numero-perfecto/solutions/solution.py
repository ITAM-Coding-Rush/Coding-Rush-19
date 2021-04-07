# Leer el número entero
n = int(input())

# Acumularemos la suma de los divisores, entonces la inicializo en 0
sumadiv = 1

# Iteraremos checando si son divisores
tope = min (n, int(n ** 0.5) + 1)
for i in range(2, tope):
    # ¿Cómo se si i es divisor de n?
    if n % i == 0:
        sumadiv += i
        if n > i * i:
            sumadiv += n / i

# Checamos si n cumple la condición de ser número perfecto
if n > 1 and n == sumadiv:
    print("Es perfecto")
else:
    print("No es perfecto")