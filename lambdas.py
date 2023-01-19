"""
    https://docs.python.org/3.11/reference/expressions.html?highlight=lambda
    https://www.w3schools.com/python/python_lambda.asp
    https://realpython.com/python-lambda/
        lambda_expr ::=  "lambda" [parameter_list] ":" expression
            > Lambda expressions (sometimes called lambda forms) are used
            to create anonymous functions. The expression lambda parameters:
            expression yields a function object. The unnamed object behaves
            like a function object defined with:
"""

usuarios = [
    {'nome': 'Ledson', 'sobrenome': 'Vanini', 'idade': '36'},
    {'nome': 'Catia', 'sobrenome': 'Cordeiro', 'idade': '42'},
    {'nome': 'Davi', 'sobrenome': 'Cordeiro', 'idade': '12'},
    {'nome': 'Zac', 'sobrenome': 'Vanini', 'idade': '3'},
    {'nome': 'Nina', 'sobrenome': 'Vanini', 'idade': '2'},
]

# def ordena(item):
#     # print(item['nome'])
#     return item['sobrenome']

# #usuarios.sort(key=ordena)
# usuarios.sort(key=lambda item: item['nome'])
# sor = sorted(usuarios, key=lambda item: item['idade'])
# print(f'Original{usuarios}')
# print()
# print(f'Sorted Copy{sor}')
# print()
# # for item in usuarios:
# #     print(item)

### AVANÇANDO COM LAMBDAS

def executa(func, *args):
    return func(*args)

def soma(x, y):
    return x + y

print(
    executa(lambda x, y: x+y, 3,5),  # Executa recebe uma Lambda expression
    executa(soma, 3,5)               # Executa recebe uma função nomeada
)

duplica = executa(
    lambda m: lambda n: m * n, 2
)
print(duplica(5))

print(
    executa(
        lambda *args: sum(args),
        1,2,5
    )
)













