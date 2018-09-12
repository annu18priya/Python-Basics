# Save File to system

text = 'Sample text which should be saved in the system'

saveFile = open('/Users/annpriya/Desktop/exampleFile.txt', 'w') # write(w), read(r)
saveFile.write(text)
saveFile.close() # make sure to close the file



appendMe = '\nNew bit of information'
appendFile = open('exampleFile.txt', 'a') #a (append)
appendFile.write(appendMe)
appendFile.close()



class Calculator:

    def addition(x, y):
        added = x + y
        print(added)
        
    def subtraction(x, y):
        subtract = x - y
        print(subtract)

    def multiplication(x, y):
        multiply = x * y
        print(multiply)

    def division(x, y):
        divided = x / y
        print(divided)

Calculator.addition(4, 6)


# Get Input Value Demo

x = input('What is your name? ')
print('Hello', x)


