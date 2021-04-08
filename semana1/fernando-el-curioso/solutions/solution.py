minimo = 1e9
x_min = None
y_min = None
maximo = 0
x_max = None
x_min = None
n = int(input())
for i in range(n):
    x = int(input())
    y = int(input())
    # distancia euclidiana a origen (casa de Jorge)
    distancia = ((x**2)+(y**2))**0.5
    if distancia < minimo:
        minimo = distancia
        x_min = x
        y_min = y
    if distancia > maximo:
        maximo = distancia
        x_max = x
        y_max = y

# Distancia entre puntos minimo y maximo
dist = ((x_max-x_min)**2)+((y_max-y_min)**2)
dist = dist**0.5
tiempo = dist/30  # v=d/t => t=d/v - Fernando viaja a 30km/hr
print(round(tiempo, 6))  # redondeamos a 6 cifras
