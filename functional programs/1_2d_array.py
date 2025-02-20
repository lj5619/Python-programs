# Program to print 2d array
def print_2d_array(rows,columns):
    number = []
    for i in range(rows):
        row = []  
        for j in range(columns):
           value = input(f"Enter element for position [{i}, {j}]: ")
           row.append(value)  
        number.append(row)

    for row in number:
        print(row)

# Take input for rows and columns
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
print_2d_array(rows,columns)