################################################################
# Descrição: Analisa vinte temperaturas registradas em graus Celsius.
# Parâmetros de entrada: Vinte temperaturas reais.
# Valores de saída: Menor temperatura, maior temperatura e média.
# Autor: Rafael Dantas dos Santos
################################################################

leituras = []

for posicao in range(1, 21):
    leitura = float(input(f"Temperatura {posicao}: "))
    leituras.append(leitura)

menor_valor = min(leituras)
maior_valor = max(leituras)
media_valores = sum(leituras) / len(leituras)

print(f"Menor temperatura: {menor_valor:.1f} °C")
print(f"Maior temperatura: {maior_valor:.1f} °C")
print(f"Média: {media_valores:.2f} °C")
