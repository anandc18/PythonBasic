from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
print(new_year.day)
print(new_year.month)
print(new_year.year)
print(new_year.minute)
print(new_year.second)

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time_one:",time_one)


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born

    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
