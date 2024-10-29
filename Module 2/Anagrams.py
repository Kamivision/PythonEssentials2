# Objectives
# improving the student's skills in operating with strings;
# converting strings into lists, and vice versa.

# Scenario
# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

# Your task is to write a program which:

# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.

# Note:

# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

text1 = input("Enter a word or phrase: ")
text2 = input("Enter another word or phrase: ")

def anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    text1_char = []
    text2_char = []

    for char in text1:
        if not char.isalpha():
            continue
        text1_char.append(char)

    for letter in text2:
        if not letter.isalpha():
            continue
        text2_char.append(letter)

    