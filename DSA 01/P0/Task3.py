"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Solution A: (Not sure this is the most efficient way but)..
distinct_codes = {}
for i in calls:

    # Check if the caller is using a fixed line from Bangalore.
    if i[0].startswith("(080)"):
        receiver = i[1]

        # Check if the receiver has a fixed line that is not from Bangalore
        if receiver[0] == "(" and (receiver[:5] != "(080)"):
            code = receiver.split(")")[0]+")"

        # Check if the receiver has a fixed line from Bangalore
        elif receiver[:5] == "(080)":
            code = "(080)"

        # Check if receiver has a Telemarketers' number
        elif receiver[:3] == "140":
            code = "140"

        # Check if receiver has a mobile number
        else:
            code = i[1][:4]

        # Add code to the dictionary
        if code not in distinct_codes.keys():
            distinct_codes[code] = 1
        else:
            distinct_codes[code] += 1

# Get the list of all the codes
code_list = list(distinct_codes.keys())


# Additional nLogn complexity. I am not sure this is efficient.
code_list.sort()

print("The numbers called by people in Bangalore have codes:")
for code in code_list:
    print(code)

# Solution 2
accumulator = 0

# get the total number of calls made from fixed lines in Bangalore.
for value in distinct_codes.values():
    accumulator += value

# Get the percentage of those calls that belong to other fixed lines in Bangalore
percentage = (distinct_codes["(080)"]/accumulator)*100

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in "
      "Bangalore.".format(percentage))

