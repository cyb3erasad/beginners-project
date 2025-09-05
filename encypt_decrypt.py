import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters

print(chars)
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print()
# print(f"key: {key}")
# print()

# Encrypt

plain_text = input("Enter A Message: ")
cypher_text = " "

for letter in plain_text:
    index = chars.index(letter)
    cypher_text += key[index]

print(f"\nOriginal message: {plain_text}")
print(f"\nEncrypted message: {cypher_text}")    

# Dyscrypt

cypher_text = input("\nEnter A Message For Dyscrypt: ")
plain_text = " "

for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cypher_text}")
print(f"Dycrypted message: {plain_text}")  