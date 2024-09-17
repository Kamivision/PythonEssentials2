# From section 2.3
# Objectives

# improving the student's skills in operating with strings;
# using built-in Python string methods.
# Scenario

# You already know how split() works. Now we want you to prove it.

# Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

# it should accept exactly one argument - a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()

def mysplit(string):
   # return [] if string is empty or contains whitespaces only
    if not string or string.isspace():
        return [ ]
     
    # prepare a list to return
    word_list = []
    word = ""
    
    # check if we are currently inside a word (i.e., if the string starts with a word)
    inword = not string[0].isspace()

    # iterate through all the characters in string
    for letter in string:
        # if we are currently inside a string...
        if inword:
            # ... and current character is not a space...
            if not letter.isspace():
                # ... update current word
                word = word + letter
            
            # ... otherwise, we reached the end of the word so we need to append it to the list...
            else: 
                word_list.append(word)
                # ... and signal a fact that we are outside the word now
                inword = False

        else:
            # if we are outside the word and we reached a non-white character...    
            if not letter.isspace():
                # ... it means that a new word has begun so we need to remember it and
                inword = True
                # ... store the first letter of the new word
                word = letter
    else:
        # if we left the string and there is a non-empty string in word, we need to update the list
        if not word.isspace() and word not in word_list:
            word_list.append(word)

    # return the list to invoker
    return word_list
   
        

    




print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
