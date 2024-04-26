import nltk
import string
from nltk.corpus import stopwords  
from collections import Counter

# nltk.download('punkt')

def read_file(file_name):
    try:
        with open(paragraphs.txt, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print("The file couldn't be found.")
        return None

def clean_words(text):
    stop_words = set(stopwords.words('english'))

    # Remove punctuation
    for character in string.punctuation: 
        text = text.replace(character, '')

    words = text.lower().split()  # Split into words and make lowercase
    clean_words = [word for word in words if word not in stop_words]
    return clean_words

def count_words(words):
    word_counts = Counter(words)
    return word_counts

def show_word_counts(word_counts):
    for word, count in word_counts.items():
        print(word, ":", count)

def save_counts(word_counts, output_file_name):
    try:
        with open(output_file_name, 'w') as file:
            for word, count in word_counts.items():
                file.write(word + ": " + str(count) + "\n")
        print("Word counts saved!")
    except Exception as e:
        print("Error saving:", e)

file_name = "paragraphs.txt"
output_file_name = "word_frequencies.txt"

text = read_file(file_name)
if text:
    clean_words = clean_words(text)
    word_counts = count_words(clean_words)
    show_word_counts(word_counts)
    save_counts(word_counts, output_file_name) 
