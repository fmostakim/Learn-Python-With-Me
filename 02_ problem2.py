def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature: "))
print(f"{f_to_c(f)} degree celcius")