def format_phone_number(phone_number):
    part1 = phone_number[:3]
    part2 = phone_number[3:6]
    part3 = phone_number[6:]
    return f"({part1}){part2}-{part3}"
print(format_phone_number("0732475684"))
print(format_phone_number("9874567329"))
print(format_phone_number("8325837489"))