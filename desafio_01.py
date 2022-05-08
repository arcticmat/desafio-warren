# Alguns números inteiros positivos n possuem uma propriedade na qual a soma de
# n + reverso(n) resultam em números ímpares. Por exemplo, 36 + 63 = 99 
# e 409 + 904 = 1313. Considere que n ou reverso(n) não podem começar com 0.

# Existem 120 números reversíveis abaixo de 1000.

# Construa um algoritmo que mostre na tela todos os números n onde a soma 
# de n + reverso(n) resultem em números ímpares que estão abaixo de 1 milhão.


def reverse(n: int) -> int:
    r = int(str(n)[::-1])
    return r

def find_reverse(n : int) -> list:
    n_list: list = []
    for i in range(1, n + 1):
        if (i % 10 == 0):
            pass
        elif ((i + reverse(i)) % 2 == 1):
            n_list.append(i)
    return n_list


reversed_numbers = find_reverse(n=1_000_000)

for n in reversed_numbers:
    print(n)
