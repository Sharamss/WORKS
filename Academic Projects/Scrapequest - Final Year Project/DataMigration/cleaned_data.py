import pandas as pd

def load_data(file_path):
    """ Load data from a CSV file """
    return pd.read_csv(file_path)

def clean_data(df):
    """ Clean the dataframe """
    # Remove duplicate rows
    df = df.drop_duplicates()
    # Drop rows where all elements are missing
    df = df.dropna(how='all')
    # Replace missing values with a placeholder or an interpolation
    df = df.fillna(method='ffill').fillna('Unknown')
    return df

def test_cleaning(original_df, cleaned_df):
    """ Perform tests to ensure data cleaning was successful """
    assert len(cleaned_df) <= len(original_df), "Cleaned data should not have more rows than original."
    assert cleaned_df.isna().sum().max() == 0, "No NaN values should exist in cleaned data."
    print( path + " Tests passed successfully!")

#usage
directory = '../ScrapeBots/ProjectData/'
file_names = ['ADB.csv', 'JICA.csv', 'SDC.csv', 'UKAID.csv', 'UNDP.csv', 'UNFAO.csv', 'USAID.csv', 'WB.csv']
file_paths = [directory + file_name for file_name in file_names]
all_dataframes = []

for path in file_paths:
    df = load_data(path)
    cleaned_df = clean_data(df)
    test_cleaning(df, cleaned_df)
    all_dataframes.append(cleaned_df)
