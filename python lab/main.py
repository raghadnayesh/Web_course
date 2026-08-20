name = "Raghad"
hoppy = "Drawing"
print(f"My name is {name} and I love {hoppy}")
print("My name is {} and I love {}".format(name,hoppy))

print(name.upper())
print(name.lower())
print(name.endswith('d'))
print(name.title())
print(name.isalnum())
print(name.isalpha())
print(name.join(hoppy))

for i in range(0,10):
    if (i%2 == 0):
        print(i)

location = (12.345, 156.568) #Tuple
print(location) 
print(type(location))
print(location[0])
print(location[1])

location = [12.345, 156.568] #List
print(location)
print(type(location))
print(location[0])
print(location[1])
location[0] = 10
print(location)

profile = {"name": "Raghad", "age":25, "hoppy": "Drawing"}
for i in profile.keys():
    print(i)

for i in profile.values():
    print(i)

for i in profile.items():
    print(i)

#Exercise 1
list = []
for i in range (0,6):
    list.append(5-i)

print(list)

#Exercise 2
def print_and_return(a,b):
    print(a)
    return b
    
print_and_return(1,2)

#Exercise 3
def first_plus_length(list):
    length = list[len(list)]

def sum(n=5,m=6):
    return n+m

print(sum(n=4,m=3))
print(sum)

x =3
y =7
x,y = y,x
print(y)
print(x)