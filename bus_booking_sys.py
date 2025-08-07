buses = {
    "1": {
        "route": "Karachi to Islamabad",
        "departure": "9:00 Am",
        "price": 5000,
        "seats": 20
    },
    "2": {
        "route": "Karachi to lahore",
        "departure": "8:00 Pm",
        "price": 5500,
        "seats": 20
    },
    "3": {
        "route": "Islamabad to Kashmir",
        "departure": "8:00 Am",
        "price": 8000,
        "seats": 15
    }
}

print("=== 🚌 Welcome To Bingo Bus App 🚌 ===\n")
print("Avaliable Routes:\n")

for bus_id, info in buses.items():
    print(f"{bus_id}. Route: {info["route"]} | Departure: {info["departure"]} |"
          f" Seats Available: {info["seats"]} | Fair: Rs {info["price"]} ")

bus_choice = input("\n🚌 Enter The Bus Number You Want To Book: ")

if bus_choice in buses:
    passenger_name = input("👤 Enter Your Name: ")
    date = input("Enter date: ")
    try:
        seats_requested = int(input("💺 Enter Number Of Seats You Want: "))
        available = buses[bus_choice]["seats"]
        if seats_requested <=0:
            print("❌ Invalid Seat Number!")
        elif seats_requested > available:
            print("❌ Not enough seats available!")
        else:
            total_fair = seats_requested * buses[bus_choice]["price"]
            buses[bus_choice]["seats"] -= seats_requested

            print("\n🎟️  Booking Confirmed!")
            print(f"Passenger Name: {passenger_name}")
            print(f"Date: {date}")
            print(f"Route: {buses[bus_choice]["route"]}")
            print(f"Departire Time: {buses[bus_choice]["departure"]}")
            print(f"Seats Booked: {seats_requested}")
            print(f"Fair: {total_fair}")
            
            with open("booking.txt", "a") as f:
                f.write(f"Name: {passenger_name}, Date: {date,}, "
                        f"Departure: {buses[bus_choice]["departure"]}, Total Rs: {total_fair}, "
                        f"Seats: {seats_requested}, Route: {buses[bus_choice]["route"]}")
                print("📝 Booking Saved to booking.txt")
    except ValueError:
        print("❌ Enter a valid number of seats!")
else:
    print("❌ Invalid bus number. Please try again.")        





