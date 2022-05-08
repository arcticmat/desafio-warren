def solution(limite_alunos_presentes: int, t_chegada_alunos: list):
    # filtrando apenas os alunos que chegaram no horario
    alunos_presentes: list = [x for x in t_chegada_alunos if x <= 0]
    
    # se a quantidade de alunos presentes for
    # igual ou maior que o limite definido
    # então terá aula normal
    if len(alunos_presentes) >= limite_alunos_presentes:
        print("Aula Normal")
    # caso falso a condição acima
    else:
        print("Aula Cancelada")
        

solution(limite_alunos_presentes=3, t_chegada_alunos=[-2, -1, 0, 1, 2])
# output: Aula Normal
# Os três primeiros alunos chegaram no horário. Os dois últimos estavam atrasados.
# O limite é de três alunos, portanto a aula não será cancelada

solution(limite_alunos_presentes=5, t_chegada_alunos=[-2, -1, -3, 0, 1, 2, 2, 3, 4])
# output: Aula Cancelada
# Os quatro primeiros alunos chegaram no horário. Os dois últimos cinco estavam atrasados.
# O limite é de cinco alunos, portanto a aula será cancelada
