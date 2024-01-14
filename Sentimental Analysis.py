import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon') #vader_lexicon is used for sentimental analysis
sia = SentimentIntensityAnalyzer()
text = input("Enter text: ")
score = sia.polarity_scores(text)
print(score)
overall_sentiment = "Positive" if score['compound'] > 0 else "Negative" if score['compound'] < 0 else "Neutral"
print(f"Overall Sentiment: {overall_sentiment}")
