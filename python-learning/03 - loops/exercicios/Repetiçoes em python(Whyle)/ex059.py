valor1 = int(input('primeiro valor: '))
valor2 = int(input('Segundo valor: '))
acao = 0
menu = ' [1]somar\n [2]multiplicar\n [3]maior\n [4]novos numeros\n [5]sair do programa'
print(menu)
acao = int(input('Oque deseja fazer:'))
while acao != 5:
    if acao == 1:
        print(valor1 + valor2)
        print(menu)
        acao = int(input('Oque deseja fazer:'))
    if acao == 2:
        print(valor1 * valor2)
        print(menu)
        acao = int(input('Oque deseja fazer:'))

    if acao == 3:
        if valor1 > valor2:
            print(f'Primeiro valor é maior {valor1}')
            print(menu)
            acao = int(input('Oque deseja fazer:'))

        else:
            print(f'Segundo valor é maior {valor2}')
            print(menu)
            acao = int(input('Oque deseja fazer:'))
    if acao == 4:
        print('Inserir novamente')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        print(menu)
        acao = int(input('Oque deseja fazer: '))
    if acao == 5:
        print('Tenha um bom dia')