import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
def build_table(words):
    result = {}
    #read and split into words
    words = words.split()
    for i in range(1, len(words)-1):
        if result[words[i-1]] == None:
            result[words[i-1]]=[]
        result[words[i-1]].append(words[i])


# print(words)
# TODO: construct 5 random sentences
# Your code here

# solution code
# import random
# # Read in all the words in one go
# with open("./applications/markov/input.txt") as f:
#     words = f.read()
#     words = words.split()
#     # print(words)
# following = {}
# prev = None
# for word in words:
#     if prev is not None:
#         # Make an empty list for the first entries
#         if prev not in following:
#             following[prev] = []
#         # Add word to the list of those that are following
#         following[prev].append(word)
#     prev = word
# # Words that we can start a sentence with
# # We'll get clever and look for words where either the first letter is a
# # capital, or the second is (presumably following a quote):
# def is_good_start(x): return x[0].isupper() or len(x) > 1 and x[1].isupper()
# # if word[0](i.e. first letter of the word) is uppercase or length of word is
# # greater than 1 AND word[1](i.e. character 2) is upper
# # then add word to is_good_start
# start_words = [w for w in following.keys() if is_good_start(w)]
# # if word in following.keys() and word in is_good_start
# # then start_words = word
# # Print a number of paragraphs (five in this case)
# for _ in range(5):
#     # Choose the starting word at random from start_words
#     word = random.choice(start_words)
#     stopped = False  # Initialize stopped to False
#     stop_punctuation = ".!?"  # Initalize stop punctuation on any of these characters
#     while not stopped:
#         # print single word from our list and follow printed word with a space
#         print(word, end=" ")
#         if word[-1] in stop_punctuation or len(word) > 1 and word[-2] in stop_punctuation:
#             # if last character of word is punctuation or second to last character of word is punctiation
#             # then STOP
#             stopped = True
#         else:
#             # Follow to the next word in the chain
#             next_words = following[word]
#             word = random.choice(next_words)
#     print("\n")
# # TODO: analyze which words can follow other words
# # Your code here
# # TODO: construct 5 random sentences
# # Your code here