################################################################
# Descrição: Preenche A e B com regras diferentes e junta os dois vetores.
# Parâmetros de entrada: Doze valores válidos para A e doze para B.
# Valores de saída: Vetor C contendo os 24 valores de A e B.
# Autor: Rafael Dantas dos Santos
################################################################

vetor_a = []
vetor_b = []

print("Preencha A com números divisíveis por 2 ou por 3.")
while len(vetor_a) < 12:
    candidato = int(input("Valor para A: "))

    if candidato % 2 == 0 or candidato % 3 == 0:
        vetor_a.append(candidato)
    else:
        print("Esse valor não atende à regra. Tente novamente.")

print("\nPreencha B com números que não sejam múltiplos de 5.")
while len(vetor_b) < 12:
    candidato = int(input("Valor para B: "))

    if candidato % 5 == 0:
        print("Múltiplos de 5 não são permitidos.")
    else:
        vetor_b.append(candidato)

vetor_c = []
vetor_c.extend(vetor_a)
vetor_c.extend(vetor_b)

print("\nElementos do vetor C:")
for elemento in vetor_c:
    print(elemento, end=" | ")
print()
