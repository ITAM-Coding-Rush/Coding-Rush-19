s = input().strip()
arr = [ord(c) - ord('A') + 1 for c in s]
n = len(s)
printed = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if printed:
                    break
                if arr[i] + arr[j] + arr[k] + arr[l] == 42:
                    printed = True
                    print(s[i] + s[j] + s[k] + s[l])

printed = False
for i in range(n):
    for j in range(n):
        if printed:
            break
        if arr[i] * arr[j] == 42:
            printed = True
            print(s[i] + s[j])
