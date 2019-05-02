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
    for key in telemarketers_who_send_text:
        if telemarketers_who_make_call.get(key) is not None:
            del telemarketers_who_make_call[key]
else:
    for key in telemarketers_who_make_call:
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

"""
Opening the "texts.csv" file in read mode                  -- 1 instruction
reading the csv file                                       -- 1 instruction
Adding each line from "texts.csv" to the list              -- m instructions (Assuming there are m lines to the file)
Loop goes for m time, with worst case all the if conditions
will be true and will be executed                          -- m instructions (for creating rwo variables)
                                                           -- 3m instructions 
                                                                repeat m times 3 actions below
                                                                (if condition, 
                                                                get 0th element from list
                                                                function call and statement in function)
Add entry to dictionary telemarketers_who_send_text        -- 2 instructions

Opening the "calls.csv" file in read mode                  -- 1 instruction
reading the csv file                                       -- 1 instruction
Adding each line from "calls.csv" to the list              -- n instructions (Assuming there are n lines to the file)
Loop goes for n time, with worst case all the if conditions
will be true and will be executed                          -- n instructions (for creating rwo variables)
                                                           -- 3n instructions 
                                                                repeat n times 3 actions below
                                                                (if condition, 
                                                                get 0th element from list
                                                                function call and statement in function)
Add entry to dictionary telemarketers_who_make_call        -- 2 instructions


The last if/else condition will execute on basis if m (number of text messages sent) is less 
or n (number of calls) is less. Assuming m is less.

Check if condition                                         -- 3 instructions
Loop runs m times as m is less                             -- m instructions
Within loop there are 4 instructions which will run m times
assuming all if conditions are true so total instructions 
with loop                                                  -- 4m instructions

Print will take total                                      -- 4 instructions

Worst case performance = O(1+1+m+m+3m+2+1+1+n+n+3n+2+3+m+4m+4) = O(16+10m+5n) ~=O(m+n) for large values 
                                                                                        of m and n

"""