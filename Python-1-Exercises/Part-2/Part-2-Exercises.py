user_int = int(input("Give me an integer: "))

if user_int % 2 == 0:
    print("This integer is even")
elif user_int % 4 == 0:
    print("Integer is even and a multiple of 4")
else:
    print("This integer is odd")

user_int_2 = int(input("Give me another integer: "))
if user_int_2 % 3 == 0:
    print("fizz")
if user_int_2 % 5 == 0:
    print("buzz")