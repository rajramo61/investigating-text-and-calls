"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

not_telemarketers = set()
telemarketers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for row in texts:
        not_telemarketers.add(row[0])
        not_telemarketers.add(row[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        telemarketers.add(row[0])
        not_telemarketers.add(row[1])

telemarketers -= not_telemarketers

print("These numbers could be telemarketers:")
for number in sorted(telemarketers):
    print(number)

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
will be true and will be executed                          -- 
                                                           -- 4m instructions 
                                                                The following instructions execute of each item in loop
                                                                (. 2 instructions for fetching values from indices
                                                                 . 2 instructions for adding values to set 
                                                                )
                                                                

Opening the "calls.csv" file in read mode                  -- 1 instruction
reading the csv file                                       -- 1 instruction
Adding each line from "calls.csv" to the list              -- n instructions (Assuming there are n lines to the file)
Loop goes for n time, with worst case all the if conditions
will be true and will be executed                          -- 4m instructions 
                                                                The following instructions execute of each item in loop
                                                                (. 2 instructions for fetching values from indices
                                                                 . 2 instructions for adding values to set 
                                                                )

telemarketers -= not_telemarketers                          -- 2n instructions (As it has to go in loop and remove the
                                                                                telemarketers entry. So an if condition 
                                                                                and delete statement. Total 2 statements 
                                                                                n times.)

Print will take total                                      -- 1 instructions + nlogn instructions (sorting n elements
                                                                                assuming all the number are telemarketers)
                                                                            + n instructions for printing n values

Worst case performance = O(1+1+m+4m+1+1+n+n+4n+2n+1+nlogn+n) = O(6+5m+7n+nlogn) ~=O(m+n+nlogn) for large values 
                                                                                        of m and n

"""