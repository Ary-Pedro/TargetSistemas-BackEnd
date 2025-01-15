import xml.etree.ElementTree as ET

def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    return f"Soma dos números: {SOMA}"

def verificar_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    pertence = b == num or num == 0
    return f"O número {num} pertence à sequência de Fibonacci: {pertence}"

def carregar_dados_do_xml():
    try:# tentativa de consultar o arquivo dados.xml
        with open('dados.xml', 'r', encoding='utf-8') as file:
            xml_content = file.read().strip()  # limpar dados para uso

        # Corrige possíveis erros de formatação
        if not xml_content.startswith('<root>'):
            xml_content = f"<root>{xml_content}</root>"

        # Parseia o conteúdo do XML
        tree = ET.ElementTree(ET.fromstring(xml_content))
        root = tree.getroot()

        # Extrai os valores de faturamento diário a partir da tag <valor>
        faturamento_diario = [float(row.find('valor').text) for row in root.findall('row')]
        return faturamento_diario

    except ET.ParseError as e:
        print(f"Erro ao processar o XML: {e}")
        return []

def calcular_faturamento():
    # Carrega os dados do XML
    faturamento_diario = carregar_dados_do_xml()
    
    if not faturamento_diario:
        return "Erro ao carregar os dados do faturamento."

    # Calcula os valores de maior, menor, média e dias acima da média
    maior = faturamento_diario[0]
    menor = float('inf')
    soma = 0
    dias_acima_da_media = 0
    dias_validos = 0

    for valor in faturamento_diario:
        if valor > maior:
            maior = valor
        if valor > 0 and valor < menor:
            menor = valor
        if valor > 0:
            soma += valor
            dias_validos += 1

    media = soma / dias_validos

    for valor in faturamento_diario:
        if valor > media:
            dias_acima_da_media += 1

    # Exibindo os cálculos
    print(f"Média: {media}")
    print(f"Dias acima da média: {dias_acima_da_media}")
    
    return (f"Maior faturamento: {maior}\n"
            f"Menor faturamento: {menor}\n"
            f"Dias acima da média: {dias_acima_da_media}")

def calcular_percentual():
    faturamento_estados = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}
    total = 0
    for valor in faturamento_estados.values():
        total += valor

    percentuais = {}
    for estado, valor in faturamento_estados.items():
        percentuais[estado] = (valor / total) * 100

    resultado = ""
    for estado, percentual in percentuais.items():
        resultado += f"{estado}: {percentual:.2f}%\n"

    return resultado.strip()


def inverter_string(texto):
    texto_invertido = texto[::-1]
    return f"Texto invertido: {texto_invertido}"
