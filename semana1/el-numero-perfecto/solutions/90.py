n = int(input())
if n == 0:
    print("No es perfecto")
else:
    if n < 0:
        n = - n
    sumadiv = 0
    for i in range(1, n):
        if n % i == 0:
            sumadiv += i
    if n == sumadiv:
        print("Es perfecto")
    else:
        print("No es perfecto")
