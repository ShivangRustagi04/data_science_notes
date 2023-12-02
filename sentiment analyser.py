# i created another text file which contains most common hindi and english words that are used in conversation and through which i can detect sentiment of message as negative or positive 

import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('wordnet')


from deep_translator import GoogleTranslator
import pandas as pd

def copy_person_messages_to_text(csv_file, specific_person, output_text_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Filter data for the specific person
    filtered_data = df[df['user'] == specific_person]['message']

    # Write filtered data to the specified text file
    with open(output_text_file, 'w', encoding='utf-8') as f:
        for message in filtered_data:
            f.write(message + '\n')

    print(f"Messages from '{specific_person}' copied to '{output_text_file}'.")

# Specify the CSV file and specific person
csv_file = 'sample_whatsapp_messages.csv'
specific_person = input("Whose messages do you want to copy? ")
output_text_file = 'read.txt'  # Change this to your desired output text file

# Call the function
copy_person_messages_to_text(csv_file, specific_person, output_text_file)
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Using word_tokenize because it's faster than split()
tokenized_words = word_tokenize(cleaned_text)  # Removed "english"

# Removing Stop Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - From plural to single + Base form of a word (example better -> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in lemma_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyze(sentiment_text):  # Renamed from sentiment_analyse to sentiment_analyze
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyze(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

