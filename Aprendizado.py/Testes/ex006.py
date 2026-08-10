a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = True
termo_atual = a1 + r
while c:
    termo_atual = termo_atual + r
    c += 1
    if c == 10:
        c = False
    maisterm = str(input('Deseja mostrar mais termos?:'))