# Objectives

# improving the student's skills in operating with strings;
# converting characters into ASCII code, and vice versa.

# Scenario
# You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

# The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

# Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

# Your task is to write a program which:

# asks the user for one line of text to encrypt;
# asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# prints out the encoded text.

# asks the user for one line of text to encrypt;
text = input("Enter your message: ")
# asks the user for a shift value
shift = int(input("Enter shift value between 1-25: "))
# check if user entered a valid number and prompt again if not
if shift not in range(0,26):
    shift = int(input("Please enter a whole number between 1-25: "))
#define funtion to create cipher
def encrypt(text, shift):
    #create empty string to hold cipher
    cipher = ''
    # iterate through text to check for alphabetical characters
    for char in text: 
        if char.isalpha():
            # determine if character is upper or lower-case
            if char.islower():
                start_character = ord('a')
            else:
                start_character = ord('A')
        # shift character forward by given value
            start = ord(char) - start_character
            offset = ((start + shift) % 26) + start_character
            cipher += chr(offset)
        # add non-alphabetical characters to the string unchanged
        else:
            cipher += char
    return cipher

print(encrypt(text, shift))



# for char in text: 
#     if char.isalpha():
#         if char.islower():
#             start_character = ord('a')
#         else:
#             start_character = ord('A')

# What happens in the start variable is locating the letter's index number as if it was within range(26) with 'a' being 0. 
# That is our starting point to begin counting through the alphabet. Then in offset we take that starting number and the given shift and get the modulo. The modulo gives us the new index number. Then it must be converted back into it's ASCII code by readding the code for the starting character.
#         start = ord(letter) - start_character
#         offset = ((start + jump) % 26) + start_character
#         result = chr(offset)
        
#     else:
#         cipher += char