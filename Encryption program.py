import random
import string 
chars=string.ascii_letters+string.digits+string.punctuation+" "
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)

plain=input("Enter a message to encrypt: ")
code=""
for letter in plain:
  index=chars.index(letter)
  code+=keys[index]
print(f"Encrypted message: {code}")

code=input("Enter a message to decrypt: ")
plain=""
for letter in code:
  index=keys.index(letter)
  plain+=chars[index]
print(f"Decrypted message: {plain}")

    
  