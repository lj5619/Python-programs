# Program to take user input and replace string template

# Declaring a variable to take input from user
user_name = input('Enter your Username: ')

#Checking if length is minimum 3
if len(user_name)>= 3:
    print(f'Hello {user_name}, How are you?')
else:
    print('Username should have atleast 3 characters')

