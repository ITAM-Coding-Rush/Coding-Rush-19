palabra = input()
letraInicial = input()
letraContar = input()
cont = 0

if palabra[0] == letraInicial:
  for i in range(1, len(palabra)):
    if palabra[i] == letraContar:
      cont += 1

print(cont)