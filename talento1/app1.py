import os

def entrada_inteira(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido.\n")

def finalizar():
    sair = entrada_inteira('''\nPressione 1 para refazer operações
Pressione 2 para sair
Digite aqui: ''')
    
    if sair == 1:
        main()
    elif sair == 2:
        print("\n/// Finalizando programa ///\n")
        exit()

def soma():
    a = entrada_inteira('Digite um número: ')
    b = entrada_inteira('Digite outro número: ')
    print('\nA soma resultou em:', a + b, '\n')
    finalizar()

def subtracao():
    a = entrada_inteira('Digite um número: ')
    b = entrada_inteira('Digite outro número: ')
    print('\nA subtração resultou em:', a - b, '\n')
    finalizar()

def multiplicacao():
    a = entrada_inteira('Digite um número: ')
    b = entrada_inteira('Digite outro número: ')
    print('\nA multiplicação resultou em:', a * b, '\n')
    finalizar()

def divisao():
    a = entrada_inteira('Digite um número: ')
    while True:
        b = entrada_inteira('Digite um número para divisão: ')
        if b == 0:
            print("Divisão por zero não é permitida. Tente novamente.\n")
        else:
            break
    print('\nA divisão resultou em:', a / b, '\n')
    finalizar()

def exibir_opcoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Calculadora ===\n")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair\n")

def opcao_escolhida():
    escolhida = entrada_inteira('Escolha uma opção: ')
    
    if escolhida == 1:
        soma()
    elif escolhida == 2:
        subtracao()
    elif escolhida == 3:
        multiplicacao()
    elif escolhida == 4:
        divisao()
    elif escolhida == 5:
        print("\nFinalizando o programa...")
        exit()
    else:
        print("Opção inválida!\n")
        main()

def main():
    exibir_opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()
