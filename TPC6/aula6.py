# Modelo: [(nome,desc,anoCriação,periodo,compositor,duração,_id)]

import csv
import matplotlib.pyplot as plt

def lerObras(filename):
    file=open(filename, encoding='UTF8')
    file.readline()
    csv_file= csv.reader(file,delimiter=';')
    lista = []
    for linha in csv_file:
        lista.append(tuple(linha))
    return lista

def contarObras(obras):
    return len(obras)

def imprimeObras(obras):
        print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
        for nome, desc, ano,_, comp, *_ in obras:
            print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")

def ordenavalores(tuplo):
    return tuplo[0]
def ordenaAlft(obras):
    lista2=[]
    for nome,_,anoCriacao, *_ in obras:
        lista2.append((nome,anoCriacao))
    lista2.sort(key=ordenavalores)
    return lista2

def ordenavalores1(tuplo):
    return tuplo[1]
def ordenaCresa(obras):
    lista3=[]
    for nome,_, anoCriacao, *_ in obras:
        lista3.append((nome,anoCriacao))
    lista3.sort(key=ordenavalores1)
    return lista3

def ordenaComp(obras):
    listaComp=[]
    for _,_,_,_,compositor,*_ in obras:
        listaComp.append(compositor)
    listaComp.sort()
    return listaComp
    
def distribP():
    file=open('obras.csv',encoding='UTF8')
    file.readline()
    linhas=csv.reader(file, delimiter=';')
    distribP={}
    for c in linhas:
        if c[3] in distribP.keys():
            distribP[c[3]]=distribP[c[3]]+1
        else:
            distribP[c[3]]=1
    return distribP

def distribTitA(obras):
    distribA = {}
    for nome, _, ano, *_ in obras:
        if ano in distribA.keys():
            distribA[ano].append(nome)
        else:
            distribA[ano] = [nome]
    return distribA

def distribTitC(obras):
    distribC={}
    for nome,_,_,_,compositor,*_ in obras:
        if compositor in distribC.keys():
            distribC[compositor].append(nome)
        else:
            distribC[compositor]=[nome]
    return distribC

def plotDistribP():
    file=open('obras.csv',encoding='UTF8')
    file.readline()
    linhas=csv.reader(file, delimiter=';')
    distrib1={}
    for p in linhas:
        if p[3] in distrib1.keys():
            distrib1[p[3]]=distrib1[p[3]]+1
        else:
            distrib1[p[3]]=1
    plt.bar(distrib1.keys(), distrib1.values(), color='magenta')
    plt.xticks([x for x in range(0, len(distrib1.keys()))], distrib1.keys(), rotation='vertical')
    plt.show()
    return

def plotDistribA():
    file=open('obras.csv',encoding='UTF8')
    file.readline()
    linhas=csv.reader(file, delimiter=';')
    distrib2={}
    for a in linhas:
        if a[2] in distrib2.keys():
            distrib2[a[2]]=distrib2[a[2]]+1
        else:
            distrib2[a[2]]=1
    plt.figure(figsize=(28,12))
    plt.bar(distrib2.keys(), distrib2.values(), color='green')
    plt.xticks([x for x in range(0, len(distrib2.keys()))], distrib2.keys(), rotation='vertical')
    plt.show()
    return

def plotDistribC():
    file=open('obras.csv',encoding='UTF8')
    file.readline()
    linhas=csv.reader(file, delimiter=';')
    distrib3={}
    for c in linhas:
        if c[4] in distrib3.keys():
            distrib3[c[4]]=distrib3[c[4]]+1
        else:
            distrib3[c[4]]=1
    plt.figure(figsize=(28,12))
    plt.bar(distrib3.keys(), distrib3.values(), color='purple')
    plt.xticks([x for x in range(0, len(distrib3.keys()))], distrib3.keys(), rotation='vertical')
    plt.show()
    return

def compositorO(obras):
    novodicio=zip(obras.keys(), obras.values())
    novalista=list(novodicio)
    return novalista