import csv
import pandas as pd
import numpy as np
import urllib.request
from io import StringIO
import os

# Directory Configuration
directory = 'ProjectData'
if not os.path.exists(directory):
    os.makedirs(directory)

# USAID Data Retrieval and Processing
url = 'https://www.foreignassistance.gov/data_query/results.csv?&transaction_type=Obligations&country_id=524'
response = urllib.request.urlopen(url)
csv_content = response.read().decode('utf-8')
csv_file = StringIO(csv_content)
df = pd.read_csv(csv_file)

selected_columns = ['Activity Name', 'International Sector Name', 'Activity Start Date', 'Activity End Date']
subset_df = df[selected_columns]
subset_df = subset_df.drop_duplicates()

subset_df['Name of the Project'] = subset_df['Activity Name']
subset_df['Duration of the Project'] = subset_df['Activity Start Date'] + " - " + subset_df['Activity End Date']
subset_df['Sector'] = subset_df['International Sector Name']
subset_df = subset_df.drop(['Activity Name', 'International Sector Name', 'Activity Start Date', 'Activity End Date'], axis=1)

# Save the modified dataframe to a CSV in the specified directory
usa_csv_path = os.path.join(directory, 'USAID.csv')
subset_df.to_csv(usa_csv_path, index=False, quoting=csv.QUOTE_NONNUMERIC)

