# -*- coding: UTF-8 -*-

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)
    return 'O nome %s foi adicionado com sucesso' % (nome)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.remove(nome)
    return 'O nome %s foi removido com sucesso' % (nome)

def alterar(nomes):
    print 'Qual nome gostaria de alterar'
    nome_remover = raw_input()
    if (nome_remover in nomes):
        posicao = nomes.index(nome_remover)
        print 'Digite novo nome:'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()
    if (nome_a_procurar in nomes):
        print 'Nome %s está cadastrado' % (nome)
    else:
        print 'Nome %s não está cadastrado' % (nome)

def menu():
    nomes = []
    escolha = ' '
    while (escolha != '0'):
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar e 0 para terminar'
        escolha = raw_input()

        if (escolha == '1'):
            cadastrar(nomes)

        if (escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover(nomes)

        if (escolha =='4'):
            alterar(nomes)

         if (escolha=='5'):
            procurar(nomes)


menu()