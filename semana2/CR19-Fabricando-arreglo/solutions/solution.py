n = int(input())
A = [int(input()) for _ in range(n)]
B = [int(input()) for _ in range(n)]

MAX_ELEMENT = max (max(A), max(B)) + 2
bucketA = [0] * MAX_ELEMENT
bucketTot = [0] * MAX_ELEMENT

for i in range(n):
    bucketA[A[i]] += 1
    bucketTot[A[i]] += 1
    bucketTot[B[i]] += 1

cnt = n
i = MAX_ELEMENT - 1
S = 0
k = 0
while cnt > 0:
    if bucketTot[i] > 0:
        S += i
        if bucketA[i] > 0:
            bucketA[i] -= 1 # Usamos uno de A
        else:
            k += 1      # Usamos uno de B entonces usamos un swap
        bucketTot[i] -= 1
        cnt -= 1
    else:
        i -= 1

print(S)
print(k)