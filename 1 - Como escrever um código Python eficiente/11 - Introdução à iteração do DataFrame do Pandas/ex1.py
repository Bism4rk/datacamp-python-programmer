import pandas as pd

pit_df = pd.read_csv('pittsburghdata.csv')

# Iterate over pit_df and print each index variable, row, and row type
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(i))
    print(type(row))

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

'''
O código acima demonstra como iterar sobre um DataFrame do Pandas usando o método iterrows(). Ele imprime o índice, a linha e os tipos de dados do índice e da linha. Além disso, ele mostra como cada linha é representada como uma tupla contendo o índice e a série correspondente.
'''