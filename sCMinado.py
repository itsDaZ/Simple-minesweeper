import math
import random

def gera_campo(tam_campo):

    '''
    Função responsável por gerar o "Campo" do jogo.
    '''
    campo = []
    chance = [0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0 -1]
    for i in range(tam_campo+2):
        lin_campo = []
        for j in range(tam_campo+2):
            if i == 0 or i == tam_campo+1:
                lin_campo.append(0)
            elif j == 0 or j == tam_campo+1:
                lin_campo.append(0)
            else:

                gera_bomba = random.choice(chance)
                lin_campo.append(gera_bomba)
        campo.append(lin_campo)

    for i in range(1,len(campo)-1):

        for j in range(1,len(campo[0])-1):

            count = 0

            top_r = campo[i-1][j+1]
            top   = campo[i-1][j]
            top_l = campo[i-1][j-1]

            left  = campo[i][j-1]
            right = campo[i][j+1]

            bot_r = campo[i+1][j+1]
            bot   = campo[i+1][j]
            bot_l = campo[i+1][j-1]

            arredores = [top_r,top,top_l,left,right,bot_r,bot,bot_l]
            for n in arredores:
                if n == -1:
                    count += 1
            if campo[i][j] != -1:
                campo[i][j] = count

    return(campo)

def clone_matriz(A):
    C = []
    m = len(A)
    for i in range(m):
        C.append(A[i][:])
    return C


def camp_vazio(campo):


    camp2 = []

    for i in range(len(campo)):
        lin_camp2 = []
        for j in range(len(campo[0])-1):
            lin_camp2.append(-2)

        camp2.append(lin_camp2)

    return(camp2)



def atualiza_jogo(campo,camp2,x,y):

    m = x
    n = y

    scan = [-1,0,1]

    perdeu = False

    if campo[y][x-1] == -1:

        perdeu = True

    elif campo[y][x-1] == 0 and m < len(campo[0])-2:

        for i in scan:
            for j in scan:
                camp2[n+i][m-1+j] = campo[n+i][m-1+j]
    else:
        camp2[y][x-1] = campo[y][x-1]





    return(perdeu)



def imprime_atual(camp2):

    '''
    Essa função imprime o estado atual do jogo.

    '''

    for i in range(len(camp2)-1):
        for j in range(len(camp2[0])):
            if i == 0 and not j == len(camp2[0]):
                print('%2d'%j , end = " ")
            elif j==0 :
                print('%2d' %i ,end = " ")
            elif camp2[i][j] == 0:
                print(' -',end = " ")
            elif camp2[i][j] > 0:
                print('%2d' % camp2[i][j], end = " ")
            else:
                print('[]' , end = " ")
        print()

    print()
    return()


def main():

    print("Bem Vindo ao jogo!")
    tam_campo = int(input("Digite o tamanho desejado para o campo: "))
    campo_1 = gera_campo(tam_campo)
    campo_2 = camp_vazio(campo_1)
    perdeu = False
    imprime_atual(campo_2)
    while perdeu == False:
        x = int(input("digite a coordenada x de sua jogada: \n")) + 1
        y = int(input("digite a coordenada y de sua jogada: \n"))
        perdeu = atualiza_jogo(campo_1,campo_2,x,y)
        if not perdeu:
            imprime_atual(campo_2)
    if perdeu:
        imprime_atual(campo_1)
    print("\n Putz, você acertou uma bomba... \n")
    print("Fim de jogo.")

main()
