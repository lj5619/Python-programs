# Function to calculate euclidean distance
def distance(x:int,y:int):
    euclidean_distance = (x*x+y*y)**0.5
    return euclidean_distance

# Taking input from user
x = int (input('Enter the value for x: '))
y = int (input('Enter the value for y: '))
print(f'The Euclidean distance between ({x},{y}) from (0,0) is {distance(x,y)}')