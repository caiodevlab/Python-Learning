primeiroterm = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroterm
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{cont}° termo = {termo}')
        termo += razao
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais? (Digite 0 para sair): '))

print(f'FIM! Progressão finalizada com {total} termos mostrados.')
