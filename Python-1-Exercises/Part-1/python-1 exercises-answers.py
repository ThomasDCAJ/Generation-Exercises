#PART 1 STRINGS

first_name = 'Thomas'
last_name = 'Alva-Jorgensen'
full_name = ('{} {}'.format(first_name, last_name))

print(first_name)
print(last_name)
print(full_name)

#INTEGERS

First_int = 17
Second_int = 29
product = First_int * Second_int
Answer = ('The product of {} and {} is {}'.format(First_int,Second_int,product))
print(Answer)

#LISTS

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
thrd= people[2]
print(thrd)
ffth = people[-3]
print(ffth)
people2 = people[2:6]
print(people2)
print (people[0] == people[-1])

#INPUT
Name = input("What is your name?")
print(Name)
Num1 = int(input("give me an integer"))
Num2 = int(input("Now give me another integer"))
product = Num1 * Num2
print("Their product is {}".format(product))
Num3 = input("Another integer: ")
Num4 = input("And another integer: ")
print(Num3 is Num4)




