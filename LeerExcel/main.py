import pandas as pd
import xlsxwriter

ex_path = 'airdrop.xlsx'
df_ex = pd.read_excel(ex_path)
exchanges = df_ex['address'].values
exchangesToken = df_ex['tokens'].values

libro = xlsxwriter.Workbook('airdropNew.xlsx')
sheet = libro.add_worksheet()

row = 0
col = 0



for i in range(len(exchanges)):
    print(i, ' :::: ', exchanges[i], ' >>>>>> ', exchangesToken[i])
    sheet.write(i, col, exchanges[i])
    sheet.write(i, col + 1, exchangesToken[i])
    sheet.write(i, col + 2, 'Ya se escribir en el Excel')

libro.close()
    