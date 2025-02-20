# Checking for triples in array
def triples(array):
    flag= 0
    n=len(array)
    for i in range (0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(array[i]+array[j]+array[k]==0):
                    print(f'{array[i]} , {array[j]} , {array[k]}')
                    flag= 1
    if(flag==0):
        print('Not found')

array = []
num = int(input("Enter total number of elements: "))

# Taking array from user
for i in range(num):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)
triples(array)
