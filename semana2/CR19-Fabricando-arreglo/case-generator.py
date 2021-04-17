import random
import os

baseString = """
{N}
{A}
{B}
""".strip(' \t\n\r')

casos = 10

for i in range(casos):
    MAXN = 100000 // ((casos - i))
    MAX_X = MAXN // ((casos - i))

    n = random.randint(1, MAXN)

    A = [random.randint(0, MAX_X) for _ in range(n)]
    B = [random.randint(0, MAX_X) for _ in range(n)]

    case = {
        'N': str(n),
        'A': "\n".join(str(x) for x in A),
        'B': "\n".join(str(x) for x in B)
    }
    caseName = "{}.in".format(i)
    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
