try:
    height = input("enter your height in centimenters: ")
    weight = input("enter your weight in kilograms: ")
    bmi= float(weight) / (float(height)/100) ** 2
    match bmi:
        case bmi if bmi <= 16:
            print("You are severely underweight.")
        case bmi if 16 < bmi <= 18.5:
            print("You are underweight.")
        case bmi if 18.5 < bmi <= 25:
            print("You have a healthy weight.")
        case bmi if 25 < bmi <= 30:
            print("You are overweight.")
        case _:
            print("You are severely overweight.")
except ValueError:
    print("Please enter valid numbers for height and weight.")
except ZeroDivisionError:
    print("Height cannot be zero.")
