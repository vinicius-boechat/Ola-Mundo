#   Jogo da cobrinha com escolha das variáveis.
# controle com as setinhas ← →, esquerda e direita, do teclado  
# 
#         Correção de alguns bugs
#           Colocar no GitHub
# 
#  Faltou: 
#   - Opção de recomeço
# 

from os import system
from time import sleep
import msvcrt  # usar o teclado
import emoji
from random import randint, choice


#  VARIAVEIS

e = '     ' # espaços 5 caracteres

caracter_jogador = emoji.emojize('  :star: ', language='alias') # cobrinha

parede = '  #  '

x = y = 15 # tamanho tabuleiro

x_c = y_c = 2  # ponte de partida 

cobra = [(x_c, y_c)] #  cobra

tam = 3 # tamanho inicial

seta = '>' #direção

time = 0.20

comida = emoji.emojize('  :smile: ', language='alias')




linha_comida = randint(1, x)
coluna_comida = randint(1, y)
tem_comida = False
lugar_comida = None



# Criando o tabuleiro
coluna = [[e for j in range(x)] for i in range(y)]  # revisar essa forma de criar matriz


# Imprimindo as paredes do tabuleiro
#criar a parede
for i in range(y):
    for j in range(x):
        if j == 0 or i == 0 or j == (len(coluna[0]) - 1) or i == (len(coluna) - 1):
            coluna[i][j] = parede





#fazendo o while
while True:
   

#               atualizar a cobrinha toda no tabuleiro 
    cobra.append((x_c, y_c))

        # colocando a cobrinha no tabuleiro

    
    # ficou tendo q atualizar so a cabeça
    coluna[cobra[-1][1]][cobra[-1][0]] = caracter_jogador

        
        
        
# colocar a comida

    #   criar a comida

    if not tem_comida:   
        vazio = []      # lista de lugares vazios

        for k, i in enumerate(coluna):
            for g, j in enumerate(i):

                if j != caracter_jogador and j != parede and j != comida:
                    vazio.append([k, g])
                    
            
        if vazio:
            lugar_comida = choice(vazio)

            y_comida, x_comida = lugar_comida

            tem_comida = True
            coluna[y_comida][x_comida] = comida


    
    #               checar o teclado do jogador
    if msvcrt.kbhit():      # tava dando problema sem isso, O codigo ficou esperando uma tecla pra prosseguir com o while

        tecla = msvcrt.getch()              #   Setas o teclado devolve 2 bytes, o primeiro começam com b'\xe0' pq é uma tecla especial
                                            #       a próxima tecla identifica qual seta foi

        if tecla == b'\xe0':        # se é tecla especial
            tecla2 = msvcrt.getch()     # qual tecla é

            # If's para atualizar a direção
            if tecla2 == b'K': #    SETINHA ESQUERDA
                # girar
                if seta == '^':
                    seta = '<'
                elif seta == '<':
                    seta = 'v'
                elif seta == 'v':
                    seta = '>'
                elif seta == '>':
                    seta = '^'

            
            elif tecla2 == b'M': #    SETINHA DIREITA
                if seta == '^':
                    seta = '>'
                elif seta == '>':
                    seta = 'v'
                elif seta == 'v':
                    seta = '<'
                elif seta == '<':
                    seta = '^'

#atualizando a direção

    # andar 1 pra frente
    if seta == '^':
        y_c -= 1
    elif seta == '>':
        x_c += 1
    elif seta == 'v':
        y_c += 1
    elif seta == '<':
        x_c -= 1


        # VERIFICAR ANTES A O LUGAR Q ELA VAI
    
    
    if cobra[-1][0] == 0 or cobra[-1][1] == 0 or cobra[-1][0] == (x - 1) or cobra[-1][1] == (y - 1) or (x_c, y_c) in cobra:
        break




#       VERIFICAR COMER COMIDA
    if coluna[y_c][x_c] == comida:
#        coluna[y_c][x_c] = e
        tam += 1
        tem_comida = False
        lugar_comida = None



    # se n bateu em nada ---> continuar



    #   EXIBIR             ta criando certinho a matriz
    for i in range(y):
        for j in range(x):
            print(f'{coluna[i][j]}', end='')
        print('')

    print(f'Tamanho: {tam}')


    # controlar o tamanho da cobrinha AQUI
    if (len(cobra)) > tam:
        coluna[cobra[0][1]][cobra[0][0]] = e        #tem q substituir o rabo por E ja que n cria mais a matriz toda vez
        cobra.pop(0)

    sleep(time)

    system('cls')       # print("\033[H\033[J", end="")


print(f'\n {'FIM DO JOGO':-^40} \n')

