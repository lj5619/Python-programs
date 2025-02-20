# Program to find factors
def prime_factors(number: int):
    prime = []
    i=2
    while i*i <= number:
        while number%i == 0:
            prime.append(i)
            number//=i
        i+=1    
    if number > 1:
        prime.append(number)
    return prime


number = int(input('Enter a number to find the prime factors: '))
print(f'The prime factors are {prime_factors(number)}')

    


