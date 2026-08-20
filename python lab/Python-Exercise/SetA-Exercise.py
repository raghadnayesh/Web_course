# Wed 19 Augest
# Set A: Basic List Logic:
# Exercise 1: Countdown: Create countdown(5) -> should return [5,4,3,2,1].
def countdown(num):
    countdown_list = []
    for i in range (num + 1):
        countdown_list.append(num-i)
    return countdown_list
#Test Function
print(countdown(5))
print(countdown(8))

# Exercise 2: Print and Return: print_and_return([1,2]) -> should print 1 and return 2.
def print_and_return(list):
    print("The entered list is: {}".format(list))
    print("The first index in the list is {}".format(list[0]))
    return list[len(list)-1]
#Test Function
x1 = print_and_return([1,2])
print("The last index of the list is: {}".format(x1))
x2 = print_and_return([3,6,9])
print("The last index of the list is: {}".format(x2))

# Exercise 3: First Plus Length: first_plus_length([1,2,3,4,5]) -> should return 6(1+5)
def first_plus_length(list):
    y = len(list) + list[0]
    return y
#Test Function
list1 = [1,2,3,4,5]
print("The list is: {}".format(list1))
print("First index plus length equal to: {}".format(first_plus_length(list1)))

list2 = [5,3,5,7,20,17,2]
print("The list is: {}".format(list2))
print("First index plus length equal to: {}".format(first_plus_length(list2)))

# Exercise  4: Values Greater than Second: values_greater_than_second([5,2,3,2,1,4]) -> print 3 (the count) and return [5,3,4]
def values_greater_than_second(list):
    print("The list is: {}".format(list))
    greater_than_second = []
    for i in list:
        if i > list[1]:
            greater_than_second.append(i)
    print("There is {} indecies that greater than the second index.".format(len(greater_than_second)))
    return greater_than_second
#Test Function
y1 = values_greater_than_second([5,2,3,2,1,4])
print("This is the list of the values greater than second: {}".format(y1))

y2 = values_greater_than_second([10,3,1,8,6,2,3,-1,5])
print("This is the list of the values greater than second: {}".format(y2))

# Exercise  5: This length, That Value: length_and_value(4,7) -> [7,7,7,7]
def length_and_value(list):
    print("The list is: {}".format(list))
    length_and_value_list = []
    if len(list)<2:
        return print("Invalid Value, list length must be at least 2")
    else:
        for i in range(list[0]):
            length_and_value_list.append(list[len(list)-1])
    return length_and_value_list
#Test Function
z1 = length_and_value([4,7])
print("This Length, That Value list is: {}".format(z1))

z2 = length_and_value([4])
print("This Length, That Value list is: {}".format(z2))

z3 = length_and_value([5,9,4,2,3])
print("This Length, That Value list is: {}".format(z3))

# DONE!! 😁👍✌️