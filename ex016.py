'''
from math import trunc
n = float(input('Digite um número: '))
nModificado = trunc(n)
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, nModificado))
'''
n = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))