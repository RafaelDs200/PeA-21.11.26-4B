################################################################
# Descrição: Calcula a área de cada cômodo e a área total da casa.
# Parâmetros de entrada: Nome, largura e comprimento dos cômodos.
# Valores de saída: Área individual e soma das áreas em metros quadrados.
# Autor: Rafael Dantas dos Santos
################################################################

soma_areas = 0.0
resposta = "S"

while resposta == "S":
    comodo = input("\nQual é o cômodo? ")
    medida_largura = float(input("Largura (m): "))
    medida_comprimento = float(input("Comprimento (m): "))

    resultado = medida_largura * medida_comprimento
    soma_areas += resultado

    print(f"A área de {comodo} é {resultado:.2f} m²")
    resposta = input("Adicionar outro cômodo? (S/N): ").strip().upper()

print(f"\nÁrea total da residência: {soma_areas:.2f} m²")
