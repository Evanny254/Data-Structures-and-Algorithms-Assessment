# Dictionaries: 

# Question 3: Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

 
import string

def word_frequency(sentence):
    cleaned_sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_sentence.split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# Example 
sentence = "This is a test sentence. This sentence is a test."

result = word_frequency(sentence)
print(result)
