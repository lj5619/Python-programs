import time

print('Press enter to start the stopwatch: ')
input()
start_time = time.time()

print('Stopwatch is running.....')
print('Press enter to stop the stopwatch !')
input()
stop_time = time.time()

elapsed_time = stop_time - start_time
print(f'The elapsed time is {elapsed_time} seconds')