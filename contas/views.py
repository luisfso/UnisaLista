from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    arq = open('arquivo.txt','r')
    data = {}
    fila = []
    test = request.GET.get("add","")
    conteudo = arq.readlines()
    conteudo.insert(0,str(test)+"\n")
    arq.close()
    arq = open('arquivo.txt','w')
    arq.writelines(conteudo)
    conteudo.reverse()
    data["resposta"] = test
    data["completa"] = conteudo

    arq.close()
    return render(request,"index.html" , data)

def deletar(request):
    arq = open("arquivo.txt")
    todas_as_linhas = arq.readlines()
    ultima = todas_as_linhas[len(todas_as_linhas)-1]
    arq.close()
    with open('arquivo.txt', 'r+', encoding="utf-8") as arquivo:

        # Move o ponteiro (similar a um cursor de um editor de textos) para o fim do arquivo.
        arquivo.seek(0, os.SEEK_END)

        # Pula o ultimo caractere do arquivo
        # No caso de a ultima linha ser null, deletamos a ultima linha e a penúltima
        pos = arquivo.tell() - 1

        # Lê cada caractere no arquivo, um por vez, a partir do penúltimo
        # caractere indo para trás, buscando por um caractere de nova linha
        # Se encontrarmos um nova linha, sai da busca
        while pos > 0 and arquivo.read(1) != "\n":
            pos -= 1
            arquivo.seek(pos, os.SEEK_SET)

        # Enquanto não estivermos no começo do arquivo, deleta todos os caracteres para frente desta posição
        if pos > 0:
            arquivo.seek(pos, os.SEEK_SET)
            arquivo.truncate()
    data = {}
    arq = open("arquivo.txt")
    conteudo = arq.readlines()
    conteudo.reverse()
    data["completa"] = conteudo
    data["chamado"] = ultima

    arq.close()
    return render(request,"deletar.html" , data)

