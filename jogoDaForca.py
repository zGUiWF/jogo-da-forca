#Aluno:Guilherme Winck Ferrari RA:1134330
import os
import colorama
colorama.init()
import time

def dancinhaDaVitoria(danca1, danca2):
    coresRGB = [(255, 0, 255),(0, 0, 255),(255, 255, 0),(255, 0, 0),(0, 255, 255),(0, 255, 0)]
    loopCores = 0
    tempoDeExecucao = 0
    while True:
        if tempoDeExecucao == 5:
            break
        for revesaPrint in range(0,10):
            if tempoDeExecucao == 5:
                break
            if revesaPrint % 2 == 0:
                tempoDeExecucao = tempoDeExecucao + 1
                backgroundColor = f"\033[48;2;{coresRGB[loopCores % len(coresRGB)][0]};{coresRGB[loopCores % len(coresRGB)][1]};{coresRGB[loopCores % len(coresRGB)][2]}m"
                fonteColor = colorama.Fore.WHITE if loopCores % len(coresRGB) == 1 else colorama.Fore.BLACK
                os.system("cls" if os.name == "nt" else "clear")
                print(backgroundColor + fonteColor + colorama.Style.BRIGHT + str(danca1)+ colorama.Style.RESET_ALL)
                loopCores += 1
            else:
                backgroundColor = f"\033[48;2;{coresRGB[loopCores % len(coresRGB)][0]};{coresRGB[loopCores % len(coresRGB)][1]};{coresRGB[loopCores % len(coresRGB)][2]}m"
                fonteColor = colorama.Fore.WHITE if loopCores % len(coresRGB) == 1 else colorama.Fore.BLACK
                os.system("cls" if os.name == "nt" else "clear")
                print(backgroundColor + fonteColor + colorama.Style.BRIGHT + str(danca2)+ colorama.Style.RESET_ALL)
                loopCores += 1
            revesaPrint += 1
            time.sleep(0.5)

def jogarOuSair():
    while True:
        jogarNovamente = (input(f'({colorama.Fore.BLUE}0{colorama.Style.RESET_ALL})Para jogar novamente ({colorama.Fore.BLUE}1{colorama.Style.RESET_ALL})Para Sair:'))
        if jogarNovamente == '1' or jogarNovamente == '0':
            break
        else:
            print(f'Resposta inválida. Digite ({colorama.Fore.BLUE}0{colorama.Style.RESET_ALL})Para jogar novamente ({colorama.Fore.BLUE}1{colorama.Style.RESET_ALL})Para Sair:')
    if jogarNovamente == '0':
        jogoDaForca()
    else:
        os.system('cls')

def esconderPalavra(palavra):
    return '_' * len(palavra)

def atualizaPalavraEscondida(palavraChave, palavraEscondida, letra):
    novaPalavraEscondida = ''
    for i in range(len(palavraChave)):
        if palavraChave[i] == letra:
            novaPalavraEscondida += letra
        else:
            novaPalavraEscondida += palavraEscondida[i]
    return novaPalavraEscondida

def jogoDaForca():
    os.system('cls')
    print(f'             {colorama.Fore.MAGENTA}JOGO DA FORCA{colorama.Style.RESET_ALL}')
    print(f'')
    print(f"                 ______")
    print(f"                |/    |")
    print(f"                |     {colorama.Fore.RED}0{colorama.Style.RESET_ALL}")
    print(f"                |    {colorama.Fore.RED}/|\\{colorama.Style.RESET_ALL}")
    print(f"                |    {colorama.Fore.RED}/ \\{colorama.Style.RESET_ALL}")
    print(f"               _|_")
    print(f'')
    print(input(f'      precione {colorama.Fore.YELLOW}ENTER{colorama.Style.RESET_ALL} para jogar...'))

    os.system('cls')
    print(f'{colorama.Fore.BLUE}Insira o nome dos Jogadores:{colorama.Style.RESET_ALL}')
    desafiante = input(f'Nome do Desafiante{colorama.Fore.YELLOW}:{colorama.Style.RESET_ALL}')
    competidor = input(f'Nome do Competidor{colorama.Fore.YELLOW}:{colorama.Style.RESET_ALL}')
    danca1Desafiante = (f"<('o'<) !!!VITÓRIA DO {desafiante.upper()}!!! (>'o')> ")
    danca2Desafiante = (f" (>'o')>!!!VITÓRIA DO {desafiante.upper()}!!!<('o'<)  ")
    danca1Competidor = (f"<('o'<) !!!VITÓRIA DO {competidor.upper()}!!! (>'o')> ")
    danca2Competidor = (f" (>'o')>!!!VITÓRIA DO {competidor.upper()}!!!<('o'<)  ")
    danca1empate = (f" (>'o')>!!!EMPATE!!!<('o'<)  ")
    danca2empate = (f"<('o'<) !!!EMPATE!!! (>'o')> ")

    os.system('cls')

    print(f'{colorama.Fore.BLUE}Tela do Desafiante{colorama.Style.RESET_ALL}')
    palavraChave = input(f'Palavra secreta{colorama.Fore.YELLOW}:{colorama.Style.RESET_ALL}').lower()
    dica1 = input(f'Dica 1{colorama.Fore.YELLOW}:{colorama.Style.RESET_ALL}')
    dica2 = input(f'Dica 2{colorama.Fore.YELLOW}:{colorama.Style.RESET_ALL}')
    dica3 = input(f'Dica 3{colorama.Fore.YELLOW}:{colorama.Style.RESET_ALL}')
    dicas = [dica1, dica2, dica3]
    os.system('cls')
    
    print(f'              {colorama.Fore.BLUE}Sitema de Pontos:{colorama.Style.RESET_ALL}')
    print(f'       O competidor começa com {colorama.Fore.GREEN}12 pontos{colorama.Style.RESET_ALL}')
    print(f'     cada tentativa gasta diminui {colorama.Fore.RED}1 ponto{colorama.Style.RESET_ALL} do')
    print(f'    competidor e soma nos pontos do desafiante')
    print(f'      cada dica gasta diminui {colorama.Fore.RED}2 pontos{colorama.Style.RESET_ALL} do')
    print(f'    competidor e soma nos pontos do desafiante')
    print(f' no final da partida quem tiver mais pontos vence')
    print(f'ou se o competidor zera as {colorama.Fore.RED}6 tentativas{colorama.Style.RESET_ALL} ele perde!')
    print(input(f'        Presione {colorama.Fore.YELLOW}ENTER{colorama.Style.RESET_ALL} para iniciar...'))
    os.system('cls')

    palavraEscondida = esconderPalavra(palavraChave)

    palavraEscondida = esconderPalavra(palavraChave)
    letrasErradas = []
    tentativas = 6

    respostaAnterior = ""
    
    while tentativas > 0 and palavraEscondida != palavraChave:
        if tentativas == 6:
            print("  ______")
            print(" |/    |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print('')
        if tentativas == 5:
            print("  ______")
            print(" |/    |")
            print(f" |     {colorama.Fore.RED}0{colorama.Style.RESET_ALL}")
            print(" |")
            print(" |")
            print("_|_")
            print('')
        if tentativas == 4:
            print("  ______")
            print(" |/    |")
            print(f" |     {colorama.Fore.RED}0{colorama.Style.RESET_ALL}")
            print(f" |     {colorama.Fore.RED}|{colorama.Style.RESET_ALL}")
            print(" |")
            print("_|_")
            print('')
        if tentativas == 3:
            print("  ______")
            print(" |/    |")
            print(f" |     {colorama.Fore.RED}0{colorama.Style.RESET_ALL}")
            print(f" |     {colorama.Fore.RED}|\\{colorama.Style.RESET_ALL}")
            print(" |")
            print("_|_")
            print('')
        if tentativas == 2:
            print("  ______")
            print(" |/    |")
            print(f" |     {colorama.Fore.RED}0{colorama.Style.RESET_ALL}")
            print(f" |    {colorama.Fore.RED}/|\\{colorama.Style.RESET_ALL}")
            print(" |")
            print("_|_")
            print('')
        if tentativas == 1:
            print("  ______")
            print(" |/    |")
            print(f" |     {colorama.Fore.RED}0{colorama.Style.RESET_ALL}")
            print(f" |    {colorama.Fore.RED}/|\\{colorama.Style.RESET_ALL}")
            print(f" |    {colorama.Fore.RED}/{colorama.Style.RESET_ALL}")
            print("_|_")
            print('')

        print(f'{colorama.Fore.BLUE}Palavra: {palavraEscondida}{colorama.Style.RESET_ALL}')
        print(f'Tentativas restantes{colorama.Fore.GREEN}:{colorama.Style.RESET_ALL}{colorama.Fore.GREEN}{tentativas}{colorama.Style.RESET_ALL}')
        print(f'Letras erradas{colorama.Fore.RED}:{colorama.Style.RESET_ALL}{colorama.Fore.RED} {", ".join(letrasErradas)}{colorama.Style.RESET_ALL}')
        print(f'Dicas restantes{colorama.Fore.GREEN}:{colorama.Style.RESET_ALL}{colorama.Fore.GREEN}{len(dicas)}{colorama.Style.RESET_ALL}')
        print(f'Digite ({colorama.Fore.GREEN}1{colorama.Style.RESET_ALL}) Para solicitar 1 dica.')

        letra = input(f'Digite uma letra{colorama.Fore.YELLOW}:{colorama.Style.RESET_ALL}').lower()
        os.system('cls')

        if letra == respostaAnterior:
            if respostaAnterior == '1':
                print(f'{colorama.Fore.RED}Você deve ariscar uma letra antes de solicitar outra dica!{colorama.Style.RESET_ALL}')
                continue
            else:
                print(f'{colorama.Fore.RED}Você ja jogou essa letra!{colorama.Style.RESET_ALL}')
                continue
        else:
            respostaAnterior = letra

        if letra == '1':
            mostraDica = -1
            mostraDica = mostraDica + 1
            os.system('cls')
            if dicas == []:
                continue
            else:
                print(f'{colorama.Style.BRIGHT}A dica é:{colorama.Fore.YELLOW}{dicas[mostraDica]}{colorama.Style.RESET_ALL}')
                dicas.pop(0)
                continue

        if letra in palavraChave:
            palavraEscondida = atualizaPalavraEscondida(palavraChave, palavraEscondida, letra)
        else:
            letrasErradas.append(letra)
            tentativas -= 1

    if palavraEscondida == palavraChave:
        if ((len(dicas) * 2) + tentativas) > (12 - ((len(dicas) * 2) + tentativas)):
            dancinhaDaVitoria(danca1Competidor, danca2Competidor)
            print('')
            print(f'Pontos {competidor.upper()}:{colorama.Fore.GREEN}{(len(dicas) * 2) + tentativas}{colorama.Style.RESET_ALL} Pontos {desafiante.upper()}:{colorama.Fore.RED}{12 - ((len(dicas) * 2) + tentativas)}{colorama.Style.RESET_ALL}')
            print('')
            jogarOuSair()
        elif ((len(dicas) * 2) + tentativas) == (12 - ((len(dicas) * 2) + tentativas)):
            dancinhaDaVitoria(danca1empate, danca2empate)
            print('')
            print(f'Pontos {competidor.upper()}:{colorama.Fore.YELLOW}{(len(dicas) * 2) + tentativas}{colorama.Style.RESET_ALL} Pontos {desafiante.upper()}:{colorama.Fore.YELLOW}{12 - ((len(dicas) * 2) + tentativas)}{colorama.Style.RESET_ALL}')
            print('')
            jogarOuSair()
        else:
            dancinhaDaVitoria(danca1Desafiante, danca2Desafiante)
            print('')
            print(f'Pontos {competidor.upper()}:{colorama.Fore.RED}{(len(dicas) * 2) + tentativas}{colorama.Style.RESET_ALL} Pontos {desafiante.upper()}:{colorama.Fore.GREEN}{12 - ((len(dicas) * 2) + tentativas)}{colorama.Style.RESET_ALL}')
            print('')
            jogarOuSair()
    else:
        os.system('cls')
        dancinhaDaVitoria(danca1Desafiante, danca2Desafiante)
        print('')
        print("  ______")
        print(" |/    |")
        print(f" |     {colorama.Fore.RED}0{colorama.Style.RESET_ALL}")
        print(f" |    {colorama.Fore.RED}/|\\{colorama.Style.RESET_ALL}")
        print(f" |    {colorama.Fore.RED}/ \\{colorama.Style.RESET_ALL}")
        print("_|_")
        print('')
        print(f'{colorama.Fore.RED}!!!GAME OVER!!!{colorama.Style.RESET_ALL}')
        print(f'A palavra era {colorama.Fore.YELLOW}{palavraChave}{colorama.Style.RESET_ALL}')
        print('')
        jogarOuSair()
               
jogoDaForca()