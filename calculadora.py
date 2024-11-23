# Função para adicionar dois números
def adicionar(x, y):
    return x + y

# Função para subtrair o segundo número do primeiro
def subtrair(x, y):
    return x - y

# Função para multiplicar dois números
def multiplicar(x, y):
    return x * y

# Função para dividir o primeiro número pelo segundo
def dividir(x, y):
    # Verifica se o divisor é zero para evitar divisão por zero
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

# Função principal da calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    # Recebe a entrada do usuário para selecionar a operação
    escolha = input("Digite a escolha (1/2/3/4): ")
    
    # Verifica se a escolha é válida
    if escolha not in ['1', '2', '3', '4']:
        print("Escolha inválida!")
        return
    
    # Recebe os números do usuário e verifica se são válidos
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite números válidos.")
        return
    
    # Realiza a operação com base na escolha do usuário
    if escolha == '1':
        print(f"{num1} + {num2} = {adicionar(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")

# Chama a função principal da calculadora
calculadora()
