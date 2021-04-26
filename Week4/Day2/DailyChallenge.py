# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
import calendar
from datetime import datetime
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
# Bonus : If they were born on a leap year, display two cakes !

# get birthdate and separate year
birthday = input("Enter your birthday (mm/dd/yyyy): ")
x = birthday.split('/')
year = (x[2])

# get current year
currentyear = datetime.now().year
# convert to age and get last digit of age
age = currentyear-int(year)
candles=str(age)[-1]

# if age is multiple of 10, convert 0 to 10 to display 10 candles
candles=int(candles)
if candles==0:
    candles=10

# calculate the number of dashes surrounding the candles
dash = int((12-candles)/2)

# print cake
cake=[" "*4+"_"*dash +"i"*candles +"_"*dash,"   |:H:a:p:p:y:|"," __|"+"_"*11+"|__", "|"+"^"*17+"|","|:B:i:r:t:h:d:a:y:|","|"+" "*17+"|","~"*19]
print("\n".join(cake[:]))

# if leap year print a second cake
if calendar.isleap(int(year)):
    print('\n'.join(cake[:]))
    print("An extra cake for the leap year.")

    

