# knuth_morris_pratt.py

```python
def compute_prefix_function(pattern):
    """
    Compute the prefix function used in KMP algorithm.

    Args:
        pattern (str): The pattern to be searched for.

    Returns:
        list: A list where the i-th element is the length of the longest proper prefix which is also a suffix.
    """
    m = len(pattern)
    pi = [0] * m
    j = 0

    # Compute the prefix function values
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    return pi


def kmp_search(text, pattern):
    """
    Perform KMP search on the given text for the given pattern.

    Args:
        text (str): The text to be searched.
        pattern (str): The pattern to be searched for.

    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    m = len(pattern)
    n = len(text)

    # Initialize prefix function values
    pi = compute_prefix_function(pattern)

    # Initialize variables
    j = 0
    result = []

    # Traverse through all occurrences of substring in text
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = pi[j - 1]
        if pattern[j] == text[i]:
            j += 1

        # If the entire pattern has been found, then print a message
        if j == m:
            result.append(i - m + 1)
            j = pi[j - 1]

    return result


# Example usage
text = "abcabcabc"
pattern = "abc"

result = kmp_search(text, pattern)

if not result:
    print("Pattern not found in the text.")
else:
    print("Pattern found at indices:", result)