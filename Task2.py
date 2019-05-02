"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

LONGEST_TIME = 0
PHONE_NUMBER = 0
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        call_duration = int(row[3])
        ph_number = row[0]
        if LONGEST_TIME < call_duration:
            LONGEST_TIME = call_duration
            PHONE_NUMBER = ph_number

print("{} spent the longest time, {} seconds, on the phone during \
        September 2016.".format(PHONE_NUMBER, LONGEST_TIME))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

"""
Ignoring the text.csv as the solution for this problem does not require reading data from "texts.csv."

Opening the "calls.csv" file in read mode     -- 1 instruction
reading the csv file                          -- 1 instruction
Adding each line from "calls.csv" to the list -- n instructions (Assuming there are n lines to the file)
Iterating over each item in list              -- n instructions
get call duration from the line               -- 2 instructions (1 instruction to get data from array using array index and one to convert string to integer)
get phone number from the line                -- 2 instructions (1 instruction to get data from array using array index and one to convert string to integer)
if condition                                  -- 1 instructions
2 assignments within if condition:            -- 2 instructions
Print will take 2 more instructions (1 Print method, 1 format method)

Worst case performance == O(1+1+n+n+2+2+1+2) = O(2n+9) ~= O(n) if n is very large
"""
