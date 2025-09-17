import pandas as pd

baseball_df = pd.read_csv("baseball.csv")

def calc_win_perc(wins, games):
    if games == 0:
        return 0
    return wins / games

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

'''
O código acima demonstra como calcular a porcentagem de vitórias de uma equipe de beisebol usando o Pandas. Ele lê os dados de um arquivo CSV, aplica uma função para calcular a porcentagem de vitórias e adiciona essa informação de volta ao DataFrame. Isso ilustra como o Pandas pode ser usado para realizar operações complexas de forma eficiente e legível, evitando loops explícitos. O que torna esse processo ainda mais eficiente é o uso de operações vetorizadas do NumPy, que são otimizadas para desempenho.
'''