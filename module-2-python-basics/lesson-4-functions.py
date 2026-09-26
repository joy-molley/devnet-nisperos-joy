"""
Module 2 — Lesson 4: Functions
Student: [Joy Nisperos]
Date: [September 26,2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Function is a reusable block of code that performs a task,
 we can put code inside a function and call the
function whenever we need it.]


============================================
KEY VOCABULARY
============================================
- function : a reusable block of code that performs a task
- def : keyword to use to create a function
- parameter: variable listed insise a function
- argument: the actual value given to a function when calling it 
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_total(amount1, amount2, amount3):
    total = (amount1 + amount2 + amount3)
    return total

total_amount = calculate_total(150, 200, 250)

print("Total amount:", total_amount)



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I get confused with the arguments and parameter.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[Functions are connected with loops because we can use them inside 
the functions.Functions make the code clean and organize.]
"""
