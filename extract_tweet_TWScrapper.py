import os

list_europe2 = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
               'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Finland', 'France',
               'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia',
               'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland',
               'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'UK','england', 'Scotland', 'Vatican']


list_asia = ['Japan', 'India', 'China', 'Indonesia', 'Vietnam', 'Thailand', 'Singapore', 'Philippines', 'Hong Kong', 'Malaysia', 'South Korea',
             'Pakistan', 'Iran', 'North Korea', 'Sri Lanka', 'Israel', 'Myanmar', 'Syria', 'Cambodia', 'Taiwan', 'Maldives', 'Bangladesh', 'Saudi Arabia', 'Iraq',
             'Nepal', 'Qatar', 'Afghanistan', 'Yemen', 'United Arab Emirates', 'Laos', 'Mongolia', 'Lebanon', 'Macau', 'Oman', 'Uzbekistan',
                      'Jordan', 'Azerbaijan', 'Kuwait', 'State of Palestine', 'Armenia', 'Bhutan', 'Bahrain', 'Tajikistan', 'Brunei', 'Kyrgyzstan', 'Turkmenistan']

list_north_america = ['Bahamas', 'Barbados', 'Belize', 'Bermuda', 'Canada', 'Costa Rica',
                      'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras',
                      'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'St. Kitts and Nevis', 'St. Lucia', 'St. Vincent and The Grenadines',
                      'Trinidad and Tobago', 'usa']

list_south_america=['Argentina','Bolivia','Brazil','Chile','Colombia',
                    'Ecuador','Falkland islands','French guiana','Guyana',
                    'Paraguay','Peru','Suriname','Uruguay','Venezuela']


list_africa=['Algeria','Angola','Benin','Botswana','Burkina Faso',
         'Burundi','Cabo Verde','Cameroon','Central African Republic',   
         'Chad','Comoros','Democratic Republic of the Congo',
         'Republic of the Congo',"Cote d'Ivoire",'Djibouti','Egypt',
         'Equatorial Guinea','Eritrea','Eswatini','Ethiopia',
         'Gabon','Gambia','Ghana', 'Guinea','Guinea-Bissau','Kenya',
         'Lesotho','Liberia','Libya','Madagascar','Malawi','Mali', 
         'Mauritania','Mauritius','Morocco','Mozambique','Namibia',
         'Niger','Nigeria','Sao Tome and Principe','Senegal','Seychelles',
         'Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Rwanda',
         'Tanzania','Togo','Tunisia','Uganda','Uganda','Zimbabwe']

list_australia=['Australia', 'Fiji', 'Kiribati', 'Marshall Islands',
                'Micronesia', 'Nauru', 'New Zealand', 'Palau',
                'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga',
                'Tuvalu', 'Vanuatu']


list_subcontinent = ['Bangladesh', 'India', 'Pakistan']


# Keywords
types= ["cancer","Melanoma","lymphoma", "Leukemia", "carcinoma", "sarcoma","teratoma"]


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
assure_path_exists("europe/")
assure_path_exists("asia/")
assure_path_exists("na/")
assure_path_exists("sa/")
assure_path_exists("africa/")
assure_path_exists("aus/")
assure_path_exists("subcontinent/")

for country in list_europe2:
    print(country)
    for t in types:
        command = "twitterscraper \"" + t + " near:" + country + "\" -o \"./europe/"+country+"_"+t+"_tweets.json\" -l 5000 --lang en -bd 2016-01-01 -ed 2017-12-31"
        os.system(command)

for country in list_asia:
    print(country)
    for t in types:
        command = "twitterscraper \"" + t + " near:" + country + "\" -o \"./asia/"+country+"_"+t+"_tweets.json\" -l 5000 --lang en -bd 2016-01-01 -ed 2017-12-31"
        os.system(command)

for country in list_north_america:
    print(country)
    for t in types:
        command = "twitterscraper \"" + t + " near:" + country + "\" -o \"./NA/"+country+"_"+t+"_tweets.json\" -l 5000 --lang en -bd 2016-01-01 -ed 2017-12-31"
        os.system(command)

for country in list_south_america:
    print(country)
    for t in types:
        command = "twitterscraper \"" + t + " near:" + country + "\" -o \"./sa/"+country+"_"+t+"_tweets.json\" -l 5000 --lang en -bd 2016-01-01 -ed 2017-12-31"
        os.system(command)

for country in list_africa:
    print(country)
    for t in types:
        command = "twitterscraper \"" + t + " near:" + country + "\" -o \"./africa/"+country+"_"+t+"_tweets.json\" -l 5000 --lang en -bd 2016-01-01 -ed 2017-12-31"
        os.system(command)

for country in list_australia:
    print(country)
    for t in types:
        command = "twitterscraper \"" + t + " near:" + country + "\" -o \"./aus/"+country+"_"+t+"_tweets.json\" -l 5000 --lang en -bd 2016-01-01 -ed 2017-12-31"
        os.system(command)


for country in list_subcontinent:
    print(country)
    for t in types:
        command = "twitterscraper \"" + t + " near:" + country + "\" -o \"./subcontinent/"+country+"_"+t+"_tweets.json\" -l 5000 --lang en -bd 2016-01-01 -ed 2017-12-31"
        os.system(command)




