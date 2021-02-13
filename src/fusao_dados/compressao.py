import random
import math

'''
    Compressao de dados
'''

def toBinary(number):
    ans = []
    while number > 0:
        ans.append(number%2)
        number = number//2
    return ans


def diferenca(base, number):
    ans = []
    index = 0
    while base[index] == 0:
        index += 1

    while index < len(number) and number[index] == 1:
        index += 1

    if index == len(number):
        index -= 1

    while index < len(number):
        ans.append(number[index])
        index += 1
    return ans


def binaryToNumber(binary):
    ans = 0
    binary.reverse()
    for i in range(len(binary)):
        ans += int(binary[i]) * 2**i
    return ans
    


def descomprime(base, diff_concatenado, posicao_leituras):
    N = 0
    numbers_binary = []
    diff_numbers = []

    
    ## pega numero de elementos
    aux = []
    for val, elem in enumerate(posicao_leituras):
        if elem == 1:
            N+=1
            aux.append(diff_concatenado[val])

            ans = [base[i] for i in range(len(base))]
            k = -1
            for i in range(len(base)-1, len(base)-1-len(aux), -1):
                ans[i] = aux[k]
                k += -1

            print("\t", aux)
            print("\t", ans)
            print("\t", binaryToNumber(ans))
            aux = []
        else:
            aux.append(diff_concatenado[val])

    print("\n\n ###### descomprimindo usando apenas: ######", \
            "\n    base       : ", base, "(", len(base), " bits )",\
            "\n    concatenado: ", diff_concatenado, "(", len(diff_concatenado), " bits )", \
            "\n    posicaoLeit: ", posicao_leituras, "(", len(posicao_leituras), " bits )", \
            "\n ####### antes seria (", (N*len(base)), " bits ) para os dados ######")


    


def main():
    N = 5
    maxBits = 8
    base = [0 for i in range(maxBits)]
    numbers = [int(random.uniform(11,15)) for i in range(N)]
    numbers_binary = []
    max_bits_used = 0
    diff_concatenado = []
    posicao_leituras = []

    ## itera nos numeros
    for i in range(N):
        binary_number = toBinary(numbers[i])    ## converte pra binario
        max_bits_used = max(max_bits_used, len(binary_number))
        while len(binary_number) < 8:
            binary_number.append(0)
        binary_number.reverse()
        numbers_binary.append(binary_number)

    for i in range(max_bits_used):
        base[i] = 1
    base.reverse()

    print("numbers  : ", numbers)
    print("base     : ", base)
    for i, elem in enumerate(numbers_binary):
        print("val[", numbers[i], "]: ", elem)

    ## calcula as diferencas
    for i in range(N):
        diff_full = diferenca(base, numbers_binary[i])
        print("diff     : ", diff_full)

        for i in range(len(diff_full)):
            diff_concatenado.append(diff_full[i])
            posicao_leituras.append(0)
        posicao_leituras[-1] = 1

    print("concatenado:", diff_concatenado)
    print("posicao lei:", posicao_leituras)

    ## envio dos elementos
    descomprime(base, diff_concatenado, posicao_leituras)





if __name__ == "__main__":
    main()
