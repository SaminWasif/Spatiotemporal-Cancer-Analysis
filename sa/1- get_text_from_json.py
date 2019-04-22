import json
import csv
import os
import re
from datetime import datetime

files = [f for f in os.listdir('.') if os.path.isfile(f) and '.json' in f]

for file in files:
    country_name = file.split('_')[0]  # country name is the first part
    disease_name = file.split('_')[1]

    jsonFile = open(file, 'r')  # open json file
    values = json.load(jsonFile)
    jsonFile.close()

    res_file_name = country_name + '_' + disease_name + '.csv'
    csvFile = open(res_file_name, 'w', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    # header
    csvWriter.writerow(["tweet_text", "month_of_tweet"])

    for i in range(len(values)):
        texts = values[i]["text"]
        texts = re.sub(r"http\S+", "", texts)  # removes links
        texts = re.sub(r"RT", "", texts)  # removes RT
        texts = re.sub(r"@\S+", "", texts)  # removes tags @NAME
        texts = ' '.join(texts.split())  # removes extra white spaces

        timestamp = values[i]["timestamp"]
        month_of_tweet = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S").month

        csvWriter.writerow([texts, month_of_tweet])  # write to csv

    csvFile.close()
print("Done")
