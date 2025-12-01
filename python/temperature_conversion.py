def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


temperatures_in_celsius = [0, 25, 50, 100]
temperatures_in_fahrenheit = [convert_temperature(t) for t in
temperatures_in_celsius]
print(temperatures_in_fahrenheit)