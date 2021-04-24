codigos = {}

for i in range(4):
    jugador = input()
    clave = input()
    codigos[clave] = jugador

for i in range(2):
    numero = input()
    if numero in codigos:
        print(codigos[numero])
    else:
        print("Juanito Lo Hizo de Nuevo")