"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


def is_number_from_bangalore(number):
    """
    Calls initiated from Bangalore can be determined by the area code only.
    As mobile number does not provide info for the location
    """
    return number.startswith('(080)')


def is_number_mobile_user(number):
    return ' ' in number and (number.startswith('7') or number.startswith('8') or number.startswith('9'))


def is_number_a_telemarketer(number):
    return number.startswith('140')


calls_initiated_from_bangalore_to_fixed_line = set()
calls_initiated_from_bangalore_to_mobile = set()
calls_initiated_from_bangalore_to_telemarketer = set()
calls_initiated_from_bangalore_to_others = set()

"""
Part B of the solution is based on all the calls initiated and destined to Bangalore.

One number can make many calls to different or to one number.
So using list is better choice as it will keep the duplicate numbers as well.
"""
calls_targeted_to_bangalore = []
calls_started_from_bangalore = []

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        caller = row[0]
        callee = row[1]
        if is_number_from_bangalore(caller):
            calls_started_from_bangalore.append(caller)
            if callee.startswith('('):
                index = callee.find(')')
                calls_initiated_from_bangalore_to_fixed_line.add(callee[1:index])
                if is_number_from_bangalore(callee):
                    calls_targeted_to_bangalore.append(callee)
            elif is_number_mobile_user(callee):
                calls_initiated_from_bangalore_to_mobile.add(callee[0:4])
            elif is_number_a_telemarketer(callee):
                calls_initiated_from_bangalore_to_telemarketer.add(callee[0:3])
            else:
                calls_initiated_from_bangalore_to_others.add(callee)

calls_to_fixed_lines_mobile_telemarketers = list(calls_initiated_from_bangalore_to_fixed_line) \
                                            + list(calls_initiated_from_bangalore_to_mobile) \
                                            + list(calls_initiated_from_bangalore_to_telemarketer)
total_calls_from_bangalore = calls_to_fixed_lines_mobile_telemarketers + list(calls_initiated_from_bangalore_to_others)

"""
Part A solution print
"""
print("The numbers called by people in Bangalore have codes:")
for codes in sorted(calls_to_fixed_lines_mobile_telemarketers):
    print(codes)

"""
Part B solution print
"""
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    round((len(calls_targeted_to_bangalore) / len(calls_started_from_bangalore)) * 100, 2)))

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

"""
Ignoring the text.csv as the solution for this problem does not require reading data from "texts.csv."

Opening the "calls.csv" file in read mode                  -- 1 instruction
reading the csv file                                       -- 1 instruction
Adding each line from "calls.csv" to the list              -- n instructions (Assuming there are n lines to the file)
Iterating over each item in list                           -- n instructions
Get the caller and callee details from row                 -- 2 instructions (one for each item)

The first if condition will execute for each items in list -- 2n instructions (1 if condition and one statement in 
                                                                                function call)
Rest all are dependent on the first if condition. 
But to get the worst case condition, assuming the most of
the instructions will be executed. Then will take the 2 
additional if condition path in the code.
So, I can see total number of instructions                  -- 8 instructions ( 
                                                                1 - append to list calls_started_from_bangalore
                                                                2 - if condition
                                                                2 - append to calls_initiated_from_bangalore_to_fixed_line
                                                                2 - if condition and function call
                                                                1 - append call to calls_targeted_to_bangalore
                                                                )
                                                                
For last 2 statements before print                          -- 2n (4 list conversion which should include adding n values
                                                                    to 4 different list object
                                                                    +
                                                                  3 list concatenation action on n elements
                                                                  which will eventually be copying n elements
                                                                  to the new lists. So n instructions to execute.
                                                                  )
                                                                sort from Python uses
                                                                Timsort-->https://en.wikipedia.org/wiki/Timsort
                                                                So,
First print statement                                      -- nlogn + 1 instruction (sorting n elements, 1 print)
Second print statement                                     -- 6 instructions (1 print
                                                                              1 format
                                                                              2 len
                                                                              1 division
                                                                              1 multiplication
                                                                              ) 

Worse case performance = O(1+1+n+n+2+2n+8+2n++nlogn+1+6) = O(6n+nlogn+19) ~= O(n+nlogn) if n is very large

"""
