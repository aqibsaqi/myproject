#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
import string

def generate_random_chars(length=3):
    """Generate a random string of given length using uppercase letters."""
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def encrypt_message(message, key):
    """Encrypt the message using a key."""
    random.seed(key)  # Use the key for reproducibility
    words = message.split(" ")
    nword = []
    for word in words:
        if len(word) >= 3:
            # Generate random prefix and suffix
            prefix = generate_random_chars()
            suffix = generate_random_chars()
            # Encrypt the word
            stnew = prefix + word[1:] + word[0] + suffix
            nword.append(stnew)
        else:
            # Reverse short words
            nword.append(word[::-1])
    # Add a marker to verify the key during decryption
    marker = generate_random_chars(5)
    return f"{marker} {' '.join(nword)}"


def decrypt_message(encoded_message, key):
    """Decrypt the message using the same key."""
    random.seed(key)  # Use the key for reproducibility
    # Extract the marker and encrypted message
    parts = encoded_message.split(" ", 1)
    if len(parts) < 2:
        return "Invalid encoded message format!"
    marker, encrypted_words = parts
    # Validate the marker
    expected_marker = generate_random_chars(5)
    if marker != expected_marker:
        return "Error: Key does not match! Unable to decode the message."

    words = encrypted_words.split(" ")
    nword = []
    for word in words:
        if len(word) >= 9:  # Minimum length for a word with prefix and suffix
            # Remove the random prefix and suffix
            stripped_word = word[3:-3]
            # Decrypt the word
            original_word = stripped_word[-1] + stripped_word[:-1]
            nword.append(original_word)
        else:
            # Reverse short words
            nword.append(word[::-1])
    return " ".join(nword)


# Main program
message = input("Write the message: ")
key = input("Enter the key (a number or string): ")

coding = input("Enter 1 for encrypt and 0 for decode: ")
if coding == "1":
    # Encrypt the message
    encoded_message = encrypt_message(message, key)
    print("Encoded message:", encoded_message)
elif coding == "0":
    # Decrypt the message
    decoded_message = decrypt_message(message, key)
    print("Decoded message:", decoded_message)
else:
    print("Invalid option selected.")


# In[ ]:





# In[ ]:



      


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




