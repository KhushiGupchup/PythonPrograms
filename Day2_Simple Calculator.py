#simple calculator
a= float(input("Enter first number"))
b= float(input("Enter Second number"))

#perform arithmetic operation

addition = a + b
subtraction = a -b
multiplication = a * b
division =a / b if b !=0 else "cannot divide by zero"


#display result

print("\n Calculator result")

print(f"Addition : {a} + {b} = {addition}")
print(f"Subtraction : {a} - {b} = {subtraction}")
print(f"Multiplication : {a} x {b} = {multiplication}")
print(f"Division : {a } / {b}",{division})

