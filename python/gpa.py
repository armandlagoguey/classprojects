try:
    gpa = float(input("Enter your GPA :"))
except ValueError:
    print("Please enter a valid GPA")
try:
    communityservice = int(input("Do you do any community service ? (1=yes, 2=no)"))
except ValueError:
    print("Please enter only 1 or 2")
try:
    sport = int(input("Do you do sports ? (1=yes, 2=no)"))
except ValueError:
    print("Please enter only 1 or 2")

if gpa >= 3.5:
    if communityservice == 1:
        print("You are eligible for a full scholarship")
    else:
        print("You are eligible for a partial scholarship")
    if 3.0 <= gpa <= 3.49:
        if sport==1:
            print("You are eligible to a sports scholarship")
        else:
            print("You are not eligible to a scholarship")
else:
    print("You are not eligible to a scholarship")
