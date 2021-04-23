n = int(input())
lista = {}
for i in range(n):
  articulo = input()
  lista[articulo] = 0
m = int(input())
for i in range(m):
  articulo = input()
  lista[articulo] = 1
for articulo in lista:
  if lista[articulo] == 0:
    print(articulo)