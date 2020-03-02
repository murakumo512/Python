num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))


switcher = {
        0: zero,
        1: one,
        2: two

def zero():
    minus = num1 - num2
    return "zero"
 
def one():
    plusss = num1 + num2
    return "one"
 
def two():
    complit = num1 * num2
    return "two"
    }
 
 
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
 
Input: numbers_to_strings(1)
Output: One
 
Input: switcher[1]=two #changing the switch case
Input: numbers_to_strings(1)
Output: Two