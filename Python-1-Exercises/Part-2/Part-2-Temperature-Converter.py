print("Temperature Converter")
temp_type = input("Would you like to convert Celcius(c) or Fahrenheit(f)?")
acceptable_inputs= ("c","f")
if temp_type.lower() not in acceptable_inputs:
    temp_type= input("incorrect input please input c or f: ")


Reading = int(input("What is the temperature in {} that you would like to convert?".format(temp_type)))

if temp_type.lower() == "c":
    end_type = "f"
elif temp_type.lower() == "f":
    end_type = "c"

c_to_f = (Reading * (9/5)) + 32
f_to_c = (Reading - 32) * (5/9)
print("your temperature in {} is {}".format(end_type, c_to_f))