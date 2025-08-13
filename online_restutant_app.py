# Resturant online app

menu = {
   "1": 400,
   "2": 250,
   "3": 500,
   "4": 2000,
   "5": 900,
   "6": 350,
   "7": 100,
   "8": 300,
   "9": 800,
   "10": 200,
   "11": 300,
   "12": 1000
}

# order_list = []
pay = [" 💵 Cash ", " 💳 Card "]

print("=== 🍽️  Welcome to Bingo Express 🍽️  ===\nMenu:")
print("1.Zinger burger: 400\n2.Kabab roll: 250\n3.Beef burger: 500\n4.Arabian rench Pizza(large): 2000\n5.Arabian rench Pizza(small): 900\n6.Crunchy burger: 350\n7.Coldrink: 100\n8.Cofee: 300\n9.Double patty burger: 800\n10.Fries: 200\n11.Pizza fries: 300\n12.White sauce pasta: 1000\n")


total_order = 0

while True:
    item = input("Please Enter The Item Number You Want To Order: ")
    if item in menu:
       total_order +=menu[item]
       print("Your Item Has Been Added To Your Cart  🛒!")
    else:
        print("Sorry This Item Is Not Available Right Now")  

    another_order = input("Do You Want TO Add Another Item To Your Cart? (yes/no) ")
    if another_order.lower() !='yes':
        break 

# print(f"\nTotal Bill: {total_order} Rs")
# Show order Summary

print("\n=== Order Summary ===\n")
print(f"\nTotal Bill: Rs {total_order} 💵\n")
# print(f" You ordered {item}  = {total_order} ")
# print(f"\nTotal Bill: {total_order} Rs")

def address():
   print("Please Enter Your House Address 🏠: ")
   house_no = input("Enter Your House No: ")
   area = input("Enter Your Area: ")
   city = input("Enter Your City: ")
   print("Your Address is: ", house_no, area, city)

address()

print(pay)
payment = input("Enter Your Payment Method: ")

if payment == "Card":
    while True:
     cardno = input("Enter Your Card Number With Space: ").split()
    
     if len(cardno) == 9 and all(item.lstrip('-').isdigit() for item in cardno):
        numbers = [int(i) for i in cardno]
        print("Payment Successfull!!")
        print("Your Card Number Is:", numbers)
        break
     else:
      print("Invalid input! Please enter exactly 9 integers.")

    
   
elif payment == "Cash":
    print("Order Packed!!")
else:
    print("Sorry This Method Is Not Available Right Now")

print("✅ Order placed successfully! Thank you.")  
print("The rider will deliver your order as soon as possible 🛵 🚚 📦 ")  




