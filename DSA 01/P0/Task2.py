"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Solution (Finding the longest call)
call_durations = {}

for call_record in calls:
    if call_record[0] not in call_durations:
        call_durations[call_record[0]] = int(call_record[3])
    else:
        call_durations[call_record[0]] += int(call_record[3])

    if call_record[1] not in call_durations:
        call_durations[call_record[1]] = int(call_record[3])
    else:
        call_durations[call_record[1]] += int(call_record[3])

largest_key = ""
largest_value = 0
for key, value in call_durations.items():
    if value > largest_value:
        largest_key = key
        largest_value = value

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    largest_key, largest_value))

