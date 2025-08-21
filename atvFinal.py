import random


def jogoVelha():
    tamanho = 3
    placarX = 0
    placarO = 0
    resposta = "s"


    while resposta.lower() == "s":
        jogadaValida = 0
        jogadorAtual = "X"
        acertos = 0
        totalJogadas = tamanho * tamanho


        tabuleiro = [[" " for _ in range(tamanho)] for _ in range(tamanho)]


        print("Seja bem-vindo(a) ao Jogo da Velha")


        while acertos < totalJogadas:
            jogadaValida = 0
            while jogadaValida == 0:
                for i in range(tamanho):
                    linha = ""
                    for j in range(tamanho):
                        linha += f" | {tabuleiro[i][j]}"
                    linha += " |"
                    print(linha)


                print(f"\n=== Jogador {jogadorAtual}, faça a sua jogada! ({acertos}/{totalJogadas}) ===")
                linha_input = int(input(f"Digite a linha (0 a {tamanho-1}): "))
                coluna_input = int(input(f"Digite a coluna (0 a {tamanho-1}): "))


                if 0 <= linha_input < tamanho and 0 <= coluna_input < tamanho:
                    if tabuleiro[linha_input][coluna_input] != " ":
                        print("⚠️ Essa posição já foi ocupada. Tente outra!")
                    else:
                        tabuleiro[linha_input][coluna_input] = jogadorAtual
                        jogadaValida = 1
                        acertos += 1
                else:
                    print("⚠️ Coordenadas inválidas! Tente novamente.")


            venceu = 0
            for i in range(tamanho):
                if ((tabuleiro[i][0] == jogadorAtual and tabuleiro[i][1] == jogadorAtual and tabuleiro[i][2] == jogadorAtual) or
                    (tabuleiro[0][i] == jogadorAtual and tabuleiro[1][i] == jogadorAtual and tabuleiro[2][i] == jogadorAtual)):
                    venceu = 1


            if ((tabuleiro[0][0] == jogadorAtual and tabuleiro[1][1] == jogadorAtual and tabuleiro[2][2] == jogadorAtual) or
                (tabuleiro[0][2] == jogadorAtual and tabuleiro[1][1] == jogadorAtual and tabuleiro[2][0] == jogadorAtual)):
                venceu = 1


            if venceu == 1:
                print(f"\n🎉 O jogador {jogadorAtual} venceu!! 🎉")
                if jogadorAtual == "X":
                    placarX += 1
                else:
                    placarO += 1
                break


            jogadorAtual = "O" if jogadorAtual == "X" else "X"


        if acertos == totalJogadas and venceu == 0:
            print("\nDeu velha! Todos os espaços foram preenchidos.")


        print(f"\n🏆 Placar Atual 🏆\nJogador X: {placarX} | Jogador O: {placarO}")


        resposta = input("\nDeseja jogar outra rodada? (s/n): ")


    print("\nObrigado por jogar!")
    menu()




def megaSena():
    posicoes = 6
    sorteados = [random.randint(1, 60) for _ in range(posicoes)]


    sorteio = {}
    for numero in sorteados:
        if numero in sorteio:
            sorteio[numero] += 1
        else:
            sorteio[numero] = 1
   
    print("Seja bem-vindo(a) ao jogo da Mega Sena")
    print("Digite seus 6 números (de 1 a 60): ")


    numUsuario = []
    for i in range(posicoes):
        while True:
            try:
                numero = int(input(f"Número {i + 1}: "))
                if numero < 1 or numero > 60:
                    print("Número inválido! Digite um número entre 1 e 60.")
                else:
                    numUsuario.append(numero)
                    break
            except ValueError:
                print("Por favor, digite um número válido")


    print("\nNúmeros sorteados:", sorteados)
    print("Seus números:", numUsuario)
   
    acertos = 0
    for num in numUsuario:
        if num in sorteio:
            acertos += 1


    if acertos == 6:
        print("Você ganhou o prêmio principal")
    elif acertos == 5:
        print("Você acertou a quina")
    elif acertos == 4:
        print("Você ganhou a quadra")
    else:
        print("Você não teve acertos suficientes")


    jogarNovamente = input("Deseja jogar mais uma vez? (s/n): ").lower()
    if jogarNovamente == 's':
        megaSena()
    elif jogarNovamente == 'n':
        print("Até a proxima!!")
        menu()
    else:
        print("Digite o caractere correto")




def naval():
    jogarNovamente = 's'
   
    while jogarNovamente.lower() == 's':
        print("Seja bem-vindo(a) ao jogo de Batalha Naval 🌊")
        print("\nEscolha o tamanho do tabuleiro 🌊🚤")
        tabuleiro = int(input("Qual o tamanho do seu tabuleiro: "))


        print(f"\nO seu tabuleiro é de {tabuleiro} por {tabuleiro}\n")


        navios = [["🌊" for _ in range(tabuleiro)] for _ in range(tabuleiro)]
        tabuleiroVisivel = [["🌊" for _ in range(tabuleiro)] for _ in range(tabuleiro)]


        for linha in navios:
            linhas = ""
            for coluna in linha:
                linhas += coluna
            print(linhas)


        totalNavios = tabuleiro
        colocados = 0
        while colocados < totalNavios:
            i = random.randint(0, tabuleiro - 1)
            j = random.randint(0, tabuleiro - 1)


            if navios[i][j] == "🌊":
                navios[i][j] = "🚤"
                colocados += 1


        totalBombas = 3
        bombasColocadas = 0
        while bombasColocadas < totalBombas:
            i = random.randint(0, tabuleiro - 1)
            j = random.randint(0, tabuleiro - 1)
            if navios[i][j] == "🌊":
                navios[i][j] = "💣"
                bombasColocadas += 1


        acertos = 0
        while acertos < totalNavios:
            print(f"\n🏹 Tente acertar o navio! ({acertos} / {totalNavios})")
            tentativaLinha = int(input(f"Digite a linha (0 até {tabuleiro - 1}): "))
            tentativaColuna = int(input(f"Digite a coluna (0 até {tabuleiro - 1}): "))
           
            if 0 <= tentativaLinha < tabuleiro and 0 <= tentativaColuna < tabuleiro:
                if tabuleiroVisivel[tentativaLinha][tentativaColuna] in ["💥", "❌"]:
                    print("\n⚠️ Você já tentou essa posição")
                elif navios[tentativaLinha][tentativaColuna] == "🚤":
                    print("\n💥Você acertou um navio💥")
                    tabuleiroVisivel[tentativaLinha][tentativaColuna] = "💥"
                    acertos += 1
                elif navios[tentativaLinha][tentativaColuna] == "💣":
                    print("\n💣 Você acertou uma bomba! Está fora do jogo💣")
                    tabuleiroVisivel[tentativaLinha][tentativaColuna] = "💣"
                    print("\n💥 Tabuleiro revelado 💥")
                    for linha in tabuleiroVisivel:
                        linhas = ""
                        for coluna in linha:
                            linhas += coluna
                        print(linhas)
                    break
                else:
                    print("🌊 Só água por aqui...")
                    tabuleiroVisivel[tentativaLinha][tentativaColuna] = "❌"


                    naviosAoRedor = 0
                    for x in range(tentativaLinha - 1, tentativaLinha + 2):
                        for y in range(tentativaColuna - 1, tentativaColuna + 2):
                            if 0 <= x < tabuleiro and 0 <= y < tabuleiro:
                                if x != tentativaLinha or y != tentativaColuna:
                                    if navios[x][y] == "🚤":
                                        naviosAoRedor += 1
                    print(f"📡 Radar: Existem {naviosAoRedor} navio(s) ao redor dessa posição 📡")


                print("\nTabuleiro após a sua tentativa:")
                for linha in tabuleiroVisivel:
                    linhas = ""
                    for coluna in linha:
                        linhas += coluna
                    print(linhas)
            else:
                print("❌ Coordenadas inválidas. Que tal tentar dentro do tabuleiro?")
       
        if acertos == totalNavios:
            print("\n🎉 Você acertou todos os navios")


        jogarNovamente = input("Quer jogar mais uma partida? (s/n): ")
   
    print("Ah Você naufragou de vez, hein? Até a próxima")
    menu()




def dado():
    while True:
            print("\n\nSeja bem-vindo(a) ao jogo do Dado 🎲")


            lancamentos = int(input("Digite a quantidade de lançamentos de dado que você deseja fazer: "))
           
            faces = [0, 0, 0, 0, 0, 0]  
            for _ in range(lancamentos):
                dado = random.randint(1, 6)
                faces[dado - 1] += 1  
            print("\nResultado dos lançamentos:")
            for i in range(6):
                print(f"Face {i + 1}: {faces[i]} vez(es)")


            jogar_novamente = input("\nDeseja rolar os dados mais uma vez? (s/n): ")
           
            if jogar_novamente.lower() != 's':
                print("Os dados vão estar a sua espera para uma próxima partida!!")
                break




def imPar():
    placarJogador = 0
    placarSistema = 0


    print("Seja bem-vindo(a) ao jogo do Ímpar ou Par")


    while True:
        print("\n1. Impar\n2. Par\n")


        try:
            escolha = int(input("Escolha se você será Impar ou Par: "))
        except ValueError:
            print("Digite um número válido")
            continue


        match escolha:
            case 1:
                print("Você é o impar!!")
            case 2:
                print("Você é o par!!")
            case _:
                print("Você só pode ser impar ou par não os dois")
                continue


        numJogador = int(input("\nEscolha um número de 1 a 10: "))


        if numJogador > 10:
            print("Não pode roubar, escolha um número de 1 até 10")
            continue
       
        numSistema = random.randint(1, 10)
        print(f"O número escolhido pelo seu adversário: {numSistema}")


        soma = numJogador + numSistema
        print(f"A soma dos números escolhido por você e seu adversário é: {soma}")


        somaPar = soma % 2 == 0
        if somaPar:
            print("A soma é par!!!")
        else:
            print("A soma é impar!!!")


        if (escolha == 1 and soma % 2 != 0) or (escolha == 2 and soma % 2 == 0):
            print("Parabéns, você venceu 🎉✨")
            placarJogador += 1
        else:
            print("Você perdeu")
            placarSistema += 1


        print("\nPlacar atual: ")
        print(f"Você: {placarJogador} vitórias")
        print(f"Sistema: {placarSistema} vitórias")


        jogarNovamente = input("\nDeseja jogar mais uma vez? (s/n): ")


        if jogarNovamente.lower() != 's':
            print("Até a próxima!!")
            menu()  
 


def ppt():
    placarJogador = 0
    placarSistema = 0
    while True:
        print("Seja bem-vindo(a) ao jogo de Pedra, Papel ou Tesoura")
        print("1. Pedra 🪨")
        print("2. Papel 📜")
        print("3. Tesoura ✂️")
        try:
            opcaoJogador = int(input("\nEscolha uma opção: "))
        except ValueError: 
            print("Digite um número válido")
            continue
        
        match(opcaoJogador):
            case 1:
                print("Você escolheu Pedra 🪨")
            case 2:
                print("Você escolheu Papel 📜")
            case 3:
                print("Você escolheu Tesoura ✂️")
            case _:
                print("Você escolheu chuva 🌧️, e essa opção não existe, seu trapaceiro!")
                continue
                
        opcaoSistema = random.randint(1, 3)
        
        if (opcaoSistema == 1):
            print("O sistema escolheu Pedra 🪨")
        elif (opcaoSistema == 2):
            print("O sistema escolheu Papel 📜")
        else:
            print("O sistema escolheu Tesoura ✂️")
                
        if(opcaoJogador == opcaoSistema):
            print("EMPATE, ninguém venceu")
        elif(opcaoJogador == 1 and opcaoSistema == 3 or 
             opcaoJogador == 2 and opcaoSistema == 1 or 
             opcaoJogador == 3 and opcaoSistema == 2):
            print("PARABÉNS, você venceu  🎉✨")
            placarJogador += 1
        else:
            print("POXA!! Você perdeu!!")
            placarSistema += 1
        
        print("Placar\n")
        print(f"Você: {placarJogador} vitórias")
        print(f"Sistema: {placarSistema} vitórias")            

        jogarNovamente = input("\nDeseja jogar mais uma vez? (s/n): ")

        if jogarNovamente.lower() != 's':
            print("Até a próxima!!")
            menu()  
            
def adivinhacao():
    
    temas ={
        1: [
            ("Variável _ _ _ _ _ _", "global"),
            ("Para fazer uma página WEBsimples, precisa de HTML e _ _ _", "CSS"),
            ("Sim, os comandos JOINs são utilizados em banco de dados _ _ _ _ _ _ _ _ _ _ _", "relacionais"),
            ("Esse jogo é para discipllina de _ _ _ _ _ _ _" , "backend"),
            ("Desenvolvimento de _ _ _ _ _ _ _ _", "sistemas")
        ],
        
        2: [
            ("Super _ _ _ _ _ Bros", "Mario"),
            ("The _ _ _ _ _ _ of Zelsa", "legend"),
            ("_ _ _ _ _ _ Us", "amoung"),
            ("_ _ _ _ _ _", "roblox"),
            ("Free _ _ _ _", "fire")
        ],
        
        3: [
            ("Água mole em pedra dura, tanto _ _ _ _ até que fura", "bate"),
            ("Quem com ferro fere, com _ _ _ _ _ será ferido", "ferido"),
            ("Em terra de _ _ _ _, quem tem um olho é rei", "olho"),
            ("Quem _ _ _ _ _ _ sempre alcança", "espera"),
            ("Mais vale um pássaro na mão do que dois _ _ _ _ _ _", "voando")
        ],
        
        4: [
            ("New _ _ _ _", "York"),
            ("_ _ _ de Janeiro", "Rio"),
            ("Los _ _ _ _ _ _ _", "Angeles"),
            ("Buenos _ _ _ _ _", "Aires"),
            ("_ _ _ Dhabi", "Abu")
        ],
        
        5: [
            ("A sua última turnê mundial foi a _ _ _ _ _ _ _ _ _", "sweetener"),
            ("O Eternal Sunshine é o _ _ _ _ _ _ album da Ariana Grande", "setimo"),
            ("Interpretar a _ _ _ _ _ _ era o seu grande sonho", "Glinda"),
            ("O seu nome completo é Ariana Grande-_ _ _ _ _ _", "Butera"),
            ("_. _. _. Beauty é a sua marca de maquiagem", "rem")
        ]
    }
    
    while True:
        print("Seja bem-vindo(a) ao jogo da Adivinhação")
        print("Escolha um tema do Jogo de Adivinhação: ")
        print("1. Desenvolvimento de Sistemas")
        print("2. Jogos")
        print("3. Ditados Populares")
        print("4. Cidades")
        print("5. Ariana Grande")
        
        try:
            escolha = int(input("Escolha o seu tema: "))
            frases = temas[escolha]

        except (ValueError, KeyError):
            print("Digite um número de tema válido!\n")
            continue
        
        indice = random.randint(0, len(frases) - 1)
        frase, respostaCorreta = frases[indice]
        
        print(f"A frase sorteada foi: {frase}")
        resposta = input("Qual palavra completa a frase? ")
        
        if resposta.lower() == respostaCorreta.lower():
            print("Você venceu!!")
        else:
            print("Você errou FEIO")
            print(f"A resposta correta era: {respostaCorreta}")    
        
        jogarNovamente = input("\nDeseja jogar mais uma vez? (s/n): ")
        if jogarNovamente.lower() != 's':
            print("Até a próxima!!")
            menu()      
        
def menu():
    while True:
        print("== Playground ==\n")
        print("1. Jogo da Velha")
        print("2. Mega-Sena")
        print("3. Batalha Naval")
        print("4. Dado")
        print("5. Ímpar ou Par")
        print("6. Pedra, Papel ou Tesoura")
        print("7. Adivinhação")
        print("8. Sair")


        try:
            escolha = int(input("Escolha qual jogo você deseja jogar: "))
        except ValueError:
            print("Digite um número válido")
            return


        if escolha == 1:
            jogoVelha()
        elif escolha == 2:
            megaSena()
        elif escolha == 3:
            naval()
        elif escolha == 4:
            dado()
        elif escolha == 5:
            imPar()
        elif escolha == 6:
            ppt()
        elif escolha == 7:
            adivinhacao()
        elif escolha == 8:
            print("Você está saindo...")
            break
        else:
            print("Digite um jogo válido")
            continue
    
menu()

