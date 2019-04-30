"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

"""
Keeping data in dictionary will keep the records unique.
This will help to avoid additional logic to check duplicate records.
"""
distinct_phone_numbers = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for row in texts:
        distinct_phone_numbers[row[0]] = 1
        distinct_phone_numbers[row[2]] = 1

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        distinct_phone_numbers[row[0]] = 1
        distinct_phone_numbers[row[2]] = 1

print("There are {} different telephone numbers in the records.".format(len(distinct_phone_numbers)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
