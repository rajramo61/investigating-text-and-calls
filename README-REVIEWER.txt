Same details are there at the end of the each file as comments:

*********
TASK - 0
*********
======================================================================
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
======================================================================

*********
TASK - 1
*********
======================================================================
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
======================================================================

*********
TASK - 2
*********
======================================================================
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
======================================================================

*********
TASK - 3
*********
======================================================================
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
First print statement                                      -- 2 instruction (1 print and 1 format method)
Second print statement                                     -- 6 instructions (1 print
                                                                              1 format
                                                                              2 len
                                                                              1 division
                                                                              1 multiplication
                                                                              )

Worse case performance = O(1+1+n+n+2+2n+8+2n+2+6) = O(6n+20) ~= O(n) if n is very large
======================================================================



*********
TASK - 4
*********
======================================================================
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
======================================================================