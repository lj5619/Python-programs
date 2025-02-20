# Program to find power of 2

# Taking argument power from the user
power = int(input("Enter the power value: "))

# Making sure the power is less than 31
if power>31:
    print('Enter number less than 31')
else:
    print(f'Powers of 2 that are less than 2^{power} ({2**power}):\n')
    for i in range (0,power):
        print(f'2^{i} = {(2**i)}')
