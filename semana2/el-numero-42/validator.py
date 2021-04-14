#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import sys
import math


def _main():
  # lee "data.in" para obtener la entrada original.
  with open('data.in', 'r') as f:
    s = f.read().strip()

  score = 0
  try:
    # Lee la salida del concursante
    suma = input().strip()
    prod = input().strip()

    if len(suma) != 4 or sum([ord(c) - ord('A') + 1 for c in suma]) != 42:
        print('La cadena suma está mal', file=sys.stderr)
        return
    
    if len(prod) != 2 or math.prod([ord(c) - ord('A') + 1 for c in prod]) != 42:
        print('La cadena producto está mal', file=sys.stderr)
        return 

    t = suma + prod
    t = sorted(t)
    s = sorted(s)

    for _ in range(7):
      if len(t) > 0 and s[len(s)-1] == t[len(t)-1]:
        t.pop()
      s.pop()

    if len(t) > 0:
        print('Los caracteres que usaste no coinciden', file=sys.stderr)
        return

    # Si la ejecución llega hasta aquí, la salida del concursante
    # es correcta.
    score = 1
  except:
    logging.exception('Error leyendo la salida del concursante')
  finally:
    print(score)


if __name__ == '__main__':
  _main()
