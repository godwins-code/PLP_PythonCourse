import datetime

name = input("NAME: ")
year_of_birth = int(input("YEAR OF BIRTH: "))
current_year = datetime.datetime.now().year
age = (current_year) - (year_of_birth)

print(f'{name}', age, 'years old')
