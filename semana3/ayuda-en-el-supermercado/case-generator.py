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
    MAXN = 1000 // ((casos - i))
    n = random.randint(1, MAXN)
    m = random.randint(1, n-1)
    A = [ ''.join(random.choice(string.ascii_lowercase) for i in range(10)) for j in range (n)]
    indxes = set()
    B = []
    while len(indxes) < m:
        indxes.add(random.randint(0, n-1))
    for x in indxes:
        B.append(A[x])
    
    case = {
        'N': str(n),
        'A': "\n".join(str(x) for x in A),
        'M': str(m),
        'B': "\n".join(str(x) for x in B)
    }
    caseName = "{}.in".format(i)
    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
