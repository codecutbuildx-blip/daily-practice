def compute_prefix_function(pattern):
    # Create a list to store the prefix function values
    prefix = [0] * len(pattern)
    
    j = 0  # Index for pattern array
    
    # Process every substring of pattern starting from the second character
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix[i] = j
    
    return prefix

def kmp_search(text, pattern):
    # Create a list to store the prefix function values for pattern
    prefix = compute_prefix_function(pattern)
    
    # Initialize indices for text and pattern arrays
    m = len(pattern)  # Length of pattern
    n = len(text)   # Length of text
    
    j = 0  # Index for pattern array
    i = 0  # Index for text array
    
    while i < n:
        if j == 0 or pattern[j] == text[i]:
            i += 1
            if j == m - 1:
                return i - m + 1
            else:
                j += 1
        elif j > 0 and pattern[j] != text[i]:
            j = prefix[j - 1]
    
    return -1  # Pattern not found in text

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABAB"

index = kmp_search(text, pattern)
if index != -1:
   print("Pattern found at index", str(index))
else:
   print("Pattern not found")