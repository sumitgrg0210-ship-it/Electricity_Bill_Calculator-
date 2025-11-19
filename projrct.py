# print("===== TEMPERATURE CONVERTER =====")

# def celsius_to_fahrenheit(c):
#     return (c * 9/5) + 32

# def celsius_to_kelvin(c):
#     return c + 273.15

# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5/9

# def kelvin_to_celsius(k):
#     return k - 273.15

# def fahrenheit_to_kelvin(f):
#     return (f - 32) * 5/9 + 273.15

# def kelvin_to_fahrenheit(k):
#     return (k - 273.15) * 9/5 + 32

# while True:
#     print("\nChoose Conversion:")
#     print("1. Celsius → Fahrenheit")
#     print("2. Celsius → Kelvin")
#     print("3. Fahrenheit → Celsius")
#     print("4. Fahrenheit → Kelvin")
#     print("5. Kelvin → Celsius")
#     print("6. Kelvin → Fahrenheit")
#     print("7. Exit")

#     choice = int(input("Enter your choice (1-7): "))

#     if choice == 7:
#         print("Exiting the converter... Thank you!")
#         break

#     temp = float(input("Enter temperature value: "))

#     if choice == 1:
#         print("Result:", celsius_to_fahrenheit(temp), "°F")
#     elif choice == 2:
#         print("Result:", celsius_to_kelvin(temp), "K")
#     elif choice == 3:
#         print("Result:", fahrenheit_to_celsius(temp), "°C")
#     elif choice == 4:
#         print("Result:", fahrenheit_to_kelvin(temp), "K")
#     elif choice == 5:
#         print("Result:", kelvin_to_celsius(temp), "°C")
#     elif choice == 6:
#         print("Result:", kelvin_to_fahrenheit(temp), "°F")
#     else:
#         print("Invalid choice! Try again.")










print("===== ELECTRICITY BILL CALCULATOR =====")

name = input("Enter Customer Name: ")
units = float(input("Enter total units consumed: "))

# Bill calculation based on slabs
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 12

# Adding fixed charge
fixed_charge = 50  
total_bill = bill + fixed_charge

print("\n===== BILL SUMMARY =====")
print(f"Customer Name : {name}")
print(f"Units Used    : {units}")
print(f"Energy Charge : ₹{bill:.2f}")
print(f"Fixed Charge  : ₹{fixed_charge}")
print("------------------------------")
print(f"Total Bill    : ₹{total_bill:.2f}")
print("===================================")
