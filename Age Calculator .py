from datetime import date
year=int(input('Enter year birth: '))
month=int(input('Enter month birth: '))
day=int(input('Enter day birth: '))

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year-((today.month, today.day)<(birthDate.month, birthDate.day))
    return age
     
# Driver code
print(calculateAge(date(year,month,day)), "years")



