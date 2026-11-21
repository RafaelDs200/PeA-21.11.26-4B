################################################################
# Descrição: Encontra o quociente inteiro usando subtrações repetidas.
# Parâmetros de entrada: Dividendo não negativo e divisor positivo.
# Valores de saída: Quociente inteiro da divisão.
# Autor: Rafael Dantas dos Santos
################################################################

numero = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

while numero < 0:
    print("Use um dividendo igual ou maior que zero.")
    numero = int(input("Dividendo: "))

while divisor <= 0:
    print("O divisor deve ser maior que zero.")
    divisor = int(input("Divisor: "))

quociente = 0
valor_restante = numero

while valor_restante >= divisor:
    valor_restante -= divisor
    quociente += 1

print("Quociente inteiro:", quociente)
