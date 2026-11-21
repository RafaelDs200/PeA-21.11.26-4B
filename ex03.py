################################################################
# Descrição: Calcula soma, média e quantidade de valores positivos ou zero.
# Parâmetros de entrada: Valores numéricos; um negativo encerra a leitura.
# Valores de saída: Soma, média e quantidade de valores aceitos.
# Autor: Rafael Dantas dos Santos
################################################################

total = 0.0
contador = 0

while True:
    numero = float(input("Informe um número (negativo para terminar): "))

    if numero < 0:
        break

    total += numero
    contador += 1

print(f"\nSoma dos valores: {total:.2f}")
print(f"Quantidade informada: {contador}")

if contador != 0:
    print(f"Média dos valores: {total / contador:.2f}")
else:
    print("Nenhum valor foi informado.")
