import itertools


n: int = 10
v: list = [2,3,4]
possibles_vectors: list = []
sum_eq_n_vectors: list = []


# criando uma lista com todas as combinações
# possíveis de 10 elementos
for i in range(1, 11):
    possibles_vectors += itertools.combinations_with_replacement(v, i)
    
# filtrando apenas os conjuntos onde a soma
# de seus elementos é igual a n
for p in possibles_vectors:
    if sum(list(p)) == n:
        sum_eq_n_vectors.append(p)

# obtendo o tamanho do menor conjunto
min = len(sum_eq_n_vectors[0])

# obtendo todos os conjuntos onde seu tamanho
# é igual o tamanho do menor conjunto
final_vector = [x for x in sum_eq_n_vectors if len(x) == min]

# print(possibles_vectors)
print(sum_eq_n_vectors) # output: [(2, 4, 4), (3, 3, 4), (2, 2, 2, 4), (2, 2, 3, 3), (2, 2, 2, 2, 2)]
print(min) # output: 3
print(final_vector) # output: [(2, 4, 4), (3, 3, 4)]
