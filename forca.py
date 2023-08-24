import random

#Função do Jogo
def jogar():
    
    #Chamando a função
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    #Variaveis com valor False para que a contagem possa ser mais limpa
    enforcou = False
    acertou = False
    erros = 0

    #Loop para que aconteça toda as comparações necessárias do jogo
    while not enforcou and not acertou:

        chute = pede_chute()


        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprima_mensagem_vencedor()
    else:
        imprima_mensagem_perdedor(palavra_secreta)




#Mensagem inicial do jogo
def imprime_mensagem_abertura():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

#Essa função será responsável pela leitura do arquivo e inicialização da palavra secreta.
#Como a função irá inicializar a palavra secreta, ela deve retorná-la, assim teremos acesso à palavra fora da função.
#Ao chamar a função, como ela irá retornar a palavra secreta, será guardada em uma variável
def carrega_palavra_secreta():
    arquivo = open("Python\palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

#Ela será responsável por fazer o preenchimento de letras acertadas atravéz do caractere _
#Para que ela saiba que a letra está certa de acordo coma a palavra_secreta, ela precisa ter acesso a palavra que se encontra dentro do parametro
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

#Essa função é responsável apenas por pedir o chute do usuário e armazenala em uma variável chamada chute
#sendo assim, vocÊ precisa retornar o valor de chute
def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

#Essa função precisa receber 3 paramêtros, chute (do usuário), letras_acertadas, palavra_secreta
#Primeiro vai ser feito o comparativo, se chute está dento de letras, acontecerá o preenchimento da letras_acertadas
#Cada vez qe o usuário chuta, esse comparativo acontece até o preenchimento de letras acertadas ser igual a palavra_secreta
#Porém mais para frente terá um limite de chute.
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

#Desenho ilustrativo de um troféu, representando que você acertou e venceu o jogo.
#Essa função não precisa de nenhum paramêtro, pois essa função será chamada dentro de um if e else
#para saber se ele acertou ou não
def imprima_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

#Desenho ilustrativo que a cada chute errado dentro das 7 tentativas que você tem ele te mostrará uma parte da forca sendo preenchida
#até você errar todas e mostrar a forca completa e o desenho de que você perdeu
#Para que a contagem aconteça e seja impresso partes referente a quantidade de erros
#a função precisa receber o paramêtro a quantidade de erros que o usuário já cometeu
#para que assim a comparação aconteça
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#Desenho ilustrativo de uma caveira, representando que você perdeu por errar as letras da palavra_secreta e esgotou a quantidade de tentativas
#e que você não conseguiu ganhar esse jogo
#Quando se esgotar as tentativas do usuário, será impresso a palavra_secreta
#para que o usuário saiba qual era a palavra_secreta
#Mais para isso acontecer, essa função preisa receber como paramêtro a palavra_secreta para que assim ela seja impressa
def imprima_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

#Nome do ambiente principal do programa
if __name__ == "__main__":
    jogar()
    