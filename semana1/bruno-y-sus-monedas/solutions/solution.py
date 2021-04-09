total = 0

monedas = int(input())

for i in range(monedas):
  denominacion = int(input())
  cantidad = int(input()) 
  total += denominacion * cantidad

print(str(total))