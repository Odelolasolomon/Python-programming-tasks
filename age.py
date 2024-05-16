import datetime as date

def calculateAge(birthDate): 
    today = date.datetime.today() 
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age 

birthDate = input("Please enter your birthdate on the following format (dd/mm/yyyy)\n>>> ")
birthDate = date.datetime.strptime(birthDate, "%d/%m/%Y").date()
print("Your birthday is on "+ birthDate.strftime("%d") + " of " + birthDate.strftime("%B, %Y"))

#lets print the age now
print("You are", calculateAge(birthDate), "years old")