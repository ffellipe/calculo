def solicitar_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def solicitar_operacao():
    print("Escolha a operação que deseja realizar:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = input("Digite o número correspondente à operação: ")
    return operacao

def realizar_calculo(num1, num2, operacao):
    if operacao == '1':
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado}")
    elif operacao == '2':
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")

def main():
    num1, num2 = solicitar_numeros()
    operacao = solicitar_operacao()
    realizar_calculo(num1, num2, operacao)

if __name__ == "__main__":
    main()
