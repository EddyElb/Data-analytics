#Assuming NLTK is already running 

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from collections import Counter

# Open the file and read its contents
file_path = "path/to/your/file.txt"
with open(r"C:\Users\Ediya Mwaluka Amour\Downloads\un_declaration_hr_text_data.txt") as file:
    file_contents = file.read()

# Convert the text into words
words = file_contents.split()

# Create a set of stop words
stop_words = set(stopwords.words("english"))

# Sort out the stop words from the words list
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Get the top 25 frequent words
top_words = word_freq.most_common(25)

# Extracting the words and their frequencies
top_words, top_freq = zip(*top_words)

# Generate the bar plot
plt.figure(figsize=(10, 6))
plt.barh(range(len(top_words)), top_freq, align='center')
plt.yticks(range(len(top_words)), top_words)
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top 25 Frequent Terms (Excluding Stop Words)')
plt.tight_layout()
plt.show()
