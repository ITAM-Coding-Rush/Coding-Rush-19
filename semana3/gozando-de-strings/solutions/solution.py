T = int(input())

for _ in range(T):
    s = input()
    ans = len(s)
    tot_zeros = sum([c == '0' for c in s])
    tot_ones = sum([c == '1' for c in s])

    curr_zeros = 0
    curr_ones = 0
    for i in range(len(s)):
        # Hacemos un corte
        ans = min(ans, min(curr_ones, curr_zeros) + min(tot_ones - curr_ones, tot_zeros - curr_zeros))
        if s[i] == '0':
            curr_zeros += 1
        else:
            curr_ones += 1

    print(ans)