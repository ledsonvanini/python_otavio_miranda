# hasattr(), dir(), getattr()

nome = 'Ledson Vanini'
method = 'upper'

if hasattr(nome, method):
    print(f'Sim, {method} existe em {nome}')
    print(getattr(nome, method)())  # Se o método procurado existir basta pegá-lo com getattr() e executá-lo com ()

# pp(dir(nome))
# print(hasattr(nome, 'count'))
# #pp(getattr(nome))
#pp(setattr(nome, pp))

