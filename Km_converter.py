
print("******Km_converter******")
user_km = float(input("Enter the Kilometer to be converted: "))


def km_converter(Km):
    converted_miles = 0.621 * user_km
    return print(converted_miles)

km_converter(user_km)
repeat_or_not = input("Do you want to continue y/n? ")
while not repeat_or_not == 'n':
    print("******Km_converter******")
    user_km = int(input("Enter the Kilometer to be converted: "))
    km_converter(user_km)
    repeat_or_not = input("Do you want to continue y/n? ")

