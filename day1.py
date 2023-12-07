from itertools import combinations
from functools import reduce

# add input from inputfile to a list of numbers for each new line
expenses = [eval(expense) for expense in open("inputs/day1.txt").read().split('\n')]

# create a list of all possible combinations of elements
# use a filter to get only the combinations where the sum of the digits is 2020
# return the product of the digits
def combine(digits):
    expense_comb = list(combinations(expenses, digits))
    expense_comb = list(filter(lambda comb: sum(comb) == 2020, expense_comb))[0]
    return reduce(lambda a, b: a*b, expense_comb)

print(f"Deel 1: {combine(2)}")
print(f"Deel 2: {combine(3)}")