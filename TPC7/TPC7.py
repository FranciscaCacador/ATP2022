import csv
import matplotlib.pyplot as plt

def lerficheiro():
    file=open('alunos.csv', encoding='UTF8')
    file.readline()
    filealunos=csv.reader(file, delimiter=',')
    alunos=[]
    for linha in filealunos:
        alunos.append(tuple(linha))
    return alunos

def distribCurso(alunos):
    distribC={}
    for id_aluno, nome, curso, *_ in alunos:
        if curso in distribC.keys():
            distribC[curso].append((id_aluno, nome))
        else:
            distribC[curso]=[(id_aluno,nome)]
    return distribC








def media(alunos):
    lst1 = []
    for _, nome, _, t,p,c,v, *_ in alunos:
        media = (int(t)+int(p)+int(c)+int(v))/4
        lst1.append((nome, media))
    dici = dict(lst1)
    return dici

def paralista(al):
    l=[]
    l.append("Médias")
    alu = list(al.items())
    for i in alu:
        l.append(i[1])
    return l
def paralistag(al):
    l=[]
    l.append("Grau")
    alu = list(al.items())
    for i in alu:
        l.append(i[1])
    return l

def listadelinhas(): #para meter dataset em lista
    data = []
    with open("alunos.csv", "r", encoding="utf8") as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    f.close()
    return data
def listacomp(lst): #adicionar lista da dist aluno/qqcoisa à lista dataset pode ser media ou avaliacao final
    data = listadelinhas()
    for i in range(len(lst)):
        data[i].append(lst[i])
    return data
def addcolumn_1(data): #addcolumn(listacomp(media(alunos)))
    with open("alunos.csv", "w", encoding= "utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    f.close()




def almedia(alunos):
    dicionariaescalao = {"[1,4.99] - E":0, "[5,8.99] - D":0, "[9,12.99] - C":0, "[13,16.99] - B":0, "[17,20] - A":0,}
    for _,_,_,_, _, _, _, media, *_ in alunos:
        med = float(media) #[(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4)]
        if med < 5:
            dicionariaescalao["[1,4.99] - E"] += 1
        elif med < 9:
            dicionariaescalao["[5,8.99] - D"] += 1
        elif med < 13:
            dicionariaescalao["[9,12.99] - C"] += 1
        elif med < 17:
            dicionariaescalao["[13,16.99] - B"] += 1
        elif med < 21:
            dicionariaescalao["[17,20] - A"] += 1
    return dicionariaescalao

def grau(alunos):
    lista2=[]
    med = list(media(alunos).items())
    for x in range (100):
        if med[x][1] < 5:
            lista2.append((lerficheiro()[x][1], "E"))
        elif float(med[x][1]) < 9:
            lista2.append((lerficheiro()[x][1], "D"))
        elif float(med[x][1]) < 13:
            lista2.append((lerficheiro()[x][1], "C"))
        elif float(med[x][1]) < 17:
            lista2.append((lerficheiro()[x][1], "B"))
        elif float(med[x][1]) < 21:
            lista2.append((lerficheiro()[x][1], "A"))
    dicionariograu = dict(lista2)
    return dicionariograu


def alcurso(alunos):
    dic = {}
    for _,_,curso, *_ in alunos:
        if curso in dic.keys():
            dic[curso] += 1
        else:
            dic[curso] = 1
    return dic



def graficoalunoscurso(dist, titulo, abcissa, ordenada):
    x = list(dist.keys())
    y = list(dist.values())
    plt.xlabel(abcissa)
    plt.ylabel(ordenada, rotation= 'vertical')
    plt.plot(x,y,color= "red")
    plt.title(titulo)
    plt.show()


def tabeladistribuicaocurso():
    print(f"{'':19} {'':_^85}")
    print(f"{'':20}|{'ENGBIOM':^20}|{'ENGFIS':^20}|{'LEI':^20}|{'LCC':^20}|")
    print(f"{'':_^105}")
    print(f"|{'Alunos:':^19}|{list(alcurso(lerficheiro()).values())[0]:^20}|{list(alcurso(lerficheiro()).values())[1]:^20}|{list(alcurso(lerficheiro()).values())[2]:^20}|{list(alcurso(lerficheiro()).values())[3]:^20}|")
    print(f"{'':_^105}")

def tabeladistribuicaograus(): 
    print(f"{'':14} {'':_^81}")
    print(f"{'':15}|{'A':^15}|{'B':^15}|{'C':^15}|{'D':^15}|{'E':^15}|")
    print(f"{'':_^96}")
    print(f"|{'Alunos:':^14}|{list(almedia(lerficheiro()).values())[4]:^15}|{list(almedia(lerficheiro()).values())[3]:^15}|{list(almedia(lerficheiro()).values())[2]:^15}|{list(almedia(lerficheiro()).values())[1]:^15}|{list(almedia(lerficheiro()).values())[0]:^15}|")
    print(f"{'':_^96}")


