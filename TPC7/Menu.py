import TPC7 as t
alunos=t.lerficheiro()
utilizador=15
while utilizador!=0:
    print('''Menu de opções:
    [1]- Lê o dataset obras
    [2]- Distribuição dos alunos por curso
    [3]- Calcula as médias de cada aluno e acrescenta a nova coluna ao dateset
    [4]- Atribui um escalão a cada aluno de acordo com a sua média e acrescenta a nova coluna no dataset
    [5]- Distribuição dos alunos por escalão
    [6]- Gráficos das distribuições
    [7]- Tabelas das distribuições''' )
    utilizador=int(input('Qual opção do menu escolhe?'))
    print('A sua opção foi', utilizador)
    if utilizador==1:
        print(t.lerficheiro())
    elif utilizador==2:
        print('A distribuição dos alunos por curso é:')
        print(t.distribCurso(alunos))
        print('\n')
        print('O número de alunos por curso é:')
        print(t.alcurso(alunos))
        print('\n')
    elif utilizador==3:
        print(f"{'Média dos TPCs por alunos':-^50}")
        print(f"|{'Aluno':^40}|{'Média':^7}|")
        al = list(t.media(alunos).items())
        for x in range(100):
            print(f"|{al[x][0][:38]:^40}|{al[x][1]:^7}|")
        t.addcolumn_1(t.listacomp(t.paralista(t.media(alunos))))
    elif utilizador==4:
        print(f"{'Escalão de cada aluno':-^52}")
        print(f"|{'Aluno':^40}|{'Escalão':^9}|")
        al = list(t.grau(t.lerficheiro()).items())
        for x in range(100):
            print(f"|{al[x][0][:38]:^40}|{al[x][1]:^9}|")
        t.addcolumn_1(t.listacomp(t.paralistag(t.grau(alunos))))
    elif utilizador==5:
        print('A distribuição dos alunos por escalão é:')
        print(t.almedia(alunos))
    elif utilizador==6:
        print('''[1]- Gráfico da distribuição dos alunos por curso
[2]- Gráfico da distribuição dos alunos por escalão''')
        p=3
        while p!=0:
            p=int(input('Qual a distribuição que quer ver representada?'))
            if p==1:
                print(t.graficoalunoscurso(t.alcurso(t.lerficheiro()), "Distribuição dos alunos por curso", "Curso", "Número de alunos"))
            elif p==2:
                print(t.graficoalunoscurso(t.almedia(t.lerficheiro()), "Distribuição dos alunos por escalão", "Escalão", "Número de alunos"))
        if p==0:
            print('A opção escolhida anteriormente fechou')
    elif utilizador==7:
        print('''[1]- Tabela da distribuição por curso
[2]- Tabela da distribuição por escalão''' )
        q=3
        while q!=0:
            q= int(input('Qual a distribuição que quer ver tabelada?'))
            if q==1:
                print(f"{'Tabela de alunos por curso':_^105}")
                print(t.tabeladistribuicaocurso())
            elif q==2:
                print(f"{'Tabela de alunos por curso':_^96}")
                print(t.tabeladistribuicaograus())
        if q==0:
            print('A opção escolhida anteriormente fechou')
print('Fim do programa')
        