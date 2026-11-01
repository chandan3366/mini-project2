print("1. veg Sandwitch:- Rs.60")
print("2. Masala DOsa:- RS.80")
print("3. Chole Rice:- RS.90")
print("4. Tea:- Rs.20")
print("5. Paneer roll:- Rs.100")

subtotal = 0

while True:
    choice = int(input("choose item number: "))
    quantity = int(input("Enter quantity: "))

    if choice == 1:
        name = "Veg Sandwich"
        price = 60

    elif choice == 2:
        name = "Masala Dosa"
        price = 80

    elif choice == 3:
        name = "Chole Rice"
        price = 90

    elif choice == 4:
        name = "Paneer Roll"
        price = 100

    elif choice == 5:
        name = "tea"
        price = 20

    else:
        print("invalid item number")
        continue

    if quantity <= 0:
        print("invalid quantity")
        continue

    cost = price * quantity
    subtotal = subtotal + cost

    print(name,"x",quantity, "=", cost)


    again = input("add another item? (yes/no): ")

    if again == "no":
        break

print("subtotal:", subtotal)

if subtotal >= 500:
    discount = subtotal * 10 / 100

elif subtotal >= 250:
    discount = subtotal * 5 / 100

else:
    discount = 0

final_total = subtotal - discount

print("Discount:", discount)
print("Final Total:", final_total)
print("thank you") 