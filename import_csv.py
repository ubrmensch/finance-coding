import pandas as pd
import datetime as dt
import mysql.connector

#Create a datbase connection to the local MySQL database.  Your username / password will be set by you.
db = mysql.connector.connect(user='myuser', password='mypassword', host='localhost', database='financial_app')
cursor = db.cursor()

#read in the contents of the csv file downloaded from the Nasdaq website.
res = pd.read_csv('stock_symbols.csv')

#create a pythong datatime string so we can populate the Last_Refresh column in the table, which is a MySQL column of DATA-TIME type.  We will use this column to track when the
#stock symbol was last refreshed.
today =  dt.datetime.strftime(dt.datetime.today(), "%Y-%m-%d %H:%M:%S")

#loop through the panda res variable (created from read_csv method above), and create an insert statement to add each row to our database.
for i in res.index:
    #Country =
    cursor.execute("INSERT INTO stock_symbols (`Symbol`, `Name`, `Market_Cap`, `Country`, `IPO_Year`, `Sector`, `Industry`, `Volume`, `Last_Refresh`) VALUES ((\"{}\"), (\"{}\"), (\"{}\"), (\"{}\"), (\"{}\"), (\"{}\"), (\"{}\"), (\"{}\"), (\"{}\"))".format
    (res["Symbol"][i] if not(str(res['Symbol'][i])=="nan") else "",
    res["Name"][i] if not(str(res['Name'][i])=="nan") else "",
    str(res["Market Cap"][i]) if not(str(res['Market Cap'][i])=="nan") else "0",
    res["Country"][i] if not(str(res['Country'][i])=="nan") else "",
    res["IPO Year"][i] if not(str(res['IPO Year'][i])=="nan") else "",
    res["Sector"][i] if not(str(res['Sector'][i])=="nan") else "",
    res["Industry"][i] if not(str(res['Industry'][i])=="nan") else "",
    res["Volume"][i] if not(str(res['Volume'][i])=="nan") else "0",
    today))
    db.commit()

cursor.close()
db.close()
