# Program to print the wind chill

def wind_chill(temp: int,speed: int):
    chill = 35.74 + 0.6215*temp + (0.4275*temp - 35.75) * speed**0.16
    print(f'The effective temperature (wind chill) is {chill} Fahrenheit')

temperature = float(input('Enter the temperature in Fahrenheit: '))
wind_speed = float(input('Enter the wind speed in miles per hour: '))
# checking the condition

if (temperature>50) or (wind_speed > 120 ) or (wind_speed < 3):
    print('Invalid value entered')
else:
    wind_chill(temperature,wind_speed)