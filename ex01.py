################################################################
# Descrição: Exibe as potências de 3 do expoente 0 ao 15.
# Parâmetros de entrada: Nenhum.
# Valores de saída: Os resultados das potências de base 3.
# Autor: Rafael Dantas dos Santos
################################################################

potencia = 1
expoente = 0

while expoente <= 15:
    print(f"3^{expoente} = {potencia}")
    potencia *= 3
    expoente += 1
