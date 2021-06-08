def notas(* n, sit=False):
    '''
    -> a Função notas tem o objetivo de mostrar o calculo das notas do aluno.
    :param n: São as notas dos alunos
    :param sit: Mostra a situação do aluno
    :return: retorna o total, a média, maior e menor nota do aluno.
    '''
    nota = dict()
    nota['nota'] = n
    nota['Total'] = len(n)
    nota['Maior'] = max(n)
    nota['Menor'] = min(n)
    nota['Média'] = sum(n) / len(n)
    if sit:
        if nota['Média'] >= 7:
            nota['Situação'] = 'BOA'
        elif nota['Média'] >= 5:
            nota['Situação'] = 'BOA'
        else:
            nota['Situação'] = 'RUIM'
    return nota

resp = notas(3, 4, 8, 10, 7, 4, sit=True)
print(resp)
help(notas)
