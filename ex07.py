################################################################
# Descrição: Gera o vetor B com a soma de 1 até cada valor de A.
# Parâmetros de entrada: Vinte números inteiros.
# Valores de saída: Os vinte resultados armazenados no vetor B.
# Autor: Rafael Dantas dos Santos
################################################################

vetor_a = []

for indice in range(20):
    entrada = int(input(f"A posição {indice + 1} recebe: "))
    vetor_a.append(entrada)

vetor_b = []

for item in vetor_a:
    resultado = 0
    atual = 1

    while atual <= item:
        resultado = resultado + atual
        atual += 1

    vetor_b.append(resultado)

print("\nValores do vetor B:")
print(vetor_b)
