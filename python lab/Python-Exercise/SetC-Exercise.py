# Wed 19 Augest
# Set C: Python Shorthand & Sequences
# Exercise 1: The Verstaile Greeter
def greet(name="Guest",time_of_day= "day"):
    return print("Good {}, {}!".format(time_of_day,name))
#Test Function
greet()
greet("Raghad","Morning")
greet(time_of_day="morning",name="Nesma")

# Exercise 2: Ternay Grade Check
def ternay_grade_check(score):
    result = "Pass" if score >= 60 else "Fail"
    print("The score is: {}".format(score))
    print("The result is: {}".format(result))
#Test Function
ternay_grade_check(85)
ternay_grade_check(50)

# Exercise 3: The List Swap