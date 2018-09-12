print('Hello World!')


# For Loop Demo

exampleList = [1, 5, 6, 7, 8, 345, 5547, 3464]

for eachNumber in exampleList:
    print(eachNumber)


x = 5
y = 8

# in if-else condition in python if the if condition and else condition both are fulfilled then both values will get printed
# Like here first if condition is satisfied and else condition are also getting satisfiled.
if x < y :
    print('x is greater than y')
if x > 55:
    print('x is greater than 55')
else:
    print('x is not greater than y')

# if, else if example

a = 5
b = 10
c = 22

if a > b:
    print('a is greater than b')
elif b > a:
    print('b is greater than a')
elif a > c:
    print('a is greater than c')
else:
    print('no execution of if-else statement')


# function tutorial

def example():
    print('we are inside function loop')

    z = 6 + 3
    print(z)


example()

# function with parameter

def simple_addition(num1, num2):
    answer = num1 + num2

    print('num1 is', num1)
    print(answer)

simple_addition(4, 7)

# function with Default Parameter

def simple(num1, num2):
    pass

# if we have predefined values as parameter in our function then we don't need to paas another params while calling that function
def simple(num1, num2 = 5):
    print(num1, num2)

simple(10)

def basic_window(width, height, font = 'TNR', bgc = 'W', scrollbar = True):
    print(width, height, font, bgc)

basic_window(500, 350, bgc='r')


# Global and Local Variable

p = 6

def example():
    globp = p
    print(globp)

    globp += 5

    return globp

a = example()

print(a)



    

    

    
