# ENGLISH TO ALIEN LANGUAGE TRANSLATOR TUTORIAL

# LEARNING OBJECTIVE:
# This tutorial will teach you how to build a program that translates
# English phrases into a unique alien language. We'll achieve this by
# mastering two fundamental Python concepts:
# 1. String Manipulation: How to work with and transform text.
# 2. Dictionaries: How to store and retrieve data using key-value pairs,
#    which is perfect for our translation rules.

# Let's get started!

# --- Section 1: Setting up our Alien Dictionary ---

# Dictionaries are like real-world dictionaries! They store pairs of
# information. In our case, the "key" will be an English word, and the
# "value" will be its translation in the alien language.

# We'll define a dictionary called 'alien_dictionary'.
# Each entry is a word-to-translation pair.
# Example: 'hello' (English word) : 'glarp' (Alien word)
alien_dictionary = {
    "hello": "glarp",
    "world": "zorg",
    "goodbye": "bloop",
    "thank you": "fizzbang",
    "please": "whizz",
    "yes": "zib",
    "no": "nob",
    "friend": "krom",
    "enemy": "vrax",
    "eat": "munch",
    "drink": "slurp",
    "happy": "flim",
    "sad": "glum",
    "big": "mega",
    "small": "mini",
    "i": "me",
    "you": "youz",
    "is": "be",
    "a": "an",
    "the": "da",
    "great": "epic",
    "day": "suntime",
}

# --- Section 2: The Translation Function ---

# Now, let's create a function that will take an English phrase and
# translate it. Functions help us organize our code and reuse it.

def translate_to_alien(english_phrase):
    # This function takes an English phrase as input.
    # Our goal is to turn this phrase into alien words.

    # First, we need to make sure our input is consistent.
    # We'll convert the entire phrase to lowercase so that "Hello" and "hello"
    # are treated the same. This is important for matching words in our dictionary.
    english_phrase = english_phrase.lower()

    # Next, we need to break the English phrase into individual words.
    # The .split() method is super handy for this. It splits a string
    # into a list of substrings (words) based on whitespace.
    # Example: "hello world".split() becomes ['hello', 'world']
    words = english_phrase.split()

    # We'll create an empty list to store our translated alien words.
    alien_words = []

    # Now, we'll loop through each word in the English phrase.
    # The 'for' loop lets us iterate over items in a list (or other sequences).
    for word in words:
        # For each English word, we check if it exists as a key in our
        # 'alien_dictionary'. The .get() method is a safe way to do this.
        # If the word is found, it returns the corresponding alien translation.
        # If the word is NOT found, it returns a default value (which we set to
        # the original English word itself, so unknown words aren't lost).
        # This makes our translator robust!
        alien_translation = alien_dictionary.get(word, word)

        # We then add the translated word (or the original English word if
        # no translation was found) to our 'alien_words' list.
        alien_words.append(alien_translation)

    # Finally, we need to join the translated alien words back into a single
    # alien phrase. The .join() method does the opposite of .split().
    # We use a space " " as the separator between the alien words.
    # Example: " ".join(['glarp', 'zorg']) becomes "glarp zorg"
    translated_phrase = " ".join(alien_words)

    # We return the final translated phrase.
    return translated_phrase

# --- Section 3: Example Usage ---

# Let's test our translator!

# Example 1: A simple phrase
english_sentence_1 = "Hello world"
alien_sentence_1 = translate_to_alien(english_sentence_1)
print(f"English: {english_sentence_1}")
print(f"Alien: {alien_sentence_1}\n") # \n adds a blank line for readability

# Example 2: A longer phrase with some unknown words
english_sentence_2 = "Thank you my friend, it is a great day"
alien_sentence_2 = translate_to_alien(english_sentence_2)
print(f"English: {english_sentence_2}")
print(f"Alien: {alien_sentence_2}\n")

# Example 3: Using words not in our dictionary
english_sentence_3 = "This is a test sentence"
alien_sentence_3 = translate_to_alien(english_sentence_3)
print(f"English: {english_sentence_3}")
print(f"Alien: {alien_sentence_3}\n")

# Example 4: Case insensitivity test
english_sentence_4 = "GOODBYE Friend"
alien_sentence_4 = translate_to_alien(english_sentence_4)
print(f"English: {english_sentence_4}")
print(f"Alien: {alien_sentence_4}\n")

# Congratulations! You've built a basic translator using dictionaries and string manipulation.
# You can easily extend this by adding more words to the 'alien_dictionary'!