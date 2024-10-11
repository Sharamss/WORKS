import csv

#opening the csv file for reading

with open('Week-9 Ass-1 Data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #Creating a new CSV file to write the seperated data
    with open('clean.csv', 'w', newline='') as clean_output:
        csv_writer = csv.writer(clean_output)
        
        for row in csv_reader: 
            #data in a single column is split via comma
            data = row[0].split(',')
            
            #writing sperated data to the output file
            csv_writer.writerow(data)

#analyzing the stock data
import pandas as pd
import matplotlib.pyplot as plt

#reading the CSV file into dataframe

df = pd.read_csv('clean.csv')

#extracting the 'Date' and 'Close' columns

dates = pd.to_datetime(df['Date'])
closing_price = df['Close']

#Creating a line plot
plt.figure(figsize=(12, 6))
plt.plot(dates,closing_price, label='Closing Prices', color = 'blue', linewidth = 2 )

#Customizing the plot
plt.title('Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.legend()

#The created plot
plt.show()