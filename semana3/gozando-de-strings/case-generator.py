import random
import os

baseString = """
{N}
{cadenas}
""".strip(' \t\n\r')

casos = 10

for i in range(2, casos):
    N = 100

    cadenas = ["".join([str(random.randint(0, 1)) for _ in range(random.randint(1, 1000))]) for _ in range(N)]

    case = {
        'N': str(N),
        'cadenas': "\n".join(x for x in cadenas),
    }
    caseName = "{}.in".format(i)
    caseString = baseString.format(**case) + "\n"
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
