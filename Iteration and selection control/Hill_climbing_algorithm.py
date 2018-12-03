import random
import string

# Generate list of strings including space
alpha = list(string.ascii_lowercase)
alpha.append(' ')


# global to contain words generated from the generate_string function
word_list = []
goal = 'methinks it is like a weasel'


# Function to generate strings 28 characters long.
def generate_string():
    # Check is the list has been filled once, if not, fill it
    if len(word_list) < len(goal):
        for x in range(0, len(goal)):
            y = random.randint(0, len(alpha) - 1)
            word_list.append(alpha[y])

    # Loop through the list and keep correct letters
    else:
        for x in range(0, len(word_list)):
            if word_list[x] != goal[x]:
                y = random.randint(0, len(alpha)- 1)
                word_list[x] = alpha[y]

    # Concatenate all letters in word_list to form a word
    word = ''
    for x in word_list:
        word = word+x

    # Return word that has been created
    return word


# Function to compare generated string to the goal
def compare_string():
    word = generate_string()
    score = 0
    # Increase score if items are the same with regards to position
    for items in range(0, len(word)):
        if word[items] == goal[items]:
            score += 1
    return word, score


# Function to keep track of strings until the sting is 100% correct
def best_string():
    word, score = compare_string()
    count = 0

    # Call function until the string generated is completely correct.
    while score < 28:
        word, score = compare_string()
        print(word, score)
        count += 1
    print(word)
    print(len(word))


best_string()

