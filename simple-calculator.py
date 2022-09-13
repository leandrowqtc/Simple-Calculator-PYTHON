opcao = 0

def somar(n1,n2):
    print('A soma dos numeros é: ', n1 + n2)
    print('')

def subtrair(n1,n2):
    print("A soma dos valores é: ", n1 - n2)
    print("")

def multiplicar(n1,n2):
    print("A multiplicação dos valores é: ", n1 * n2)
    print("")

def dividir(n1,n2):
    print("A divisão dos valores é: ", n1 / n2)
    print("")

# Rotina Principal
print("Programa para calcular valores, iniciado!")
print("")

while opcao != 5:
    print("1 - Para soma de valores")
    print("2 - Para subtração de valores")
    print("3 - Para multiplicação de valores")
    print("4 - Para divisão de valores")
    print("5 - Para finalizar o programa!")
    print("")

    opcao = int(input("Digite a operação desejada: "))

    if opcao == 5:
        print("O programa será finalizado, obrigado por nos utilizar!")
    
    elif opcao >= 1 and opcao <= 5:
        print("Agora é necessário digitar os valores para o calculo!")
        n1 = float(input("Escreva o primeiro valor: "))
        n2 = float(input("Digite outro valor: "))
        print("")

        if opcao == 1:
            somar(n1,n2)
        elif opcao == 2:
            subtrair(n1,n1)
        elif opcao == 3:
            multiplicar(n1,n2)
        elif opcao == 4:
            dividir(n1,n2)
    
    else:
        print("Valor invalido!")
        print("")
