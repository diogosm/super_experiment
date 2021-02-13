import random
import math

'''
    Implementacao do z-score
    @input:
        numbers => numeros a serem avaliados para fusao
        N => tamanho da amostra
        limiar => limiar usado no z-score... quanto menor.. menos tolerante com outliers
'''

def calculaMedia(numbers):
    soma = 0.0
    for number in numbers:
        soma += number
    soma/=float(len(numbers))
    return soma


def calculaDesvioPadrao(numbers):
    soma = 0.0
    for number in numbers:
        soma += (number - media) * (number - media)
    soma/=(len(numbers)-1)
    return math.sqrt(soma)


N = 5
numbers = [int(random.uniform(15,20)) for i in range(0,N)]
outliers = [0 for i in range(0,N)]
media = calculaMedia(numbers)
desvio = calculaDesvioPadrao(numbers)
limiar = 1.0

## calcula z-score
for i, number in enumerate(numbers):
    z = abs(number - media)/desvio
    if z > limiar:
        ## detectei outlier
        outliers[i] = 1

## realiza fusao excluindo os outliers
dado = 0.0
tam = 0
for i, number in enumerate(numbers):
    if outliers[i] == 0:
        dado += number
        tam += 1
dado /= tam

print("elementos coletados: ", numbers)
print("outliers", outliers)
print("média: ", media)
print("desvio: ", desvio)
print("elemento a ser enviado depois de remover outliers: ", dado)


