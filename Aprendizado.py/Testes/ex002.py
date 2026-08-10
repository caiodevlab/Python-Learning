from random import randint
numb = 0
numsecret = randint(1, 11)
tentativas = 0
while numsecret != numb:
    numb = int(input('Estou pensando em um numero de 1 a 10, qual é?: '))
    if numb != numsecret:
        tentativas += 1
        print('HAHA! voce errou, tente denovo')
print('Poxa vida...')
print(f'Tentativas {tentativas}')