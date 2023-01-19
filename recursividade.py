"""
    RECURSIVIDADE
        > É um programa que chama a si próprio até uma condição ser satisfeita
        > Existe um limite em Python, podendo causar Stackoverflow "getrecursionlimit()"
        > Limite de recursões pode ser ajustado com "setrecursionlimit()"
"""
import sys
from sys import getrecursionlimit
print(getrecursionlimit())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(f'Fatorial: {factorial(5)}')
print(f'Fatorial: {factorial(4)}')
print(f'Fatorial: {factorial(7)}')

