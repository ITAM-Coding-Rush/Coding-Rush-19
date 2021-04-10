n = int(input())

arr = [(int(input()), int(input())) for _ in range(n)]

d2 = [x ** 2 + y ** 2 for (x,y) in arr]

menor_id = d2.index(min(d2))
mayor_id = d2.index(max(d2))

x1, y1 = arr[menor_id]
x2, y2 = arr[mayor_id]

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
t = d / 30.0

print(round(t, 6))