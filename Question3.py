# Dictionaries: 

# Question 3: Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

# Ignore punctuation and consider words in a case-insensitive manner. 
import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    cleaned_sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    
    # Split the sentence into words
    words = cleaned_sentence.split()

    # Count the frequency of each word
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# Example input
sentence = "This is a test sentence. This sentence is a test."

# Test case
result = word_frequency(sentence)
print(result)
