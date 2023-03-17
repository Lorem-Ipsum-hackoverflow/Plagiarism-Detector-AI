import nltk
import math
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter

# Function to calculate cosine similarity between 2 vectors
def cosine_similarity(a,b):
    numerator = sum([a[i]b[i] for i in range(len(a))])
    denominator = math.sqrt(sum([a[i]**2 for i in range(len(a))]))math.sqrt(sum([b[i]**2 for i in range(len(b))]))
    return numerator/denominator

# Read the two documents from user input
doc1 = input("Enter document 1: ")
doc2 = input("Enter document 2: ")

# Tokenize the paragraphs
tokens1 = [word.lower() for word in word_tokenize(doc1) if word.isalpha()]
tokens2 = [word.lower() for word in word_tokenize(doc2) if word.isalpha()]

# Calculate the frequency of the words in each token list
freq1 = Counter(tokens1)
freq2 = Counter(tokens2)

# Create a set of unique words across both documents
unique_words = set(list(freq1.keys()) + list(freq2.keys()))

# Calculate the frequency vectors for each document
vector1 = [freq1[word] if word in freq1 else 0 for word in unique_words]
vector2 = [freq2[word] if word in freq2 else 0 for word in unique_words]

# Calculate the cosine similarity between the two vectors
similarity_score = cosine_similarity(vector1, vector2)

# Print out the similarity score
print(f"The similarity score between the two documents is {round(similarity_score,2)}")
