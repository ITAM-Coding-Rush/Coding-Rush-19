mensaje = input()
doses = 0

for c in mensaje: 
    if c == '2':
        doses=doses+1
        
if doses < 3:
    print("Pau no tiene las uñas arregladas")
else:
    print("Pau tiene las uñas arregladas")