aluno_db = 'Matheus'
def verifica_aluno(aluno):
    if aluno_db == aluno:
        return 'Aluno encontrado.'
    else:
        return 'Aluno não encontrado.'

def verifica_situacao(n1, n2, n3):
    if (n1 + n2 + n3) / 3 >= 7.0:
        return 'Aprovado'
    else:
        return 'Reprovado'

def test_aprovado():
    assert verifica_situacao(7, 7, 7) == 'Aprovado'

def test_reprovado():
    assert verifica_situacao(4, 2, 1) == 'Reprovado'

def test_existe_aluno():
    assert verifica_aluno('Matheus') == 'Aluno encontrado.'

def test_nao_exite_aluno():
    assert verifica_aluno('José') == 'Aluno não encontrado.'
