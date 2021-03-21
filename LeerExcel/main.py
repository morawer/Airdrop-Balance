import pandas as pd
import xlsxwriter, os, json, requests

#The token is a system variable.
api_key = os.environ.get('ether_API')

#This path is the localitation of our excel file.
ex_path = 'airdrop.xlsx'
df_ex = pd.read_excel(ex_path)
exchanges = df_ex['address'].values
exchangesToken = df_ex['tokens'].values

#This variable is the contract adrees of the token.
contractAdress = "0x111111111117dC0aa78b770fA6A738034120C302"

#We create  a new Excel file and new sheet.
libro = xlsxwriter.Workbook('airdropNew.xlsx')
sheet = libro.add_worksheet()

row = 0
col = 0

#We write the title in the first cell of each column
sheet.write(0, col, "Wallet")
sheet.write(0, col + 1, "Tokens")
sheet.write(0, col + 2, "Balance")
sheet.write(0, col + 3, "Percent")

#Run the array wallets.
for i in range(len(exchanges)):
    
    url = "https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=" + contractAdress + "&address=" + exchanges[i] + "&tag=latest&apikey=" + api_key
    response = requests.get(url).text
    value = json.loads(response)
    balance = float(value['result'])/1e16

    op = (balance/exchangesToken[i])*100
    porcentaje =  str("{0:.2f}".format(op)) + '%'
    
#Write the values in the Excel file and print in the terminal.
    print(i+1, ' :::: ', exchanges[i], ' >>>>>> ', exchangesToken[i])
    sheet.write(i+1, col, exchanges[i])
    sheet.write(i+1, col + 1, exchangesToken[i])
    sheet.write(i+1, col + 2, balance)
    sheet.write(i+1, col +3, porcentaje)

libro.close()
    