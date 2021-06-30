class Loan_Eligibility:
    def __init__(self,age,salary):
        self.age = age
        self.salary = salary
        if 21 < self.age < 30 and self.salary > 21000:
            self.loan_amount = 50000
        elif self.age >= 30 and 35000 < self.salary < 50000:
            self.loan_amount = 75000
        elif self.age >= 30 and self.salary > 50000:
            self.loan_amount = 10000
        else:
            self.loan_amount = 0

    @property
    def loan(self):
        if self.loan_amount != 0:
            return("You are eligible for a loan of up to {}".format(self.loan_amount))
        else:
            return("You are not eligible for a loan")

Name = input("What is your name? ")
age = int(input("How old are you? "))
salary = int(input("What is your annual salary? "))

Name = Loan_Eligibility(age, salary)
print(Name.loan)
