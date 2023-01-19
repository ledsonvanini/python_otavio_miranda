import os

perguntas = [
    
        {
            'pergunta':'Quem é o rei do futebol?',
            'opcoes': ['Diego','Pele', 'Maradona', 'Neymar'],
            'resposta': 'Pele',
        },
        {
            'pergunta':'Quanto é 5 * 5?',
            'opcoes': ['25','55', '10', '51'],
            'resposta': '25',
        },
        {
            'pergunta':'Quem é esse Pokemon?',
            'opcoes': ['Xuxa','Garurumon', 'Blastoise', 'Pikachu'],
            'resposta': 'Pikachu',
        },
    ]
    
qtd_acertos = 0
for pergunta in perguntas:
    perguntas = pergunta['pergunta']
    print(perguntas)
    print()

    opcoes = pergunta['opcoes']
    qtd_opcoes = len(opcoes)

    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    acertou = False
    escolha = input('Escolha uma opção: ')
    escolha_int = None

    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['resposta']:
                acertou = True
    print('****************************')
    if acertou:
        qtd_acertos += 1
        print('Acertou 💪')
    else:
        print('Errooou! 🎅')
    os.system('cls')

    print(f'Você acertou {qtd_acertos} de {len(pergunta)}')
    
    
    