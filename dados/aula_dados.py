import copy

from dados import produtos, pp, pcomment


novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]


print(*produtos, sep='\n')
print()
pcomment('Produtos alterados', sep='\n')
print(*novos_produtos, sep='\n')

ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse = True
)
pcomment('Ordenados por Nome [deepcopy]', sep='\n')
print(*ordenados_por_nome, sep='\n')

ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)
pcomment('Ordenados por Preco [deepcopy]', sep='\n')
print(*ordenados_por_preco, sep='\n')
