import csv
import pandas as pd
import matplotlib.pyplot as plt

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

#reading the CSV file into dataframe
df = pd.read_csv('clean.csv')
#visualizing data distributions
import seaborn as sns

#customizing Seaborn plot style
sns.set_style("whitegrid")
color_palette = 'husl'

#creating a box plot
plt.figure(figsize=(10,6))
sns.boxplot(x='Share Name', y='Close', data=df, palette='husl')

#Adding labels and title
plt.title('Distribution of Closing Prices by Share Name')
plt.xlabel('Share Name')
plt.ylabel('Closing Price')

#improving appearance
plt.xticks(rotation = 45)

#created plot
plt.tight_layout() #to ensure the labels are not cut off
plt.show()




