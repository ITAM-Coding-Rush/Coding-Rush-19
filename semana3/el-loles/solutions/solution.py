n = int(input())

vidas_efectivas_equipo_Serra = {}
damage_equipo_rival = {}

for i in range(n):
    personaje = input()
    vida_inicial = int(input())
    armadura_total = int(input())

    vida_efectiva = vida_inicial * ((100 + armadura_total) / 100)

    vidas_efectivas_equipo_Serra[personaje] = vida_efectiva

for i in range(n):
    personaje_rival = input()
    damge = int(input())

    damage_equipo_rival[personaje_rival] = damge

m = int(input())

for i in range(m):
    personaje_Serra = input()
    personaje_rival = input()

    if personaje_Serra in vidas_efectivas_equipo_Serra:
        if personaje_rival in damage_equipo_rival:
            resistencia = vidas_efectivas_equipo_Serra[personaje_Serra] / damage_equipo_rival[personaje_rival]
            print(round(resistencia, 2))
        else:
            print("Match imposible")
    else:
        print("Match imposible")