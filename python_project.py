import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

#calculate a sentiment score and put it on the same scale as the rating.
def sentiment_score(sentence):
    sentiment_analyzer = SentimentIntensityAnalyzer()

    sentiment_dict = sentiment_analyzer.polarity_scores(sentence)

    if sentiment_dict['compound'] <= - 0.05:
        val = (sentiment_dict['compound'] * 100) + 5
        if val == 0:
            return 1
        else:
            return val
    else:
        return sentiment_dict['compound'] * 100

def main():

    columns = ['ReviewText', 'Rating']

    csv_input = pd.read_csv('clothing_data.csv', usecols=columns)

    print(csv_input)

    csv_input['SentimentScore'] = 1

    #adding a row
    for entry in csv_input.ReviewText:






main()