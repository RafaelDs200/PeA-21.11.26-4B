################################################################
# Descrição: Soma os grãos colocados nas 64 casas do tabuleiro.
# Parâmetros de entrada: Nenhum.
# Valores de saída: Grãos por casa e total geral.
# Autor: Rafael Dantas dos Santos
################################################################

casa = 1
quantidade_na_casa = 1
acumulado = 0

while casa <= 64:
    acumulado += quantidade_na_casa
    print(f"{casa}ª casa -> {quantidade_na_casa} grãos")
    quantidade_na_casa *= 2
    casa += 1

print("\nQuantidade total de grãos:", acumulado)
