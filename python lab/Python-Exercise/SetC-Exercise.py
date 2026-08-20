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
fruits = ["apple", "banana", "cherry"]
print("List before Swap: {}".format(fruits))
fruits[0],fruits[2]=fruits[2],fruits[0]
print("List after Swap: {}".format(fruits))

# Exercise 4: Slicing Snippets
text = "Coding is fun"
print("Get just the word Coding: {}".format(text[0:6]))
print("Get just the word fun: {}".format(text[10:13]))
print("Get the whole string in reverse: {}".format(text[::-1]))

# Exercise 5: Sequance Analytics
data = [42, 10, 77, 2, 15]
print("The data list is: {}".format(data))
print("The largest number of the data list is: {}".format(max(data)))
print("The total sum of the numbers in the data list is: {}".format(sum(data)))
sorted_data = sorted(data)
print("Data list after sorted from smallest to largest: {}".format(sorted_data))