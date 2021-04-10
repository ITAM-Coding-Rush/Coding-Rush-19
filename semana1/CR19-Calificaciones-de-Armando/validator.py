#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import sys


def _main():
  # puedes guardar cualquier cosa que te ayude a evaluar la
  # en "data.out".
  with open('data.out', 'r') as f:
    salida_correcta = float(f.read().strip())

  score = 0
  try:
    # Lee la salida del concursante
    salida_concursante = float(input().strip())

    # Determina si la salida es incorrecta
    if abs(salida_concursante - salida_correcta) >= 0.001:
      # Cualquier cosa que imprimas a sys.stderr se ignora, pero es útil
      # para depurar.
      print('Salida incorrecta', file=sys.stderr)
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
