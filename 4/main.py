import re
def read_file():
    f = open("input.txt","r")
    contents = f.read()
    return contents

def calculate(input):
    amount = 0
    lower = int(input[0])
    higher = int(input[1])
    for number in range(lower, higher):
        adjacent = False
        increasing = True
        prev = "0"
        for char in str(number):
            if(prev in char):
                adjacent = True
            if(int(prev) > int(char)):
                increasing = False
            prev = char
        if(adjacent and increasing):
            amount += 1
    return amount

def calculate2(input):
    amount = 0
    lower = int(input[0])
    higher = int(input[1])
    for number in range(lower, higher):
        adjacent = False
        increasing = True
        prev = "0"
        prevprev = "-1"
        for char in str(number):

            if(int(prev) > int(char)):
                increasing = False
            prevprev = prev
            prev = char
        if(adjacent and increasing):
            print(number)
            amount += 1
    return amount

def main():
    contents = read_file()
    input = contents.split("-")
    amount = calculate(input)
    amount2 = calculate2(input)
    return amount, amount2

print("Result: ", main())


#     It is a six-digit number.
#     The value is within the range given in your puzzle input.
#     Two adjacent digits are the same (like 22 in 122345).
#     Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#
# Other than the range rule, the following are true:
#
#     111111 meets these criteria (double 11, never decreases).
#     223450 does not meet these criteria (decreasing pair of digits 50).
#     123789 does not meet these criteria (no double).
#
# How many different passwords within the range given in your puzzle input meet these criteria?
