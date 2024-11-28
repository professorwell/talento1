import os

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def somar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def subtrair(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        if b != 0:
            self.resultado = a / b
            return self.resultado
        else:
            return "Erro: Divisão por zero!"

    def mostrar_resultado(self):
        print(f"O resultado é: {self.resultado}\n")

    def finalizar(self):
        sair = int(input('''Pressione 1 para refazer operações
Pressione 2 para sair
Digite aqui: '''))

        if sair == 1:
            self.main()
        elif sair == 2:
            print("/// Finalizando o programa ///")
        else:
            print("Opção inválida. Finalizando o programa.")
    
    def exibir_opcoes(self):
        print("Escolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão\n")

    def opcao_invalida(self):
        print("Opção inválida. Tente novamente.\n")
        self.main()

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.exibir_opcoes()
        self.opcao_escolhida()

    def opcao_escolhida(self):
        try:
            escolhida = int(input("Escolha uma opção: "))
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if escolhida == 1:
                self.somar(a, b)
            elif escolhida == 2:
                self.subtrair(a, b)
            elif escolhida == 3:
                self.multiplicar(a, b)
            elif escolhida == 4:
                self.dividir(a, b)
            else:
                self.opcao_invalida()
                return
            
            self.mostrar_resultado()
            self.finalizar()

        except ValueError:
            print("Entrada inválida. Digite números válidos.")
            self.main()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.main()
