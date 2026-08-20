# Wed 19 Augest
# Set B: List Algorithms
# Exercise 1: Biggie Size: Change positive numbers to the string "big".
def biggie_size(list):
    print("The list is: {}".format(list))
    for i in range(len(list)):
        if list[i]>0:
            list[i] = "big"
    return list
#Test Function
print("Biggie Size List: {}".format(biggie_size([-1,5,-2,3,-10,8])))
print("Biggie Size List: {}".format(biggie_size([-1,-2,-3,-4,-5,-6])))
print("Biggie Size List: {}".format(biggie_size([1,2,3,4,5,6])))

# Exercise 2: Count Positives: Change the last value in a list to the total count of positive numbers.
def count_positive(list):
    print("The list is: {}".format(list))
    sum = 0
    for i in list:
        if i > 0:
            sum = sum + i
    list[len(list)-1] = sum
    return list
#Test Function
print("Count positives List: {}".format(count_positive([-1,2,-3,4,-5,-6,7])))
print("Count positives List: {}".format(count_positive([1,2,3,4,5,6,7,8])))
print("Count positives List: {}".format(count_positive([-1,-2,-3,-4,-5,-6,-7,-8])))

#Exercise 3: Sum Total: Return the sum of all values in a list.
def sum_total(list):
    print("The list is: {}".format(list))
    sum = 0
    for i in list:
        sum = sum + i
    return sum
#Test Function
print("The sum of all values in the list is: {}".format(sum_total([1,2,3,4,5,6,7,8])))
print("The sum of all values in the list is: {}".format(sum_total([-1,-2,-3,-4,-5,-6,-7,-8])))
print("The sum of all values in the list is: {}".format(sum_total([-1,2,-3,4,-5,6,-7,8])))