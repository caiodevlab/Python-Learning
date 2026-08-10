a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
termo_atual = a1 + r
while c < 10:
    c += 1
    termo_atual = termo_atual + r
    c += 1
    print(f'{c}termo é: {termo_atual}')
    