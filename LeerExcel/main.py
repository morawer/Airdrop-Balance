import pandas as pd

ex_path = 'airdrop.xlsx'
df_ex = pd.read_excel(ex_path)
exchanges = df_ex['address'].values
exchangesToken = df_ex['tokens'].values

for i in range(len(exchanges)):
    print(exchanges[i], ' >>>>>> ', exchangesToken[i])
    