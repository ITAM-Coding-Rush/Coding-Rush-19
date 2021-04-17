import random
import os
import string 
baseString = """
{N}
{A}
{M}
{B}
""".strip(' \t\n\r')

casos = 10

for i in range(casos):
    MAXN = 100000 // ((casos - i))
    n = random.randint(1, MAXN)
    p = random.randint(1, 1000)
    A = [ ''.join(random.choice(string.ascii_lowercase) for i in range(10)) for j in range (n)]
    B = [random.randint(0, n-1) for i in range(p)]

    case = {
        'N': str(n),
        'A': "\n".join(str(x) for x in A),
        'M': str(p),
        'B': "\n".join(str(x) for x in B)
    }
    caseName = "{}.in".format(i)
    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
