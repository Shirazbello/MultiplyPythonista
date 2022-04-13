#Function for Taken Input Values
def Takeinput():
    first=int(input('Enter your First number for Multiplication:'))
    second=int(input('Enter your second number for Multiplication:'))
    return first, second;
#Function for Multiplication Work
def Multiply(func):
    print('*'*4,'Multiplying two integers','*'*4)
    first,second=func()
    print(f'{first} * {second} = {first * second}')

#Calling the Multiplication Function
Multiply(Takeinput)