from modulo import utils
"""
    Main:
        > Se o módulo é executado diretamente ele tem um __name__ == "__main__"
        > Se o módulo for importado de outro arquivo, ele terá um __name__ igual ao nome do arquivo importado
"""

print(__name__) # __main__
print(utils.__name__) # modulo.utils

if __name__ == '__main__':  # Ou seja, se o meu arquivo estiver sendo executado diretamente(Sem importação) Então...
    ...
