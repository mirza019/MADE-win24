import pandas as pd
import requests
import tarfile
from io import BytesIO
import os
import re
import sqlite3

# URLs for the datasets
fivethirtyeight_url = "https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv"
jamesqo_url = "https://github.com/jamesqo/gun-violence-data/raw/master/DATA_01-2013_03-2018.tar.gz"

# Create data directory if it doesn't exist
data_dir = './data'
os.makedirs(data_dir, exist_ok=True)

# Function to fetch, clean, and save the FiveThirtyEight dataset
def load_fivethirtyeight_data(url):
    response = requests.get(url)
    data = pd.read_csv(BytesIO(response.content))

    # Drop rows with missing values in critical columns
    data = data.dropna(subset=['intent', 'age', 'sex', 'race', 'place', 'education'])

    # Fill remaining missing values
    data['age'] = data['age'].fillna(data['age'].median())
    data['place'] = data['place'].fillna('unknown')
    data['education'] = data['education'].fillna('unknown')

    # Standardize text columns
    data['intent'] = data['intent'].str.lower()
    data['race'] = data['race'].str.lower()
    data['place'] = data['place'].str.lower()
    data['education'] = data['education'].str.lower()

    # Select only the required columns
    data = data[['year', 'month', 'intent', 'police', 'sex', 'age', 'race', 'hispanic', 'place', 'education']]

    # Save as SQLite database and CSV file
    conn = sqlite3.connect(f'{data_dir}/fivethirtyeight_data.db')
    data.to_sql('fivethirtyeight_data', conn, if_exists='replace', index=False)
    conn.close()
    data.to_csv(f'{data_dir}/fivethirtyeight_cleaned.csv', index=False)
    return data

# Function to fetch, extract, clean, and save the Jamesqo dataset
def load_jamesqo_data(url):
    response = requests.get(url)
    with tarfile.open(fileobj=BytesIO(response.content), mode='r:gz') as tar:
        csv_file = tar.next()
        if csv_file.isfile():
            data = pd.read_csv(tar.extractfile(csv_file))

    # Drop rows with missing values in critical columns
    data = data.dropna(subset=['date', 'state', 'city_or_county', 'n_killed', 'n_injured'])

    # Convert date to datetime and extract year and month
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data = data.dropna(subset=['date'])

    # Fill missing values in non-essential columns
    data['latitude'] = data['latitude'].fillna(0)
    data['longitude'] = data['longitude'].fillna(0)
    data['gun_stolen'] = data['gun_stolen'].fillna('unknown')
    data['gun_type'] = data['gun_type'].fillna('unknown')
    data['n_guns_involved'] = data['n_guns_involved'].fillna(0)
    data['incident_characteristics'] = data['incident_characteristics'].fillna('unknown')

    # Select only the required columns
    data = data[['incident_id', 'date', 'state', 'city_or_county', 'n_killed', 'n_injured',
                 'gun_stolen', 'gun_type', 'incident_characteristics', 'latitude', 'longitude',
                 'n_guns_involved', 'year', 'month']]

    # Expand participant columns if they exist
    for col, attr in [('participant_age_group', 'age_group'),
                      ('participant_status', 'status'),
                      ('participant_type', 'type')]:
        if col in data.columns:
            expand_participant_column(data, col, attr)

    # Save as SQLite database and CSV file
    conn = sqlite3.connect(f'{data_dir}/jamesqo_data.db')
    data.to_sql('jamesqo_data', conn, if_exists='replace', index=False)
    conn.close()
    data.to_csv(f'{data_dir}/jamesqo_cleaned.csv', index=False)
    return data

# Helper functions to expand participant columns
def expand_participant_column(df, column_name, attribute_name):
    max_participants = df[column_name].apply(lambda x: len(str(x).split("||")) if pd.notnull(x) else 0).max()
    for i in range(max_participants):
        col_name = f'participant_{i}_{attribute_name}'
        df[col_name] = df[column_name].apply(lambda x: extract_participant_attribute(x, i) if pd.notnull(x) else None)

def extract_participant_attribute(entry, index):
    participants = entry.split("||")
    if index < len(participants):
        return re.sub(r"^\d+::", "", participants[index])
    return None

# Load, clean, and save both datasets as SQLite databases and CSV files
fivethirtyeight_data = load_fivethirtyeight_data(fivethirtyeight_url)
jamesqo_data = load_jamesqo_data(jamesqo_url)

print("Datasets loaded, cleaned, and saved successfully as SQLite databases and CSV files!")

