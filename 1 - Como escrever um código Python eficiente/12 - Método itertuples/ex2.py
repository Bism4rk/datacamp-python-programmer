import pandas as pd

yankees_df = pd.read_csv('yankeesdata.csv')

run_diffs = []

def calc_run_diff(runs_scored, runs_allowed):
    run_diff = runs_scored - runs_allowed
    return run_diff

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

'''
O código acima demonstra como iterar sobre um DataFrame do Pandas usando o método itertuples(). Ele calcula a diferença de corridas (run differential) para cada linha, utilizando uma função definida pelo usuário, e armazena os resultados em uma nova coluna chamada 'RD'. A lista 'run_diffs' é usada para coletar as diferenças de corridas antes de adicioná-las ao DataFrame.
'''

