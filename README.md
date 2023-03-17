# Plagiarism-Detector-AI
An AI tool which detects Plagiarism between two text files and displays the similarity between them(made exclusively for Hackoverflow 1.0)

Plagiarism is rampant on the internet and in the classroom. With so much content out there, it’s sometimes hard to know when something has been plagiarized. Authors writing blog posts may want to check if someone has stolen their work and posted it elsewhere. Teachers may want to check students’ papers against other scholarly articles for copied work. News outlets may want to check if a content farm has stolen their news articles and claimed the content as its own.

So, how do we guard against plagiarism? Wouldn’t it be nice if we could have software do the heavy lifting for us? Using machine learning, we can build our own plagiarism checker that searches a vast database for stolen content.Here we have done an AI model that detects similarity between two texts and checks for plagiarism.

This repo has source code of a Python script which detects plagiarism in a textual document using cosine similarity.
This code performs a document similarity comparison using cosine similarity.

Here's what each part of the code does:

 Importing required libraries and modules
 Downloads tokenizer data from the NLTK package.
 Importing the word tokenizing function.
 Importing the Counter class that will log the frequency of unique words.

def cosine_similarity(a,b):: Defining a function to compute the cosine similarity between two vectors. The function takes two parameters: a and b, representing the two vectors to be compared.

 Calculates the numerator of the cosine similarity formula for two vectors. It iterates through the two vectors one element at a time, multiplies each pair of corresponding elements together, and adds up their products.

Calculates the denominator of the cosine similarity formula for two vectors. It first squares each element in both vectors, sums those values, computes the square root of each sum, multiplies the square roots together (as the denominator), and then returns the resulting value.

Asks the user to enter the text of two documents so that they can be compared.
 Takes user inputted documents and tokenizes them into lowercase words while only keeping the letters of the alphabet.
 Counts the number of occurrences of each unique word in each tokenized document by using the Counter method.

Creates a set containing all unique words across both documents.

Creates separate frequency vectors for each document with zero values where a word is not present in that respective document. Computes the cosine similarity score between the frequency vectors for each document.
 Displays the similarity score rounded to two decimal places.
 
 This model has been built by [@JustBaguette](https://github.com/JustBaguette) , @Athena-2003 and @Sinchana-SH as team for Hackoverflow 0.1