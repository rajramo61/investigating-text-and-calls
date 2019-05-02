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
        distinct_phone_numbers[row[1]] = 1

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        distinct_phone_numbers[row[0]] = 1
        distinct_phone_numbers[row[1]] = 1

print("There are {} different telephone numbers in the records.".format(len(distinct_phone_numbers)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Opening the "texts.csv" file in read mode     -- 1 instruction
reading the csv file                          -- 1 instruction
Adding each line from "texts.csv" to the list -- n instructions (Assuming there are n lines to the file)
for loop has 2 statements with 2 instructions -- 4n instructions
(add to the dictionary and get the value from list using index) each 
Total instructions = 1+1+n+4n = 5n + 2

Steps are same for "calls.txt", assuming it has m lines
Total instructions = 1+1+m+4m = 5m + 2
Print will take 3 more instructions (1 Print method, 1 format method and 1 len for dictionary)

Worst case performance = O(5n + 2 + 5m + 2 + 3) = O(5n + 5m + 7) 
~= O(m+n) if m and n are large numbers.
"""