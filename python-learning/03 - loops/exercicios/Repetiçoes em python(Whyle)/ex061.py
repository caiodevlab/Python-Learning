primeiroterm = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroterm
cont = 0
while cont != 10:
    termo += razao
    cont += 1
    print(f'{cont}° termo = {termo}')
print('FIM')