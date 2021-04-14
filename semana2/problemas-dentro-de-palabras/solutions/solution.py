palabra = input()
contL = 0
contTotal = 0
for i in palabra:
  if i == "L":
    contL += 1
  if i == "A":
    contTotal += contL
print(str(contTotal))