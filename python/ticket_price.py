try:
    age=int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")  
is_student=input("Are you a student? (yes/no): ")
if is_student != "yes" and is_student != "no":
    print("Invalid input. Please enter 'yes' or 'no'.")
else:
    if 0 <= age <= 12:
        ticket_price = 5
    elif 13 <= age <= 17:
        ticket_price = 7
    elif 18 <= age <= 64:
        ticket_price = 12
    else:
        ticket_price = 8
    if is_student == "yes":
        ticket_price = ticket_price-2 
    print(f"Your ticket price is: ${ticket_price}")
