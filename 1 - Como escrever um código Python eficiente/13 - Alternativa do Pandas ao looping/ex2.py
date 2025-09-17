import pandas as pd

dbacks_df = pd.read_csv("dbacks.csv")

def calc_win_perc(wins, games):
    if games == 0:
        return 0
    return wins / games

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

'''
O código acima demonstra como calcular a porcentagem de vitórias de uma equipe de beisebol usando o Pandas. Ele lê os dados de um arquivo CSV, aplica uma função para calcular a porcentagem de vitórias e adiciona essa informação de volta ao DataFrame. Isso ilustra como o Pandas pode ser usado para realizar operações complexas de forma eficiente e legível, evitando loops explícitos.
'''