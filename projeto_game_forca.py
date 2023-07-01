# JOGO DA FORCA

import random
import os

def palavra():
    limpa_tela()
    print('Seja bem vindo ao jogo da forca')
    print('Tente acertar a palavra!\n')
    palavras = ['morango', 'abacaxi', 'uva', 'abacate', 'elefante', 'leite', 'vermelho', 'laranja']
    letra_errada = []
    sistema = random.choice(palavras)
    caractere = []
    caractere = ["_" for letra in sistema]
    print(caractere)
    tentativas = 6
    while tentativas > 0:
        print(f'\nVocê tem {tentativas} tentativas.')
        print(f'Letras erradas: {letra_errada}')
        game = input('Digite uma letra: ')
        if len(game) > 1:
            print('\nVocê digitou mais que uma letra! Quer tentar adivinhar a palavra inteira?\n')
            adivinha = input('Digite a palavra inteira: ')
            adivinha = adivinha.lower()
            if adivinha == sistema:
                print(f'\nParabéns! Você ganhou! A palavra é {sistema}.\n')
                play = input('Quer jogar de novo?? s/n ')
                play = play.upper()
                if play == 'S' or play == 'SIM':
                    palavra()
                else:
                    print('\nFIM DE JOGO!\n')          
                break
            else:
                print(f'\nVocê errou!! Você digitou: {adivinha}. Não é essa palavra!\n')
                tentativas -= 1
                print(caractere)
                continue
        elif game in letra_errada or game in caractere:
            print('\nVocê já tentou essa letra, tente novamente\n')
            print(caractere, '\n')
            continue
        elif game.lower() in sistema:
            print('\nParabéns você acertou! Tente novamente.\n')
            for i,letra in enumerate(sistema):
                if letra == game.lower():
                    caractere[i] = caractere[i].replace('_', letra)
            print(caractere)
            if '_' not in caractere:
                print(f'\nParabéns! Você ganhou! A palavra é {sistema}.\n')
                play = input('Quer jogar de novo?? s/n ')
                play = play.upper()
                if play == 'S' or play == 'SIM':
                    palavra()
                else:
                    print('\nFIM DE JOGO!\n')          
                break
        else:
            print('\nEssa letra não faz parte da palavra, sinto muito.\n')
            letra_errada.append(game)
            tentativas -= 1
            print(caractere)
    if tentativas == 0:
        print('\nGAME OVER\n')
        play = input('Quer jogar de novo?? s/n ')
        play = play.upper()
        if play == 'S' or play == 'SIM':
            palavra()
        else:
            print('\nFIM DE JOGO!\n')

def limpa_tela():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

palavra()


