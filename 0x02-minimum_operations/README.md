# MINIMUM OPERATIONS - PYTHON

### PROBLEM
In a text file, there is a single character, `H`. 
our text editor can execute only two operations in
this file: `Copy All` and `Paste`.
Given a number `n`, write a method that calculates the
fewest number of operations needed to result 
in exactly `n` `H` characters in the file.

##### Example
```
n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```

- Returns An Integer, the number of operations
- If `n` is impossible to achieve, return `0`

### HOW I WORK IT OUT
- If `n` is null, 0, or not integer, Return 0
- Create a counter variable and initiate to 1
- Create an empty list that will contain list of counts
- Increment the counter while `n` is greater than 1
- - and while `n` is divisible by the counter,
divide `n` by counter and set the value to `n`
- append that counter value to the list
- after that loop is completed sum up
all the items in the list and return the sum
