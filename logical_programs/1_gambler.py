# Program to find number of wins and percentage of win loss in gambling
import random

stake = int(input('Enter the Stake: '))
goal = int(input('Enter the goal: '))
num = int(input('Enter number of times: '))

win=0
loss=0
turn=0
while stake != goal and stake > 0 and turn < num:
    turn += 1
    stake -= 1
    odds = random.uniform(0,1)
    if odds>0.5:
        win += 1
        stake += 1
    else:
        loss += 1
        stake -= 1

win_perc = win/num * 100
loss_perc = loss/num * 100       
print(f'The number of wins are {win} , the win percentage is {win_perc}% and the loss percentage is {loss_perc}% and final amount left is {stake}')

