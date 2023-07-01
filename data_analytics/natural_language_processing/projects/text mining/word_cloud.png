# checking if stopwords package is up to date
import nltk
nltk.download("stopwords")

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords

# Open the file and read its contents
file_path = "path/to/your/file.txt"
with open(r"C:\Users\Ediya Mwaluka Amour\Downloads\un_declaration_hr_text_data.txt") as file:
    file_contents = file.read()

# Convert the text into words
words = file_contents.split()

# Create a set of stop words
stop_words = set(stopwords.words("english"))

# Sorting out the stop words from the words list
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count the frequency of each word
word_freq = {}
for word in filtered_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Generating the word cloud
wordcloud = WordCloud(width=600, height=300, background_color="white").generate_from_frequencies(word_freq)

# Display the word cloud
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
