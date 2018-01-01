from random import randint

def desenha(vetor):
    print "  {} {} {} {}".format(vetor[0],vetor[1],vetor[2],vetor[3]),
    print " ---> 1 2 3 4"
    print "  {} {} {} {}".format(vetor[4],vetor[5],vetor[6],vetor[7]),
    print " ---> 5 6 7 8"
    print "  {} {} {} {}".format(vetor[8],vetor[9],vetor[10],vetor[11]),
    print " ---> 9 10 11 12"
    print "  {} {} {} {}".format(vetor[12],vetor[13],vetor[14],vetor[15]),
    print " ---> 13 14 15 16"
    print "  {} {} {} {}".format(vetor[16],vetor[17],vetor[18],vetor[19]),
    print " ---> 17 18 19 20"

def check(vetor,pontos,num):
    for i in range(5):

        for j in range(0,18,4):
            if vetor[j] == vetor[j+1] and vetor[j] == vetor[j+2] and vetor[j] == vetor[j+3] and vetor[j] != 0:
                vetor[num] += 1
                for k in range(j,j+4):
                    if k != num:
                        vetor[k] = 0
                pontos[0] += 4*(vetor[num]-1)

        for j in range(4):
            if vetor[j] == vetor[j+4] and vetor[j] == vetor[j+8] and vetor[j] == vetor[j+12] and vetor[j] == vetor[j+16] and vetor[j] != 0:
                vetor[num] += 1
                for k in range(j,20,4):
                    if k != num:
                        vetor[k] = 0
                pontos[0] += 5*(vetor[num]-1)

vetor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pontos = [0]

print "POSICOES DE 1 a 20:"
print "Forme linhas de numeros iguais para pontuar! Vale vertical e horizontal :)\n"

desenha(vetor)

while True:
    needed = True
    maior = 5
    for j in range(20):
        if maior < vetor[j]:
            maior = vetor[j]
    rng = randint(1,maior)
    print "\n",rng,"eh seu numero nesse turno.\nEm qual posicao quer coloca-lo?"
    while needed:
        formato = False
        num = raw_input()
        try:
            num = (int)(num)
            num -= 1
        except:
            print "Formato invalido."
            formato = True
        if not formato:
            try:
                if vetor[num] == 0 and num >= 0:
                    needed = False
                else:
                    print "Numero invalido."
            except:
                print "Numero invalido."
    vetor[num] = rng
    check(vetor,pontos,num)
    desenha(vetor)
    if 0 not in vetor:
        print "Game over"
        print "Pontuacao: {}".format(pontos[0])
        break
