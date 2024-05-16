import datetime as date

def calculateAge(birthDate): 
    """"
    Arguments
    birthDate--------- (users birthdate to be inputed in the proper format)
    variables---- today (today's date gotten from datetime module)
    
    Returns:
    age --- returns the calculated age of the user
    """
    
    #get today's date
    today = date.datetime.today() 
    #variable age :users's age returned
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age    

def getBirthDate():
    """""
    returns: --- birthdate(only if a valid date is entered)
    """
    while True:
        #user enters birthdate in a particular format
        birthDate = input("Please enter your birthdate in the following format (dd/mm/yyyy)\n>>> ")
        try:
            #checks the format entered by the user against the specified in the code 
            birthDate = date.datetime.strptime(birthDate, "%d/%m/%Y").date()
            break
            #throw an error if otherwise
        except ValueError:
            print("Invalid date format. Please enter your birthdate in the format (dd/mm/yyyy)")

    return birthDate

def main():
    """
    Arguments: 
    Returns
    Variables
    """
    birthDate = getBirthDate()
    print("Your birthday is on " + birthDate.strftime("%d") + " of " + birthDate.strftime("%B, %Y"))

    # print the age 
    print("You are", calculateAge(birthDate), "years of age")

if __name__ == "__main__":
    main()
