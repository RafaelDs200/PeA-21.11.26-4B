################################################################
# Descrição: Conta os ímpares de um vetor e calcula sua porcentagem.
# Parâmetros de entrada: Dez números inteiros.
# Valores de saída: Quantidade de ímpares e percentual sobre os dez valores.
# Autor: Rafael Dantas dos Santos
################################################################

numeros = []

for contador in range(10):
    recebido = int(input(f"Número {contador + 1}: "))
    numeros.append(recebido)

impares = 0
for recebido in numeros:
    if recebido % 2 != 0:
        impares += 1

taxa = impares * 100 / len(numeros)

print(f"\nForam encontrados {impares} números ímpares.")
print(f"Percentual de ímpares: {taxa:.1f}%")
