import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def processa_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)

    valores = []

    for dia in dados:
        if dia['valor'] is not None and dia['valor'] > 0:
            valores.append(dia['valor'])
    

    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)

    
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    
    print(f"Menor valor do mês: {locale.currency(menor_valor, grouping=True)}")
    print(f"Maior valor do mês: {locale.currency(maior_valor, grouping=True)}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")


processa_faturamento('dados.json')