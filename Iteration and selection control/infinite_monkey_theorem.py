import random
import string


def generate_string():
    alpha = list(string.ascii_lowercase)
    alpha.append(' ')
    word = ''
    for x in range(0, 27):
        y = random.randint(0, 26)
        word = word + alpha[y]

    return word


def compare_string():
    word = generate_string()
    goal = 'methinks it is like a weasel'
    score = 0
    for items in range(0, len(word)):
        if word[items] == goal[items]:
            score += 1
    return word, score


def best_string():
    word, score = compare_string()
    best_score = score
    count = 0
    while score != 27:
        if count == 1000:
            word, score = compare_string()
            if score > best_score:
                best_score = score
            print(best_score)
            count = 0
            best_score = 0
        else:
            word, score = compare_string()
            if score > best_score:
                best_score = score

        count += 1

best_string()