def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

a = True
if __name__ == "__main__":  # pragma: no cover
    print("soma: + ")
    print("subtracao: - ")
    print("multiplicacao: * ")
    print("divisao: / ")
    print("de um espaço entre os numeros e a operacao ")
    print("Exemplo: 10 + 10")

while(a == True):
    a, operacao, b = input("digite a operacao que deseja fazer: ").split()
    a = float(a)
    b = float(b)

    if operacao == "+":
        print(soma(a, b))
    elif operacao == "-":
        print(subtracao(a, b))
    elif operacao == "*":
        print(multiplicacao(a, b))
    elif operacao == "/":
        print(divisao(a, b))
    else:
        print("operacao invalida")
