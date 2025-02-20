# Program to find Harmonic number

# Taking input from the user
number = int(input("Enter the Harmonic value N: "))
harmonic=0

# Ensuring N is not 0
if number == 0:
    print('Number can not be 0 ')
else:
    for i in range(1,number+1):
        harmonic= harmonic + (1/i)

    print(f'The {number} harmonic value is {harmonic}')
    