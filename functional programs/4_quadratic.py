# Program to find the quadratic roots
def quadratic(a:int,b:int,c:int):
    delta = b*b - 4*a*c
    root_1 = (-b + (delta)**0.5)/(2*a)
    root_2 = (-b - (delta)**0.5)/(2*a)
    print(f'The roots of the equation {a}x^2 + {b}x + {c} are {root_1} and {root_2}')
print('For the equation ax^2 + bx + c\n')
a=int(input('Enter value of a: '))
b=int(input("Enter value of b: "))
c=int(input('Enter value of c: '))
quadratic(a,b,c)