## Functions 1.
'''def summation():
    print("Enter 2 numbers to add up")
    a = int(input("First Number: "))
    b =  int(input("Second Number: "))
    add = a + b
    print("Sum: {}".format(add))

summation()'''

## Functions 2
'''def addition_2(*nums):
    num_list = list(nums)
    result = 0
    for num in num_list:
        result += num
    print(result)
    
    addition_2()'''

## Functions 3
'''def create_dict(**kwargs):
    arb_dict = dict()
    for key, value in kwargs.items():
        arb_dict[key] = value
    print(arb_dict)

create_dict(Name = 'Thomas', Age = 21, Race = 'White')'''

## Functions 4, 5, 6.
def addition():
    num_list = list()
    print("How many numbers would you like to add up ?")
    length = int(input("How many: "))
    result = 0
    while len(num_list) != length:
        num = int(input("Number: "))
        num_list.append(num)
    for nums in num_list:
        result += nums

    print("The sum of {} is {}".format(num_list, result))


def division():
    print("Division: Enter first the dividend and then the divisor ")
    dividend = int(input("Dividend: "))
    divisor = int(input("Divisor: "))
    result = dividend / divisor
    print("{} divided by {} is {} ".format(dividend,divisor,result))



def area_of_circle():
    print("Calculating Area of a circle.... ")
    Pie = 3.1415926535
    Radius = int(input("Radius: "))
    Area = Pie * (Radius ^2)
    print("The area of the circle with radius {} is {}".format(Radius, Area))

def fib():
    print("Generating fibonacci sequence..... ")
    end = int(input("to which index would you like this sequence to go: "))
    print("Generating Fibonacci up to {} digits: ".format(end))
    length = 0
    n1, n2 = 0, 1
    while length < end:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        length += 1

def Calculator():
    print("Calculator Functions; [1] Addition, [2] Division, [3] Area of a circle, [4] Fibonacci ")
    option = int(input("Enter 1, 2, 3 or 4: "))
    if option == 1:
        addition()

    elif option == 2:
        division()

    elif option == 3:
        area_of_circle()

    elif option == 4:
        fib()

    else:
        print("Inappropriate input detected.....")
        Calculator()

Calculator()












