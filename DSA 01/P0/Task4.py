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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Solution

# First create a universal set.
universal_set = set()

# Create set containing people who send text, receive text or receive incoming calls.
not_telemarketers = set()

# Loop through the call record
for record in calls:
    caller = record[0]
    receiver = record[1]

    universal_set.add(caller), universal_set.add(receiver), not_telemarketers.add(receiver)

# Loop through the text record
for record in texts:
    sender = record[0]
    receiver = record[1]
    universal_set.add(sender), universal_set.add(receiver), not_telemarketers.add(sender)
    not_telemarketers.add(receiver)

# Generate the complement set.
possible_telemarketers = universal_set - not_telemarketers
possible_telemarketers = list(possible_telemarketers)
possible_telemarketers.sort()

print("These numbers could be telemarketers:")
for number in possible_telemarketers:
    print(number)
