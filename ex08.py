################################################################
# Descrição: Calcula os elementos de B usando a posição dos valores de A.
# Parâmetros de entrada: Quinze números reais.
# Valores de saída: Vetor B com os valores transformados.
# Autor: Rafael Dantas dos Santos
################################################################

vetor_a = []

for numero in range(15):
    dado = float(input(f"Digite o valor da posição {numero + 1}: "))
    vetor_a.append(dado)

vetor_b = []
posicao = 1

for dado in vetor_a:
    if posicao % 2 == 0:
        transformado = dado / 2
    else:
        transformado = dado * 1.5

    vetor_b.append(transformado)
    posicao += 1

print("\nVetor B:", vetor_b)
