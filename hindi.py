from collections import defaultdict

# Define a mapping of Hinglish words to emotions
hinglish_emotions = {
    'khush': 'Happy',
    'udas': 'Sad',
    'gussa': 'Angry',
    'chintit': 'Worried',
    # Add more Hinglish words and their emotions
}

# Read the text file
input_text_file = 'read.txt'  # Replace with your text file
with open(input_text_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize the text into words
words = text.lower().split()

# Find Hinglish words and map them to emotions
hinglish_word_emotions = defaultdict(list)
for word in words:
    if word in hinglish_emotions:
        emotion = hinglish_emotions[word]
        hinglish_word_emotions[word].append(emotion)

# Print the emotions associated with Hinglish words
for word, emotions in hinglish_word_emotions.items():
    print(f'Hinglish Word: {word.capitalize()}, Emotions: {", ".join(emotions)}')
