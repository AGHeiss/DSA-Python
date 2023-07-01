# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

import math
def calculadora():
    print("\n******************* Calculadora em Python *******************")

    valor1 = input("Digite o primeiro valor ou vários valores separados por vírgula: ")
    if ',' in valor1:
        valor1 = calculadora_lista(valor1)
        print(valor1)
        print("OPERAÇÃO DISPONÍVEL: \nMULTIPLICAÇÃO '*'\nDIVISÃO '/'\nSUBTRAÇÃO '-'\nSOMA '+'")
        operacao = input("Digite a operacao: ")
        if operacao == '*':
            print('MULTIPLICAÇÃO DOS PRIMEIROS VALORES')
            valor2 = float(input('Digite o segundo valor(produto): '))
            multiplicacao = map(lambda m: m * valor2, valor1)
            print(f'Primeiro valor: {valor1}\n Segundo valor(produto): {valor2}\n Resultado da multiplicação: {list(multiplicacao)}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        elif operacao == '/':
            print('DIVISÃO DOS PRIMEIROS VALORES')
            valor2 = float(input('Digite o segundo valor: '))
            divisao = map(lambda d: d / valor2, valor1)
            print(f'Primeiro valor: {valor1}\nSegundo valor: {valor2}\nResultado da divisão: {list(divisao)}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        elif operacao == '-':
            print('SUBTRAÇÃO DOS PRIMEIROS VALORES')
            valor2 = float(input('Digite o segundo valor: '))
            subtracao = map(lambda s: s - valor2, valor1)
            print(f'Primeiro valor: {valor1}\nSegundo valor: {valor2}\nResultado da subtração: {list(subtracao)}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        elif operacao == '+':
            print('SOMA DOS PRIMEIROS VALORES')
            valor2 = float(input('Digite o segundo valor: '))
            soma = map(lambda s: s + valor2, valor1)
            print(f'Primeiro valor: {valor1}\nSegundo valor: {valor2}\n Resultado da soma: {list(soma)}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        else:
            print('Operação inválida, tente novamente.')
            calculadora()

    else:
        valor1 = float(valor1)
        print(f"Você digitou {valor1}.")
        print("Escolha a operação que você quer realizar:\n")
        print("Para soma digite '+'")
        print("Para subtração digite '-'")
        print("Para divisão digite '/'")
        print("Para multiplicação digite '*'")
        print("Para potenciação digite '**'")
        print("Para raiz quadrada digite 'sqrt'")
        operacao = input('Digite a operação: ')
        if operacao == '+':
            print('SOMA')
            valor2 = float(input('Digite o segundo valor: '))
            print(f'Primeiro valor: {valor1}\nSegundo valor: {valor2}')
            soma = valor1 + valor2
            print(f'O resultado da operação é: {soma}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')

        elif operacao == '-':
            print('SUBTRAÇÃO')
            valor2 = float(input('Digite o segundo valor: '))
            print(f'Primeiro valor: {valor1}\nSegundo valor: {valor2}')
            subtracao = valor1 - valor2
            print(f'O resultado da operação é: {subtracao}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        elif operacao == '/':
            print('DIVISÃO')
            valor2 = float(input('Digite o segundo valor: '))
            print(f'Primeiro valor: {valor1}\nSegundo valor: {valor2}')
            divisao = valor1 / valor2
            print(f'O resultado da operação é: {divisao}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        elif operacao == '*':
            print('MULTIPLICAÇÃO')
            valor2 = float(input('Digite o segundo valor: '))
            print(f'Primeiro valor: {valor1}\nSegundo valor: {valor2}')
            multiplicacao = valor1 * valor2
            print(f'O resultado da operação é: {multiplicacao}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        elif operacao == '**':
            print('POTENCIAÇÃO')
            valor2 = float(input('Digite o número do expoente: '))
            print(f'Primeiro valor: {valor1}\nSegundo valor(expoente): {valor2}')
            potenciacao = valor1 ** valor2
            print(f'O resultado da operação é: {potenciacao}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        elif operacao == 'sqrt':
            print('RAIZ QUADRADA')
            raiz = math.sqrt(valor1)
            print(f'A raiz quadrada de {valor1} é igual a: {raiz}')
            menu = input('Quer fazer mais uma operação? s/n ')
            if menu.upper() == 'S' or menu.upper() == 'SIM':
                calculadora()
            else:
                print('Obrigado por usar a calculadora simples em Python\nFIM')
        else:
            print('Operação inválida, tente novamente.')
            calculadora()
    
def calculadora_lista(lista):
    lista1 = []
    valores = lista.split(',')
    for i in valores:
        i = float(i)
        lista1.append(i)
    return lista1



calculadora()




