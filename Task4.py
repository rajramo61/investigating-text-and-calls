"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def is_number_a_telemarketer(number):
    return number.startswith('140')


telemarketers_who_send_text = {}
telemarketers_who_make_call = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for row in texts:
        if is_number_a_telemarketer(row[0]):
            telemarketers_who_send_text[row[0]] = 1

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        if is_number_a_telemarketer(row[0]):
            telemarketers_who_make_call[row[0]] = 1

if len(telemarketers_who_send_text) < len(telemarketers_who_make_call):
    for key in telemarketers_who_send_text.keys():
        if telemarketers_who_make_call.get(key) is not None:
            del telemarketers_who_make_call[key]
else:
    for key in telemarketers_who_make_call.keys():
        if telemarketers_who_send_text.get(key) is not None:
            del telemarketers_who_make_call[key]

print("These numbers could be telemarketers: {}".format(len(list(telemarketers_who_make_call))))

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

