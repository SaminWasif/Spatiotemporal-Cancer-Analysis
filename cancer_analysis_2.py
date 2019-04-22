import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
import os


# step 1: Add sentiment of tweets to loaded DataFrame

def add_sentiment_to_df(df):
    sent = []
    for i in range(len(df)):
        analysis = TextBlob(str(df["tweet_text"].iloc[i]))
        if analysis.sentiment.polarity >= 0.1:
            sent.append('positive')
        elif analysis.sentiment.polarity <= -0.1:
            sent.append('negative')
        else:
            sent.append('neutral')
    df["sentiment"] = sent
    return df


# step 2: Check for each cancer type in tweets:


cancer_types = ('breast', 'skin', 'lung', 'prostate', 'colorectal', 'bladder', 'kidney', 'brain',
                'blood', 'liver', 'thyroid', 'pancreatic', 'stomach', 'melanoma', 'lymphoma',
                'leukemia', 'uterus', 'overy', 'bone', 'tongue', 'testis')


def cancer_types_counts(df):
    cancer_types_count = [0] * 21  # will hold the counts of each type

    for i in range(len(df)):

        if "breast" in df.tweet_text.iloc[i]:
            cancer_types_count[0] += 1
        if "skin" in df.tweet_text.iloc[i]:
            cancer_types_count[1] += 1
        if "lung" in df.tweet_text.iloc[i]:
            cancer_types_count[2] += 1
        if "prostate" in df.tweet_text.iloc[i]:
            cancer_types_count[3] += 1
        if "colorectal" in df.tweet_text.iloc[i]:
            cancer_types_count[4] += 1
        if "bladder" in df.tweet_text.iloc[i]:
            cancer_types_count[5] += 1
        if "kidney" in df.tweet_text.iloc[i]:
            cancer_types_count[6] += 1
        if "brain" in df.tweet_text.iloc[i]:
            cancer_types_count[7] += 1
        if "blood" in df.tweet_text.iloc[i]:
            cancer_types_count[8] += 1
        if "liver" in df.tweet_text.iloc[i]:
            cancer_types_count[9] += 1
        if "thyroid" in df.tweet_text.iloc[i]:
            cancer_types_count[10] += 1
        if "pancreatic" in df.tweet_text.iloc[i]:
            cancer_types_count[11] += 1
        if "stomach" in df.tweet_text.iloc[i]:
            cancer_types_count[12] += 1
        if "melanoma" in df.tweet_text.iloc[i]:
            cancer_types_count[13] += 1
        if "lymphoma" in df.tweet_text.iloc[i]:
            cancer_types_count[14] += 1
        if "leukemia" in df.tweet_text.iloc[i]:
            cancer_types_count[15] += 1
        if "uterus" in df.tweet_text.iloc[i]:
            cancer_types_count[16] += 1
        if "overy" in df.tweet_text.iloc[i]:
            cancer_types_count[17] += 1
        if "bone" in df.tweet_text.iloc[i]:
            cancer_types_count[18] += 1
        if "tongue" in df.tweet_text.iloc[i]:
            cancer_types_count[19] += 1
        if "testis" in df.tweet_text.iloc[i]:
            cancer_types_count[20] += 1

    return cancer_types_count


# step3: plotting the cancer types counts

def plot_data_with_labels(labels, data, graph_title):
    x = np.arange(len(labels))
    plt.bar(x, data, width=0.3, color='#2a2c5a')
    plt.title(graph_title)
    plt.xticks(x, labels, rotation=90)
    plt.show()


# step 4: tweets distribution over months

months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')


def tweets_distribution_over_months(df):
    monthly_distribution = [0] * 12

    for i in range(len(df)):
        if df.month_of_tweet.iloc[i] == 1:
            monthly_distribution[0] += 1
        elif df.month_of_tweet.iloc[i] == 2:
            monthly_distribution[1] += 1
        elif df.month_of_tweet.iloc[i] == 3:
            monthly_distribution[2] += 1
        elif df.month_of_tweet.iloc[i] == 4:
            monthly_distribution[3] += 1
        elif df.month_of_tweet.iloc[i] == 5:
            monthly_distribution[4] += 1
        elif df.month_of_tweet.iloc[i] == 6:
            monthly_distribution[5] += 1
        elif df.month_of_tweet.iloc[i] == 7:
            monthly_distribution[6] += 1
        elif df.month_of_tweet.iloc[i] == 8:
            monthly_distribution[7] += 1
        elif df.month_of_tweet.iloc[i] == 9:
            monthly_distribution[8] += 1
        elif df.month_of_tweet.iloc[i] == 10:
            monthly_distribution[9] += 1
        elif df.month_of_tweet.iloc[i] == 11:
            monthly_distribution[10] += 1
        elif df.month_of_tweet.iloc[i] == 12:
            monthly_distribution[11] += 1

    return monthly_distribution


# Step 5: Checking cure news and death news in tweets

def treatement_and_death_with_charts(df, graph_title):
    treatement = 0
    die = 0

    for i in range(len(df)):
        if ("treat" in df.tweet_text.iloc[i] or "treatement" in df.tweet_text.iloc[i] or "cure" in df.tweet_text.iloc[i]) and df.sentiment.iloc[i] == "positive":
            treatement += 1
        elif ("die" in df.tweet_text.iloc[i] or "dead" in df.tweet_text.iloc[i] or "killed" in df.tweet_text.iloc[i] or "death" in df.tweet_text.iloc[i]) and df.sentiment.iloc[i] == "negative":
            die += 1

    # Drawing pie chart
    sizes = [treatement, die]
    colors = ['#006600', '#cc0000']
    labels = ["Cure news", "death news"]
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title(graph_title)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


# Step 6: Tweets distribution over countries

def tweets_distribution_in_countries(files_dir, region):
    csv_files = []
    all_files = os.listdir(files_dir)
    for file in all_files:
        if '.csv' in file and len(file.split('_')) == 1:
            csv_files.append(files_dir + file)

    countries_names = []
    country_tweets_count = []
    for i in csv_files:
        countries_names.append(i.split('/')[-1][:-4])
        country_tweets_count.append(len(pd.read_csv(i)))

    # plotting tweets distribution

    plt.figure(figsize=(15, 4))  # to increase width of figure
    plt.bar(range(len(countries_names)), country_tweets_count, align='center')
    plt.xticks(range(len(countries_names)), countries_names, rotation=90)
    plt.title('Tweets distribution over ' + region + ' countries')
    plt.show()


# Step 7: main causes of cancers.

def cancer_causes(df, region):
    causes = ['smoking', 'weight', 'virus', 'uv', 'alcohol', 'radiation',
              'hormones', 'pollution', 'food', 'rays', 'genes']
    causes_counts = [0] * 11

    for i in range(len(df)):
        for j in range(len(causes)):
            if causes[j] in df.tweet_text.iloc[i] and (df.sentiment.iloc[i] == "negative" or df.sentiment.iloc[i] == "neutral"):
                causes_counts[j] += 1

    plot_data_with_labels(causes, causes_counts, "Main causes of cancer in" + region + ' countries')


# Step 8: popular Treatements
def cancer_treatements(df, region):
    treatements_types = ['radiotherapy', 'chemotherapy', 'surgery',
                         'targeted therapy', 'hormone therapy', 'stem cell transplant', 'gene therapy', 'cell transfer therapy', 'bone marrow transplant']
    treatemnts_counts = [0] * 9

    for i in range(len(df)):
        for j in range(len(treatements_types)):
            if treatements_types[j] in df.tweet_text.iloc[i] and (df.sentiment.iloc[i] == "positive" or df.sentiment.iloc[i] == "neutral"):
                treatemnts_counts[j] += 1

    # Drawing pie chart
    sizes = treatemnts_counts
    labels = treatements_types
    patches, texts = plt.pie(sizes, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title("Percentages of common cancer treatements in" + region + ' countries')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


# step 9: popular drugs

def cancer_drugs(df):
    drugs = ['avastin', 'revlimid', 'rituxan', 'herceptin', 'imbruvica',
             'gleevec', 'alimta', 'velcade', 'erbitux', 'gardasil', 'Cisplatin', 'Ifosfamide',
             'cyclophosphamide', 'vincristine', 'methotrexate']
    drugs_counts = [0] * 15

    for i in range(len(df)):
        for j in range(len(drugs)):
            if drugs[j] in df.tweet_text.iloc[i]:
                drugs_counts[j] += 1

    plot_data_with_labels(drugs, drugs_counts, "popular drugs")

# Asia


#  █████  ███████ ██  █████
# ██   ██ ██      ██ ██   ██
# ███████ ███████ ██ ███████
# ██   ██      ██ ██ ██   ██
# ██   ██ ███████ ██ ██   ██


# loading data

asian_tweets_file = r'F:/myThesis/asia/asia_tweets.csv'
asian_df = pd.read_csv(asian_tweets_file)


# Step 1: Sentriment analysis
asian_df_with_sent = add_sentiment_to_df(asian_df)


# Step 2: Cancer type counts

asian_cancer_types_counts = cancer_types_counts(asian_df)
plot_data_with_labels(cancer_types, asian_cancer_types_counts, "Cancer types counts in Asia")


# Step 3: Tweet Distribution over months
asian_tweets_distribution_over_months = tweets_distribution_over_months(asian_df)
plot_data_with_labels(months, asian_tweets_distribution_over_months, "Tweets over months in Asia")


# step 4: Cure news vs Death news

treatement_and_death_with_charts(asian_df, "Cure news vs death news in Asian countries")


# Step 5: Tweet Distribution over countries:
asian_files_dir = r'F:/myThesis/asia/'
tweets_distribution_in_countries(asian_files_dir, "Asian")


# Step 6: Main causes of cancer
cancer_causes(asian_df, ' Asian')


# step 7: Popular treatments
cancer_treatements(asian_df, ' Asian')


# step 8: Popular drugs
cancer_drugs(asian_df)


# Europe

# ███████ ██    ██ ██████   ██████  ██████  ███████
# ██      ██    ██ ██   ██ ██    ██ ██   ██ ██
# █████   ██    ██ ██████  ██    ██ ██████  █████
# ██      ██    ██ ██   ██ ██    ██ ██      ██
# ███████  ██████  ██   ██  ██████  ██      ███████


# loading data

europe_tweets_file = r"F:/myThesis/europe/europe_tweets.csv"
europe_df = pd.read_csv(europe_tweets_file)


# Step 1: sentiment analysis
europe_df_with_sent = add_sentiment_to_df(europe_df)


# Step 2: cancer type counts
europe_cancer_types_counts = cancer_types_counts(europe_df)
plot_data_with_labels(cancer_types, europe_cancer_types_counts, "Cancer types counts in Europe")


# Step 3: tweet Distribution over month

europe_tweets_distribution_over_months = tweets_distribution_over_months(europe_df)
plot_data_with_labels(months, europe_tweets_distribution_over_months,
                      "Tweets over months in Europe")


# step 4: Cure news vs Death news
treatement_and_death_with_charts(europe_df, "Cure news vs death news in Europe countries")


# Step 5: Tweet Distribution over countries

europe_files_dir = r'F:/myThesis/europe/'
tweets_distribution_in_countries(europe_files_dir, "European")


# Step 6: Main causes of cancer

cancer_causes(europe_df, ' European')


# step 7: Popular treatments

cancer_treatements(europe_df, ' European')


# step 8: Popular drugs

cancer_drugs(europe_df)


# 3- Nourth America (NA)

# ███    ██  █████
# ████   ██ ██   ██
# ██ ██  ██ ███████
# ██  ██ ██ ██   ██
# ██   ████ ██   ██


# loading data
na_tweets_file = r'F:/myThesis/na/na_tweets.csv'
na_df = pd.read_csv(na_tweets_file)


# Step 1: Sentiment analysis
na_df_with_sent = add_sentiment_to_df(na_df)


# Step 2: Cancer type counts
na_cancer_types_counts = cancer_types_counts(na_df)
plot_data_with_labels(cancer_types, na_cancer_types_counts, "Cancer types counts in North America")


# Step 3: Tweet Distribution over months
na_tweets_distribution_over_months = tweets_distribution_over_months(na_df)
plot_data_with_labels(months, na_tweets_distribution_over_months,
                      "Tweets over months in North America")


# step 4: Cure news vs Death news
treatement_and_death_with_charts(na_df, "Cure news vs death news in North American countries")


# Step 5: Tweet Distribution over countries
na_files_dir = r'F:/myThesis/na/'
tweets_distribution_in_countries(na_files_dir, "North American")


# Step 6: Main causes of cancer
cancer_causes(na_df, ' North American')


# step 7: Popular treatments
cancer_treatements(na_df, ' North American')


# step 8: Popular drugs
cancer_drugs(na_df)

# 4- South America (SA)


# ███████  █████
# ██      ██   ██
# ███████ ███████
#      ██ ██   ██
# ███████ ██   ██


# loading data
sa_tweets_file = r'F:/myThesis/sa/sa_tweets.csv'
sa_df = pd.read_csv(sa_tweets_file)


# Step 1: Sentiment analysis
sa_df_with_sent = add_sentiment_to_df(sa_df)


# Step 2: Cancer type counts
sa_cancer_types_counts = cancer_types_counts(sa_df)
plot_data_with_labels(cancer_types, sa_cancer_types_counts, "Cancer types counts in Sorth America")


# Step 3: Tweet Distribution over months
sa_tweets_distribution_over_months = tweets_distribution_over_months(sa_df)
plot_data_with_labels(months, sa_tweets_distribution_over_months,
                      "Tweets over months in Sorth America")


# step 4: Cure news vs Death news
treatement_and_death_with_charts(sa_df, "Cure news vs death news in Sorth American countries")


# Step 5: Tweet Distribution over countries
sa_files_dir = r'F:/myThesis/sa/'
tweets_distribution_in_countries(sa_files_dir, "Sorth American")


# Step 6: Main causes of cancer
cancer_causes(sa_df, ' Sorth American')


# step 7: Popular treatments
cancer_treatements(sa_df, ' Sorth American')


# step 8: Popular drugs
cancer_drugs(sa_df)

# 5- Africa


#  █████  ███████ ██████  ██  ██████  █████
# ██   ██ ██      ██   ██ ██ ██      ██   ██
# ███████ █████   ██████  ██ ██      ███████
# ██   ██ ██      ██   ██ ██ ██      ██   ██
# ██   ██ ██      ██   ██ ██  ██████ ██   ██


# loading data
africa_tweets_file = r'F:/myThesis/africa/africa_tweets.csv'
africa_df = pd.read_csv(africa_tweets_file)


# Step 1: Sentiment analysis
africa_df_with_sent = add_sentiment_to_df(africa_df)


# Step 2: Cancer type counts
africa_cancer_types_counts = cancer_types_counts(africa_df)
plot_data_with_labels(cancer_types, africa_cancer_types_counts, "Cancer types counts in Africa")


# Step 3: Tweet Distribution over months
africa_tweets_distribution_over_months = tweets_distribution_over_months(africa_df)
plot_data_with_labels(months, africa_tweets_distribution_over_months,
                      "Tweets over months in Africa")


# step 4: Cure news vs Death news
treatement_and_death_with_charts(africa_df, "Cure news vs death news in African countries")


# Step 5: Tweet Distribution over countries
africa_files_dir = r'F:/myThesis/africa/'
tweets_distribution_in_countries(africa_files_dir, "African")


# Step 6: Main causes of cancer
cancer_causes(africa_df, ' African')


# step 7: Popular treatments
cancer_treatements(africa_df, ' African')


# step 8: Popular drugs
cancer_drugs(africa_df)


# 6- Australia


#  █████  ██    ██ ███████ ████████ ██████   █████  ██      ██  █████
# ██   ██ ██    ██ ██         ██    ██   ██ ██   ██ ██      ██ ██   ██
# ███████ ██    ██ ███████    ██    ██████  ███████ ██      ██ ███████
# ██   ██ ██    ██      ██    ██    ██   ██ ██   ██ ██      ██ ██   ██
# ██   ██  ██████  ███████    ██    ██   ██ ██   ██ ███████ ██ ██   ██


# loading data
aus_tweets_file = r'F:/myThesis/aus/aus_tweets.csv'
aus_df = pd.read_csv(aus_tweets_file)


# Step 1: Sentiment analysis
aus_df_with_sent = add_sentiment_to_df(aus_df)


# Step 2: Cancer type counts
aus_cancer_types_counts = cancer_types_counts(aus_df)
plot_data_with_labels(cancer_types, aus_cancer_types_counts, "Cancer types counts in Australia")


# Step 3: Tweet Distribution over months
aus_tweets_distribution_over_months = tweets_distribution_over_months(aus_df)
plot_data_with_labels(months, aus_tweets_distribution_over_months,
                      "Tweets over months in Australia")


# step 4: Cure news vs Death news
treatement_and_death_with_charts(aus_df, "Cure news vs death news in Australian countries")


# Step 5: Tweet Distribution over countries
aus_files_dir = r'F:/myThesis/aus/'
tweets_distribution_in_countries(aus_files_dir, "Australian")


# Step 6: Main causes of cancer
cancer_causes(aus_df, ' Australian')


# step 7: Popular treatments
cancer_treatements(aus_df, ' Australian')


# step 8: Popular drugs
cancer_drugs(aus_df)


# 7 Subcontinent


# ███████ ██    ██ ██████   ██████  ██████  ███    ██
# ██      ██    ██ ██   ██ ██      ██    ██ ████   ██
# ███████ ██    ██ ██████  ██      ██    ██ ██ ██  ██
#      ██ ██    ██ ██   ██ ██      ██    ██ ██  ██ ██
# ███████  ██████  ██████   ██████  ██████  ██   ████


# loading data
subcontinent_tweets_file = r'F:/myThesis/subcontinent/subcontinent_tweets.csv'
subcontinent_df = pd.read_csv(subcontinent_tweets_file)


# Step 1: Sentiment Analysis
subcontinent_df_with_sent = add_sentiment_to_df(subcontinent_df)


# Step 2: Cancer type counts
subcontinent_cancer_types_counts = cancer_types_counts(subcontinent_df)
plot_data_with_labels(cancer_types, subcontinent_cancer_types_counts,
                      "Cancer types counts in subcontinental countries")


# Step 3: Tweets Distribution over months
subcontinent_tweets_distribution_over_months = tweets_distribution_over_months(subcontinent_df)
plot_data_with_labels(months, subcontinent_tweets_distribution_over_months,
                      "Tweets over months in subcontinental countries")


# step 4: Cure news vs Death news
treatement_and_death_with_charts(
    subcontinent_df, "Cure news vs death news in subcontinental countries tweets")


# Step 5: Tweet distribution over countries
subcontinent_files_dir = r'F:/myThesis/subcontinent/'
tweets_distribution_in_countries(subcontinent_files_dir, "subcontinent countries")


# Step 6: Main causes of cancer
cancer_causes(subcontinent_df, ' Subcontinental')


# step 7: Popular treatments
cancer_treatements(subcontinent_df, ' Subcontinental')


# step 8: Popular drugs
cancer_drugs(subcontinent_df)
