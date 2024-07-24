import re
from nltk.corpus import stopwords
import pandas as pd
import nltk
import os

data = pd.read_csv('IMDB_UnsortedDataset.csv')

# Manual link to stopwords file
current_p = os.path.dirname(os.path.abspath(__file__))
stop_words_p = os.path.join(current_p, 'stopwords', 'english')

def load_stopwords(path):
	with open(path, 'r') as file:
		stopwords = file.read().splitlines()
	return set(stopwords)

stop_words = load_stopwords(stop_words_p)

def clean_text(data):
	# Removing punctuation and special characters, all text lowercase, stopwords removed from data
	data = re.sub(r'[^\w\s]', '', data)
	data = data.lower()
	words = data.split()
	words = [word for word in words if word not in stop_words]
	return ''.join(words)


# Creates clean text new column next to review
df = pd.DataFrame(data)
df['cleaned_text'] = df['review'].apply(clean_text)

print(df[['review', 'cleaned_text']])

