from faker import Faker
# # Exercise 1
# # Instructions
# # Create a function that displays the current date.
# # Hint : Use the datetime module.
# from datetime import date,datetime

# def current_date():
#     today = date.today()
#     return today

# print(current_date())
# # Exercise 2
# # Instructions
# # Create a function that displays the amount of time left from now until January 1st.
# # (Example: the 1st of January is in 10 days and 10:34:01hours).

# def time_til_newyears(year):
#     now = datetime.now()
#     newyears = datetime(int(year), 1, 1, 00, 00, 00)
#     diff = newyears-now
#     print("Difference: ", diff)

# time_til_newyears(2022)
# time_til_newyears(2032)

# # Exercise 3
# # Instructions
# # Create a function that accepts a birthdate as an argument (in the format of your choice), then display a message stating how many minutes the user has been alive.
# def minutes_alive(year,month,day):
#     now=datetime.now()
#     birthdate=datetime(year,month,day,00,00,00)
#     diff=now-birthdate
#     total_minutes = int((diff.days*1440)+(diff.seconds/60))
#     return f'You have been alive {total_minutes} minutes'
    

# print(minutes_alive(1981,1,22))

# # Exercise 4
# # Instructions
# # Write a function that display today’s date.
# # The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# # Hint: Start by hardcoding the datetime and name of the upcoming holiday.

# def next_holiday():
#     now = datetime.now()
#     shavuot = datetime(2021, 5, 16, 18, 00, 00)
#     diff = shavuot-now
#     print(f"There are {diff} hours until Shavuot")

# next_holiday()

# # Exercise 5 : How Old Are You On Jupiter?
# # Instructions
# # Given an age in seconds, calculate how old someone would be on:
# # Earth: orbital period 365.25 Earth days, or 31557600 seconds
# # Mercury: orbital period 0.2408467 Earth years
# # Venus: orbital period 0.61519726 Earth years
# # Mars: orbital period 1.8808158 Earth years
# # Jupiter: orbital period 11.862615 Earth years
# # Saturn: orbital period 29.447498 Earth years
# # Uranus: orbital period 84.016846 Earth years
# # Neptune: orbital period 164.79132 Earth years
# # So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

# def seconds_alive(year,month,day):
#     now=datetime.now()
#     birthdate=datetime(year,month,day,00,00,00)
#     diff=now-birthdate
#     total_seconds = int((diff.days*86400)+diff.seconds)
#     return total_seconds
    
# def orbital_age(seconds):
#     earth_age=seconds/31557600
#     orbital_dict ={"Earth":1,"Mercury":0.2408467,"Venus":0.61519726,"Mars":1.8808158,"Jupiter":11.862615,"Saturn":29.447498,"Uranus":84.016846,"Neptune":164.79132}
#     for k,v in orbital_dict.items():
#         print(f"You are {round(earth_age*v,3)} years old on {k}")

# orbital_age(1000000)
# orbital_age(seconds_alive(1981,1,22))

# Exercise 6 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.



faker = Faker()
users=[]
i=0
while i<7:
    fake_dict={}
    fake_dict["name"]=faker.name()
    fake_dict["address"]=faker.address()
    # fake_dict["language_code"]=faker.language_code()
    users.append(fake_dict)
    i+=1
print(users)