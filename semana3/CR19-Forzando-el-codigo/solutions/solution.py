s = input()
n = s.count('n')
c = s.count('c')
ans = ""
for i in range(n):
    ans+="1"
for i in range(c):
    ans+="0"
print(ans)
