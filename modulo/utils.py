from os import system
import pprint
def pp(valor):
    pprint.pprint(valor, indent=2, width=80)

def pl():
    print (f"{25 * '-*'}")


def pcomment(arg, sep='\n'):
    print(f'\n{pl()}{ arg }{pl()}', sep)


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def cls():
    system('cls')