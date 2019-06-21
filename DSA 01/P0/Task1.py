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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Solution (Number of different telephone numbers in the records).
distinct_set = set()

# Loop through the records and add the different numbers to the set
for i in texts:
    distinct_set.add(i[0]), distinct_set.add(i[1])
for j in calls:
    distinct_set.add(j[0]), distinct_set.add(j[1])


# Print the total number of distinct phone numbers.
print("There are {} different telephone numbers in the records.".format(len(distinct_set)))
