"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def is_number_a_telemarketer(number):
    return number.startswith('140')


not_telemarketers = set()
telemarketers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for row in texts:
        if is_number_a_telemarketer(row[0]):
            not_telemarketers.add(row[0])
        if is_number_a_telemarketer(row[1]):
            not_telemarketers.add(row[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        if is_number_a_telemarketer(row[0]):
            telemarketers.add(row[0])
        if is_number_a_telemarketer(row[1]):
            not_telemarketers.add(row[1])

for key in telemarketers:
    if key in not_telemarketers:
        telemarketers.remove(key)

print("These numbers could be telemarketers: {}".format(sorted(telemarketers)))

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

"""
Opening the "texts.csv" file in read mode                  -- 1 instruction
reading the csv file                                       -- 1 instruction
Adding each line from "texts.csv" to the list              -- m instructions (Assuming there are m lines to the file)
Loop goes for m time, with worst case all the if conditions
will be true and will be executed                          -- m instructions (for creating rwo variables)
                                                           -- 6m instructions 
                                                                The following instructions execute of each item in loop
                                                                (. 2 if conditions
                                                                 . 2 function calls
                                                                 . each if condition has 1 instruction to add element to set. 
                                                                    So total 2 instructions. 
                                                                )
                                                                

Opening the "calls.csv" file in read mode                  -- 1 instruction
reading the csv file                                       -- 1 instruction
Adding each line from "calls.csv" to the list              -- n instructions (Assuming there are n lines to the file)
Loop goes for n time, with worst case all the if conditions
will be true and will be executed                          -- n instructions (for creating rwo variables)
                                                           -- 6n instructions 
                                                                The following instructions execute of each item in loop
                                                                (. 2 if conditions
                                                                 . 2 function calls
                                                                 . each if condition has 1 instruction to add element to set. 
                                                                    So total 2 instructions. 
                                                                )

Loop runs n times and within loop there are 2 instructions
 which will run n times assuming all if conditions are true 
 so total instructions with loop                           -- 2n instructions

Print will take total                                      -- 2 instructions + nlogn instructions (sorting n elements
                                                                                assuming all the number are telemarketers)

Worst case performance = O(1+1+m+m+6m+1+1+n+n+6n+2n+2+nlogn) = O(6+8m+8n+nlogn) ~=O(m+n+nlogn) for large values 
                                                                                        of m and n

"""