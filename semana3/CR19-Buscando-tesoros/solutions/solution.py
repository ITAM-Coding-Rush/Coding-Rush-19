n = int(input())

for i in range(n):
  lin = input()
  tesoro = False
  for e in (lin):
    if e == "X":
      tesoro = True
  if tesoro == True:
      print("SI")
  else:
      print("NO")