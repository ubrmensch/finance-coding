import mysql.connector
import yfinance as yf
import datetime as dt

#Create database connection
db = mysql.connector.connect(user='myuser', password='mypassword', host='localhost', database='financial_app')
cursor = db.cursor()

#Craete a string for the symbol we wish to extra history from Yahoo Finance (you can change this to whatever symbol you wish to extract data for)
symbol = "XOM"
stock = yf.Ticker(symbol)

#Get the maximum period available for this stock (options are also #d, #mo, #y, etc...)
res = stock.history(period="max")

#This will print the result from the API call in truncated form to the command line
print(res)

#Loop through the result and enter each record into the stock_history table
for i in res.index:
    cursor.execute("INSERT INTO stock_history (`Symbol`, `Date`, `High`, `Low`, `Close`, `Volume`, `Dividends`, `Stock Splits`) VALUES (('{}'), ('{}'), ('{}'), ('{}'), ('{}'), ('{}'), ('{}'), ('{}'))".format
        (symbol, str(i), res["High"][i], res["Low"][i], res["Close"][i], res["Volume"][i], res["Dividends"][i], res["Stock Splits"][i]))

db.commit()
cursor.close()
db.close()
