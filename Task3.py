"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

"""
Calls initiated from Bangalore can be determined by the area code only.
As mobile number does not provide info for the location 
"""


def is_number_from_bangalore(number):
    return number.startswith('(080)')


def is_number_mobile_user(number):
    return number.startswith('7') or number.startswith('8') or number.startswith('9')


def is_number_a_telemarketer(number):
    return number.startswith('140')


calls_initiated_from_bangalore_to_fixed_line = {}
calls_initiated_from_bangalore_to_mobile = {}
calls_initiated_from_bangalore_to_telemarketer = {}
calls_initiated_from_bangalore_to_others = {}
calls_targeted_to_bangalore = []
calls_started_to_bangalore = []
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        caller = row[0]
        callee = row[1]
        if is_number_from_bangalore(caller):
            calls_started_to_bangalore.append(caller)
            if callee.startswith('('):
                calls_initiated_from_bangalore_to_fixed_line[callee[1:4]] = 1
                if is_number_from_bangalore(callee):
                    calls_targeted_to_bangalore.append(callee)
            elif is_number_mobile_user(callee):
                calls_initiated_from_bangalore_to_mobile[callee[0:4]] = 1
            elif is_number_a_telemarketer(callee):
                calls_initiated_from_bangalore_to_telemarketer[callee[0:4]] = 1
            else:
                calls_initiated_from_bangalore_to_others[callee] = 1

calls_to_fixed_lines_mobile_telemarketers = list(calls_initiated_from_bangalore_to_fixed_line) \
                                            + list(calls_initiated_from_bangalore_to_mobile) \
                                            + list(calls_initiated_from_bangalore_to_telemarketer)
total_calls_from_bangalore = calls_to_fixed_lines_mobile_telemarketers + list(calls_initiated_from_bangalore_to_others)

print("The numbers called by people in Bangalore have codes: {}".format(
    calls_to_fixed_lines_mobile_telemarketers
))

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    (len(calls_targeted_to_bangalore)/len(calls_started_to_bangalore)) * 100))

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
