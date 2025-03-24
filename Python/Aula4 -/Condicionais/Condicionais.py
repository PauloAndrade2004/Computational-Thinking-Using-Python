
idade_input = input('Qual a sua idade?')

if idade_input.isdigit():
    idade = int(idade_input)

    if idade > 17:
        print('Pode entrar sozinho (a)')
    else:
        responsavel = input('Acompanhado de responsável? Sim (S) ou Não (N)')
        if responsavel.lower() in ['s', 'n']:
            if responsavel.lower() == 's':
                print('Pode entrar acompanhado (a)')
            else:
                print('Não pode entrar!')
        else:
            print('Resposta incorreta!')

else:
    print('Idade incorreta!')