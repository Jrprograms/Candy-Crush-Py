import random

def iniciarMatriz(matriz):
  for i in range(16):
    matriz[i] = random.randint(1,5)
  return matriz
