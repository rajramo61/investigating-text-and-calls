"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

LONGEST_TIME = 0
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        call_duration = int(row[3])
        if LONGEST_TIME < call_duration:
            LONGEST_TIME = call_duration

print("{} spent the longest time, <total time> seconds, on the phone during \
        September 2016.".format(LONGEST_TIME))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

