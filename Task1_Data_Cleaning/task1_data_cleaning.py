import pandas as pd
import numpy as np

df = pd.read_csv("netflix_titles.csv")
print(df.head())

print(df.info())

print(df.isnull().sum())

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")

df = df.dropna()

df = df.drop_duplicates()

df['type'] = df['type'].str.lower()
df['rating'] = df['rating'].str.upper()

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df.columns = df.columns.str.lower().str.replace(" ", "_")

print(df.dtypes)

df.to_csv("cleaned_netflix_data.csv", index=False)
print("Cleaned dataset saved successfully!")
