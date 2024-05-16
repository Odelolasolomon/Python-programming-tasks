from datetime import date 
dob= str(input('Please enter your DOB (YY-MM-DD):'))
date_of_birth= date.fromisoformat(dob)
print(date_of_birth)
