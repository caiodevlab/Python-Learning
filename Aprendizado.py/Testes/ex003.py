num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
acao = 0
while acao != 5:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do Programa')
    acao = int(input('Oque deseja fazer: '))
    if acao == 1:
        print(6 * '-')
        print(f'Somado = {num1 + num2}')
        print(6 * '-')
    if acao == 2:
        print(6 * '-')
        print(f'Multiplicado = {num1 * num2}')
        print(6 * '-')
    if acao == 3:
        print(6 * '-')
        if num1 > num2:
            print(f'O maior é: {num1}')
        else:
            print(f'O maior é: {num2}')
        print(6 * '-')
    if acao == 4:
        print('INSERIR NOVAMENTE')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
print('Obrigado tenha um bom dia')