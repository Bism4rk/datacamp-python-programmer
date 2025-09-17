import pandas as pd

giants_df = pd.read_csv('giantsdata.csv')

def calc_run_diff(runs_scored, runs_allowed):
    return runs_scored - runs_allowed

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

'''
O código acima demonstra 'como iterar sobre um DataFrame do Pandas usando o método iterrows(). Ele calcula a diferença de corridas (run differential) para cada linha, utilizando uma função definida pelo usuário, e armazena os resultados em uma nova coluna chamada 'RD'. A lista 'run_diffs' é usada para coletar as diferenças de corridas antes de adicioná-las ao DataFrame.
'''