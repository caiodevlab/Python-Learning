numero = int(input('Insira um numero: '))
numeroinicio = numero
multi = 1
while numero != 1:
    multi *= numero
    numero -= 1
print(f'{numeroinicio}! = {multi}')