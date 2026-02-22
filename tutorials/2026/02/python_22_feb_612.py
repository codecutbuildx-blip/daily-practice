# String Hashing in Python

# Importing the hashlib library which provides a secure way to create hash values
import hashlib

# Function to create a hash value for a given string
def create_hash(s):
    # Using the sha256 function from the hashlib library to create a hash value
    # The sha256 function returns a hash value of 256 bits (64 characters)
    hash_value = hashlib.sha256(s.encode()).hexdigest()
    return hash_value

# Function to check if two hash values are equal
def compare_hashes(hash1, hash2):
    # Checking if the two hash values are equal
    if hash1 == hash2:
        return True
    else:
        return False

# Creating a string to be hashed
s = "Hello, World!"

# Creating a hash value for the string
hash_value = create_hash(s)

# Printing the hash value
print("Hash Value:", hash_value)

# Creating another hash value for the string
hash_value2 = create_hash(s)

# Comparing the two hash values
print("Comparing Hash Values:", compare_hashes(hash_value, hash_value2))

# Using a hash table to store unique strings
hash_table = {}

# Function to add a string to the hash table
def add_string(s):
    # Creating a hash value for the string
    hash_value = create_hash(s)
    # Adding the string to the hash table
    hash_table[hash_value] = s

# Function to remove a string from the hash table
def remove_string(s):
    # Creating a hash value for the string
    hash_value = create_hash(s)
    # Checking if the string is in the hash table
    if hash_value in hash_table:
        # Removing the string from the hash table
        del hash_table[hash_value]

# Adding strings to the hash table
add_string("Hello, World!")
add_string("Python")

# Printing the hash table
print("Hash Table:", hash_table)

# Removing a string from the hash table
remove_string("Python")

# Printing the hash table
print("Hash Table after removal:", hash_table)

# Example usage of string hashing
# Creating a string to be hashed
s = "Hello, World!"

# Creating a hash value for the string
hash_value = create_hash(s)

# Printing the hash value
print("Hash Value:", hash_value)