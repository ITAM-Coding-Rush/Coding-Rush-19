n = 1
for _ in range(n):
    cadena = input()
    #convertimos a valor de orden alfabetico
    valores = [ord(i)-64 for i in cadena]
    #buscamos primero las parejas que multiplican 42
    parejasMult = []
    for a in valores:
            for b in valores:
                #como 42 no es cuadrado perfecto basta con checar:
                if a*b == 42 and [a, b] not in parejasMult:
                    parejasMult.append([a, b])
    encontramosSol = False
    #por cada pareja que multiplica 42
    for a, b in parejasMult:
        #quitamos la pareja de valores temporalmente
        valores.remove(a)
        valores.remove(b)
        s = sum(valores)  # calculamos la suma de los caracteres restantes
        #como ahora valores tiene 5 caracteres, buscamos cual quitar para
        #formar la cadena de 4 caracteres que sume 42.
        for valor in valores:
            if not encontramosSol and s-valor == 42:
                valores.remove(valor)
                cadSuma = ''.join([chr(i+64) for i in valores])
                cadMult = chr(a+64)+chr(b+64)
                print(cadSuma)
                print(cadMult)
                encontramosSol = True
                break  # imprimimos solo una solucion
        valores.append(a)
        valores.append(b)
