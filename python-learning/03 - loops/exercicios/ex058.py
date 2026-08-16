import random
comput = 0
conter = 0
player = 1
while comput != player:
    conter += 1
    comput = random.randint(1,10)
    print(comput)
    print('Pensei em um numero, qual é')
    player = int(input('O numero é: '))
    if comput != player:
        print('HAHA tente denovo!')
    if comput == player:
        print('Poxa vida')
print(f'Foram nedcessárias {conter} vezes')
