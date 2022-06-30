linha1 = [[1], [2], [3]]
linha2 = [[4], [5], [6]]
linha3 = [[7], [8], [9]]
geral = [linha1+linha2+linha3]

def exibir_jogo ():
    print (linha1)
    print (linha2)
    print (linha3)

def regra (contador):
    c=contador
    if linha1[0]==linha1[1]==linha1[2]=='0' or linha1[0]==linha2[0]==linha3[0]=='0' or linha1[0]==linha2[1]==linha3[2]=='0' or linha1[1]==linha2[1]==linha3[1]=='0' or linha1[2]==linha2[2]==linha3[2]=='0' or linha2[0]==linha2[1]==linha2[2]=='0' or linha3[0]==linha3[1]==linha3[2]=='0' or linha1[2]==linha2[1]==linha3[0]=='0':
        print ('fim de jogo! Jogador 1 venceu')
        exibir_jogo()
        c+=9
    elif linha1[0]==linha1[1]==linha1[2]=='X' or linha1[0]==linha2[0]==linha3[0]=='X' or linha1[0]==linha2[1]==linha3[2]=='X' or linha1[1]==linha2[1]==linha3[1]=='X' or linha1[2]==linha2[2]==linha3[2]=='X' or linha2[0]==linha2[1]==linha2[2]=='X' or linha3[0]==linha3[1]==linha3[2]=='X' or linha1[2]==linha2[1]==linha3[0]=='X':
        print('fim de jogo! Jogador 2 venceu')
        exibir_jogo()
        c+=9
    return c

def jogador1 ():
    geral = linha1 + linha2 + linha3
    jogador1 = int(input('Qual posição você quer jogar? (0)'))
    while jogador1 > 9 or jogador1 < 1:
        jogador1 = int(input('Jogada inválida! Jogue novamente! (0)'))
    while geral[jogador1 - 1] == '0' or geral[jogador1 - 1] == 'X':
        jogador1 = int(input('Jogada inválida! Jogue novamente! (0)'))
    if jogador1 == 1 or jogador1 == 2 or jogador1 == 3:
        linha1[jogador1 - 1] = '0'
    elif jogador1 == 4 or jogador1 == 5 or jogador1 == 6:
        linha2[jogador1 - 4] = '0'
    else:
        linha3[jogador1 - 7] = '0'
    return jogador1

def jogador2 ():
    geral = linha1 + linha2 + linha3
    jogador2 = int(input('Qual posição você quer jogar? (X)'))
    while jogador2 > 9 or jogador2 < 1:
        jogador2 = int(input('Jogada inválida! Jogue novamente! (X)'))
    while geral[jogador2-1] == '0' or geral[jogador2-1] == 'X':
        jogador2 = int(input('Jogada inválida! Jogue novamente! (X)'))
    if jogador2 == 1 or jogador2 == 2 or jogador2 == 3:
        linha1[jogador2 - 1] = 'X'
    elif jogador2 == 4 or jogador2 == 5 or jogador2 == 6:
        linha2[jogador2 - 4] = 'X'
    else:
        linha3[jogador2 - 7] = 'X'
    return jogador2

for c in range(1, 6):
    exibir_jogo()
    jogador1()
    regra(c)
    c = regra(c)
    if c==5:
        print('O jogo deu velha')
        break
    elif c>5:
        break
    exibir_jogo()
    jogador2()
    regra(c)
    c = regra(c)
    if c>5:
        break