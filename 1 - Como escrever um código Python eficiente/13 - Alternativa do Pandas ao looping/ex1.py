import pandas as pd

rays_df = pd.read_csv("rays.csv")

def text_playoffs(playoffs):
    if playoffs == 0:
        return "No"
    elif playoffs == 1:
        return "Yes"
    else:
        return "Unknown"

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

'''
O código acima demonstra como aplicar funções de agregação e transformação em um DataFrame do Pandas de forma eficiente, evitando loops explícitos. A função `apply` permite que você aplique uma função ao longo de um eixo do DataFrame (linhas ou colunas), facilitando operações complexas de forma concisa e legível.
'''