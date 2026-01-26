# LEARNING OBJECTIVE: Understand and implement a simple Markov chain text generator in Python.
#
# This tutorial will guide you through creating a program that learns statistical patterns
# from an input text and then uses those patterns to generate new, original sentences.
# You'll learn:
# 1. How to process text to prepare it for analysis.
# 2. How to build a "Markov model" which maps words to possible next words.
# 3. How to use this model to generate coherent (but often nonsensical) text.
#
# A Markov chain is a mathematical model that describes a sequence of possible events
# in which the probability of each event depends only on the state attained in the previous event.
# In simple terms for text, it means: "What word is most likely to come next after THIS word?"

import random
from collections import defaultdict
import re

# Function 1: build_markov_model
# This function is responsible for analyzing the input text and creating the Markov chain model.
def build_markov_model(text: str) -> dict[str, list[str]]:
    """
    Builds a Markov chain model from an input text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict[str, list[str]]: A dictionary where keys are words and values are lists
                              of words that follow the key word in the input text.
    """

    # We use a defaultdict(list) because it automatically creates an empty list
    # for a key if that key doesn't exist yet when we try to append to it.
    # This simplifies adding new words to our model.
    markov_model: dict[str, list[str]] = defaultdict(list)

    # Preprocessing the text:
    # 1. Convert to lowercase to treat "The" and "the" as the same word.
    # 2. Use a regular expression to find all words and common punctuation marks separately.
    #    This helps us capture punctuation as distinct tokens and simplifies splitting.
    #    For example, "hello world." becomes ["hello", "world", "."] instead of ["hello", "world."].
    #    The regex r'\b\w+\b|[.,!?;]' matches either whole words (\b\w+\b) OR common punctuation.
    #    This approach is simple and effective for a beginner tutorial.
    words = re.findall(r'\b\w+\b|[.,!?;]', text.lower())

    # Now we iterate through the list of words to build our model.
    # We stop one word before the end because each word needs a "next word" to form a pair.
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]

        # For the current_word, we add the next_word to its list of possible followers.
        # This is the core of building the Markov chain: observing transitions.
        markov_model[current_word].append(next_word)

    # After iterating through all word pairs, our model is complete.
    return markov_model

# Function 2: generate_text
# This function uses the previously built Markov model to create new text.
def generate_text(model: dict[str, list[str]], length: int = 20) -> str:
    """
    Generates new text using a Markov chain model.

    Args:
        model (dict[str, list[str]]): The Markov chain model.
        length (int): The maximum number of words to generate.

    Returns:
        str: The generated text.
    """

    # We need a starting point for our text generation.
    # We pick a random word from the keys of our model.
    # We ensure the model is not empty to avoid errors.
    if not model:
        return "Error: Markov model is empty. Cannot generate text."

    # Get all possible starting words (all keys in the model).
    # We choose a random one to begin our generated sentence.
    current_word = random.choice(list(model.keys()))

    # Initialize our generated text with the chosen starting word.
    generated_words: list[str] = [current_word]

    # Loop to generate the rest of the text.
    # We continue until we reach the desired 'length' or a natural end.
    for _ in range(length - 1): # We subtract 1 because we already added the first word
        # Check if the current_word exists in our model as a key.
        # If it doesn't, it means we've reached a word that was always at the end
        # of a phrase in the original text, or a very rare word.
        if current_word in model:
            # From the list of words that can follow 'current_word',
            # we randomly pick one. This is the "Markov" step!
            possible_next_words = model[current_word]
            if not possible_next_words:
                # If there are no next words for some reason (e.g., last word in training text)
                # we break the loop to stop generation, as we can't continue the chain.
                break
            next_word = random.choice(possible_next_words)
            generated_words.append(next_word)
            current_word = next_word # Update current_word for the next iteration
        else:
            # If the current word has no known followers, we can't continue the chain.
            break

        # Optional: Stop if an end-of-sentence punctuation is generated.
        # This makes generated sentences look more complete and sentence-like.
        if current_word in ['.', '!', '?']:
            break

    # Join all the generated words into a single string.
    # We handle spacing for punctuation marks to make it look natural.
    # For example, "hello ." should become "hello." not "hello .".
    # This simple loop checks for punctuation and adjusts spacing.
    final_text_parts = []
    for i, word in enumerate(generated_words):
        if i > 0 and word in ['.', ',', '!', '?', ';']:
            # If it's punctuation, append without a leading space by modifying the previous part.
            final_text_parts[-1] += word
        else:
            # Otherwise, append with a leading space (or just append if it's the first word).
            final_text_parts.append(word)

    # Capitalize the first word of the sentence and ensure it ends with a period.
    # This makes the output more readable and uniform.
    return ' '.join(final_text_parts).capitalize() + '.'

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Markov Chain Text Generator Tutorial ---")
    print("\nInput Text:")

    # This is our training data. The more text you provide, the richer
    # and more varied the generated output will be.
    # Notice how we include some common sentence structures and themes.
    input_text = """
    The quick brown fox jumps over the lazy dog.
    The dog barks at the fox.
    A quick fox is fast.
    The lazy dog sleeps soundly.
    What a beautiful day!
    It is a day for adventures.
    The adventure begins now.
    """
    print(input_text)

    print("\nBuilding Markov model...")
    # Step 1: Build the model from our input text.
    # This involves analyzing all word transitions in the provided text.
    model = build_markov_model(input_text)
    print("Model built successfully!")

    # Optional: Print a small part of the model to see what it learned.
    # Uncomment the lines below to inspect the first few entries of the model.
    # print("\nSample of the Markov Model (first 5 entries):")
    # for word, next_words in list(model.items())[:5]:
    #    print(f"'{word}' can be followed by: {next_words}")

    print("\nGenerating new sentences:")
    # Step 2: Generate text using the built model.
    # We'll generate a few sentences to see the variety and patterns learned.
    for i in range(3):
        generated_sentence = generate_text(model, length=15)
        print(f"Sentence {i+1}: {generated_sentence}")

    print("\n--- Tutorial Complete ---")
    print("Try modifying the input text or generation length to see different results!")
    print("You can also experiment with larger texts for more diverse outputs.")