from math import pi
variable = pi
print(f"Using Numeric variable = {variable}")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")
print()
variable = "Python 3.9"
print(f"Using String variable = {variable}")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")

variable = 1200356.8796
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places: {variable:.2f}")
print(f"With four decimal places: {variable:.3f}")
print(f"With two decimal places and a comma: {variable:,.2f}")
print(f"With a forced plus sign: {variable:+.2f}")
print()
variable *= -1
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places and a comma: {variable:,.2f}")

print(f'{"Number":>10s}{"Square":>10s}{"Cube":>10s}')
x = 1.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 2.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 3.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')