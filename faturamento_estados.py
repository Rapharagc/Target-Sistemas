sales = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}


total_sales = 0
for value in sales.values():
    total_sales += value


percentage_representation = {}
for state, value in sales.items():
    percentage = (value / total_sales) * 100
    percentage_representation[state] = percentage


for state, percentage in percentage_representation.items():
    print(f"{state}: {percentage:.2f}%")