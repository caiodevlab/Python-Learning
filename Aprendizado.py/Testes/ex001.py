cadastro = ''
while cadastro != 'M' and cadastro != 'F':
    cadastro = str(input('SexoM/F: ')).upper()
    if cadastro != 'M' and cadastro != 'F':
        print('Valor invalido, poderia inseir novamente?')
print('Obrigado')