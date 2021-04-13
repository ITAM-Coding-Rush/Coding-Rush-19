import random
import os

random.seed(1)

baseString = """
{S}
""".strip(' \t\n\r')

div42 = [2, 3, 6]
casos = 10
for i in range(casos):
    S = ""
    a = div42[i % len(div42)]
    b = 42 // a
    S += chr(a + ord('A') - 1) + chr(b + ord('A') - 1)

    # Elegimos 4 que sumen 42
    cnt = 42
    for j in range(4):
        menor = min(26, max(1, cnt - (3 - j) * 26))
        mayor = min(26, max(1, cnt - (3 - j)))
        letra = random.randint(menor, mayor)
        cnt -= letra
        S += chr(letra + ord('A') - 1)

    # Añadimos una letra al azar
    S += chr(random.randint(ord('A'), ord('Z')))
    S = ''.join(random.sample(S, len(S))) # Desordenamos
    S += '\n'

    case = {'S': S}
    caseName = "{}.in".format(i)
    caseString = baseString.format(**case)
    casePath = os.path.join('cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString)
