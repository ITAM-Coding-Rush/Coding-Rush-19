import random
import os

baseString = """
{N}
{arreglo}
""".strip(' \t\n\r')

casos = 10

for i in range(casos):
    MAXN = 100000 // ((casos - i) ** 4)
    MAX_X = 1e9 // ((casos - i) ** 6)
    
    n = random.randint(1, MAXN)

    arr = []
    s = []
    for j in range(n):
        x = random.randint(-MAX_X, MAX_X)
        y = random.randint(-MAX_X, MAX_X)
        while x**2 + y**2 in s:
            x = random.randint(-MAX_X, MAX_X)
            y = random.randint(-MAX_X, MAX_X)
        arr += [x, y]

    case = {
        'N': str(n),
        'arreglo': "\n".join(str(x) for x in arr)
    }
    caseName = "{}.in".format(i)
    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
