def match(query, pattern):
    # Second pointer
    pattern_pointer = 0

    # Looping through the given query
    for i in range(len(query)):

        # If pattern is not complete
        if pattern_pointer < len(pattern):
            # If Text in query matches text in pattern
            if query[i] == pattern[pattern_pointer]:
                pattern_pointer += 1

            # If they do not match and text is upper, return false
            elif query[i].isupper():
                return False

        # If upper case appears after matching pattern, Return false
        else:
            if query[i].isupper():
                return False

    # Check if string matches patter
    if pattern_pointer == len(pattern):
        return True
    return False


print(match("ForceFeedBack", "FB"))