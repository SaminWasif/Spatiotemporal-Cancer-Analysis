import pandas as pd
import os

df = pd.DataFrame()

files = [f for f in os.listdir('.') if os.path.isfile(f) and '.csv' in f and len(f.split('_')) == 1]

for file in files:
    temp_df = pd.read_csv(file)
    df = pd.concat([df, temp_df], axis=0)

df.to_csv("subcontinent_tweets.csv", index=False)
print(len(df))
