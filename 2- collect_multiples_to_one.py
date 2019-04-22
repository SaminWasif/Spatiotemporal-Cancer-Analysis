 ###Convert multiple csv files into one big file###
import json
import csv
import os
import re
from datetime import datetime
import pandas as pd

files = [f for f in os.listdir('.') if os.path.isfile(f) and '.csv' in f]
explored_countries = []

countries = dict()


for index, value in enumerate(files):
    country_name = value.split('_')[0]  # country name is the first part

    if country_name in countries:
        countries[country_name].append(index)
    else:
        countries[country_name] = [index]


for country in countries:
    df = pd.DataFrame()
    for c in countries[country]:
        temp_df = pd.read_csv(files[c])
        df = pd.concat([df, temp_df])
    res_file_name = country + '.csv'
    df.to_csv(res_file_name, index=False)
