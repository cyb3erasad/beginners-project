users = {
    "asad": {"pin": "2007", "balance": 10000},
    "umer": {"pin": "7015", "balance": 10000},
    "ali": {"pin": "1611", "balance": 5000},
    "irfan": {"pin": "1085", "balance": 8000}
}
print("=== 🏦 Welcome TO Bingo Bank ===\n")
username = input("👤 Enter Your Username: ").lower()

if username in users:
    enter_pin = input("🔐 Enter Your 4-Digit Pin: ")

    if enter_pin == users[username]["pin"]:
        print(f"\n Welcome {username.capitalize()}! Login Successfully ✅\n")

        while True:
          print("🏧 ATM Menu ")
          print("1. 💰 Check Balance")
          print("2. 💳 Withdraw Money")
          print("3. 🏦 Deposit Money")
          print("4. 🚪 Exit")

          choice = input("Enter Your Choice (1-4): ")

          if choice == "1":
             print(f"💵 Your Current Balance is: Rs {users[username]["balance"]}\n")

          elif choice == "2":
             try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <=0:
                   print("❌ Invalid amount!")
                elif amount > users[username]["balance"]:
                   print("❌ Insufficient Funds!")
                else:
                   users[username]["balance"] -= amount
                   print(f"✅ Withdrawn Rs {amount}. New balance: Rs {users[username]['balance']}\n")
             except ValueError:
                print("\n ❌ Please Enter a Valid Number.\n")

          elif choice == "3":
             try:
                amount = int(input("Enter amount to deposit: "))
                if amount <=0:
                   print("❌ Invalid amount!")
                else:
                   users[username]["balance"] += amount
                   print(f"✅ Deposited Rs{amount}. New balance is {users[username]["balance"]}\n")
             except ValueError:
                print("\n ❌ Please Enter A Valid Number.\n")

          elif choice == "4":
             print(f"🚪 ThankYou, {username.capitalize()}. Goodbye!") 
             break  
          else:
             print("❌ Invalid Option Please Choose (1-4)")

    else:
       print("❌ Invalid PinCode. Access Denied")

else:
   print("❌ User not found. Please check your username")





       
