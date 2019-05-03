"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

LONGEST_TIME = 0
PHONE_NUMBER = 0
number_and_duration_tracker = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        call_duration = int(row[3])
        caller = row[0]
        callee = row[1]
        if number_and_duration_tracker.get(caller) is None:
            number_and_duration_tracker[caller] = call_duration
        else:
            number_and_duration_tracker[caller] = number_and_duration_tracker.get(caller) + call_duration

        if number_and_duration_tracker.get(callee) is None:
            number_and_duration_tracker[callee] = call_duration
        else:
            number_and_duration_tracker[callee] = number_and_duration_tracker.get(callee) + call_duration

for ph_number, call_duration in number_and_duration_tracker.items():
    if LONGEST_TIME < call_duration:
        PHONE_NUMBER = ph_number
        LONGEST_TIME = call_duration

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

Iterating over each item in list              -- n time the following instructions will be executed
    call_duration                                 -- 3 instructions (1 instruction to get data from array using array 
                                                                    index and one to convert string to integer
                                                                    assigning value to variable
                                                                    )
    caller                                        -- 2 instructions 
    callee                                        -- 2 instructions
    if/else: Both if condition will execute each
    time and either if or else will execute       -- 4 instructions (2 if conditions and 2 instructions within if or else
                                                                    based on condition is True or False)
So first loop will execute   ---- 11n instructions
                                                                    
Next loop will execute n times assuming maximum entries
It has 1 if condition and 2 assignments           -- 3 instruction
So second loop will execute  ---- 3n instructions

Print will take 2 more instructions (1 Print method, 1 format method)

Worst case performance == O(1+1+n+11n+3n+2) = O(14n+4) ~= O(n) if n is very large
"""
