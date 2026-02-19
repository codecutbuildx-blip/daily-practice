def compute_prefix_function(pattern):
    # Initialize the prefix function with all values as 0
    prefix = [0] * len(pattern)
    j = 0
    # Traverse the pattern string and fill the prefix array
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix[i] = j
    return prefix

def kmp_search(text, pattern):
    # Compute the prefix function for the pattern string
    prefix = compute_prefix_function(pattern)
    m = len(pattern)
    n = len(text)
    j = 0
    # Traverse the text and search for the pattern
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = prefix[j - 1]
        if pattern[j] == text[i]:
            j += 1
        # If the entire pattern is found, return the starting index
        if j == m:
            print("Pattern found at index", i - m + 1)
            j = prefix[j - 1]

# Test the KMP algorithm with a sample text and pattern
text = "abxabcabcx"
pattern = "abcabc"
kmp_search(text, pattern)