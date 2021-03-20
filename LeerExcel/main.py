import pandas as pd
import xlsxwriter
import os, json
import requests

api_key = os.environ.get('ether_API')

ex_path = 'airdrop.xlsx'
df_ex = pd.read_excel(ex_path)
exchanges = df_ex['address'].values
exchangesToken = df_ex['tokens'].values
contractAdress = "0x111111111117dC0aa78b770fA6A738034120C302"

libro = xlsxwriter.Workbook('airdropNew.xlsx')
sheet = libro.add_worksheet()

row = 0
col = 0

for i in range(100):
    print(i, ' :::: ', exchanges[i], ' >>>>>> ', exchangesToken[i])
    sheet.write(i, col, exchanges[i])
    sheet.write(i, col + 1, exchangesToken[i])
    

    url = "https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=" + contractAdress + "&address=" + exchanges[i] + "&tag=latest&apikey=" + api_key
    response = requests.get(url).text
    value = json.loads(response)
    balance = float(value['result'])/1e16

    sheet.write(i, col + 2, balance)



libro.close()
    