"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_text_record = texts[0]
    print("First record of texts, {} texts {} at time " \
          "{}".format(first_text_record[0], first_text_record[1], first_text_record[2]))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_call_record = calls[-1]
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds"
          .format(last_call_record[0], last_call_record[1], last_call_record[2], last_call_record[3]))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
Opening the "texts.csv" file in read mode     -- 1 instruction
reading the csv file                          -- 1 instruction
Adding each line from "texts.csv" to the list -- n instructions (Assuming there are n lines to the file)
Fetching the first element from the list      -- 1 instruction
print statement                               -- 1 instruction + (fetch 3 records from list)
Worst Case Analysis O(1+1+n+1+1+3) = O(n+7) ~= O(n)


Opening the "calls.csv" file in read mode     -- 1 instruction
reading the csv file                          -- 1 instruction
Adding each line from "calls.csv" to the list -- m instructions (Assuming there are m lines to the file)
Fetching the first element from the list      -- 1 instruction
print statement                               -- 1 instruction + (fetch 3 records from list)
Worst Case Analysis O(1+1+m+1+1+3) = O(m+7) ~= O(m)
"""
