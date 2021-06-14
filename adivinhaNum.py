from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue adivinhar qual número foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador<computador:
            print('Mais...tente mais uma vez.')
        elif jogador>computador:
            print('Menos...tente mais uma vez.')
print('Analisando...'),sleep(3)                     
print('Acertou com {} tentativas. Parabéns! '.format(palpites) )        