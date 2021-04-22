n = int(input())

mapas = [""]*n

for i in range(n):
  mapas[i] = input()

mapa = input()

m = 0
while m < n and  mapas[m] != mapa:
  m+=1

if m < n:
  print("Brandon Gana")
else:
  print("Josepe gana")