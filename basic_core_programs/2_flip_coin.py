# Flip Coin and print percentage of Heads and Tails
import random

#Function to print the percentage
def flip_coin(number_flips:int):
    heads=tails=0
    for flips in range(0,number_flips):
        result=random.uniform(0,1)
        if result < 0.5:
            tails+=1
        else:
            heads+=1
    head_perc=(heads/number_flips)*100
    tail_perc=(tails/number_flips)*100
    print(f'After {number_flips} flips, the percentage of heads is {head_perc} and the percentage of tails is {tail_perc}')    

# Taking input of number of times to flip coin
number_flips = int(input("Enter number of flips to Flip Coin: "))
if(number_flips<0):
    print('Enter positive number')
else:
    flip_coin(number_flips)


 