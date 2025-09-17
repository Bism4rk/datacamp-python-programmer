import pandas as pd

rangers_df = pd.read_csv('rangersdata.csv')

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

'''
O código acima demonstra como iterar sobre um DataFrame do Pandas usando o método itertuples(). Ele imprime o índice, o ano e o número de vitórias de cada linha, verificando se a equipe fez os playoffs. 
'''