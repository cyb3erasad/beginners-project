import datetime
import json
import os

nurses = []
BOOKING_FILE = "bookings.json"
NURSE_FILE = "nurses.json"

def load_data():
    global booking_list
    if os.path.exists(BOOKING_FILE):
        with open(BOOKING_FILE, "r") as f:
            booking_list = json.load(f)
    else:
        booking_list = []   

def save_data():
    with open(BOOKING_FILE, "w") as f:
        json.dump(booking_list, f, indent=4) 

def load_nurses():
    global nurses
    if os.path.exists(NURSE_FILE):
        with open(NURSE_FILE, "r") as f:
            nurses = json.load(f)
            for nurse in nurses:
                nurse["available"] = bool(nurse.get("available", True))
    else:
        nurses = [
            {"id": 2001, "name": " Nurse Chloe", "Speciality": "ICU", "charges": 500, "available": True, },
            {"id": 2002, "name": " Nurse Debbie", "Speciality": "Pediatrics", "charges": 600, "available": True, },
            {"id": 2003, "name": " Nurse Ollie", "Speciality": "Surgery", "charges": 1000, "available": True, },
            {"id": 2004, "name": " Nurse Bella", "Speciality": "Maternity", "charges": 400, "available": True, },
            {"id": 2005, "name": " Nurse Kelly", "Speciality": "Psheotherapist", "charges": 700, "available": True, }
        ]          
        save_nurses()

def save_nurses():
    with open(NURSE_FILE, "w") as f:
        json.dump(nurses, f, indent=4) 


print("==============================================================================")
print("             🏥     Nurse        Booking        System     🏥")
print("==============================================================================")

# nurses = [
#     {"id": 2001, "name": " Nurse Chloe", "Speciality": "ICU", "charges": 500, "available": True, },
#     {"id": 2002, "name": " Nurse Debbie", "Speciality": "Pediatrics", "charges": 600, "available": True, },
#     {"id": 2003, "name": " Nurse Ollie", "Speciality": "Surgery", "charges": 1000, "available": True, },
#     {"id": 2004, "name": " Nurse Bella", "Speciality": "Maternity", "charges": 400, "available": True, },
#     {"id": 2005, "name": " Nurse Kelly", "Speciality": "Psheotherapist", "charges": 700, "available": True, },          
# ]

booking_list = []

def view_all_nurses():
    print("\n========== View All Nurses ==========\n")
    for nurse in nurses:
        print(f"ID: {nurse['id']} | Name: {nurse['name']} | Speciality: {nurse['Speciality']} | Charges: $ {nurse['charges']} | Available:  {'Yes' if nurse['available'] else 'No'}\n")

def view_available_nurses():
    print("\n========== View Available Nurses ==========\n")
    for nurse in nurses:
        if nurse['available']:
            print(f"ID: {nurse['id']} | Name: {nurse['name']} | Speciality: {nurse['Speciality']} | Charges: $ {nurse['charges']} | \n")

def book_nurse():
    view_available_nurses()
    try:
        nurse_id = int(input("\nEnter Nurse Id To Book: "))
        for nurse in nurses:
            if nurse['id'] == nurse_id and nurse['available']:
                patient_name = input("Enter Your Name: ")
                date = input("Enter Booking Date (DD-MM-YYYY): ")
                contact_num = int(input("Enter Your Contact Number: "))
                hours = int(input("Enter Booking Hours: "))
                nurse['available'] = False
                booking = {
                    "nurse": nurse,
                    "Patient": patient_name,
                    "Date": date,
                    "Contact": contact_num,
                    "Charges": nurse['charges'],
                    "Paid": 0.0,
                    "Due": float(nurse['charges']),
                    "Hour": hours,
                    "Payments": []
                }
                booking["Paid"] = booking.get("Paid", booking.get("paid", 0))
                booking["Due"] = booking.get("Due", booking.get("due", booking["Charges"]))
                if "paid" in booking: booking.pop("paid")
                if "due" in booking: booking.pop("due")

                booking_list.append(booking)
                save_data()
                save_nurses()
                print(f"\n{nurse['name']} Successfully Book For Patient: {patient_name} For {hours} Hours On Date: {date} \n")
                return
        print(" ❌ Nurse Not Available Or Invalid Nurse ID.\n")        
    except ValueError:
        print(" ❌ Invalid Input. Please Enter Numeric ID.\n")

def generate_bill():
    if not booking_list:
        print("\nNo Bookings Found!\n")
        return
    
    print("\n========== 🧾💳     Generate Bill     🧾💳 ==========\n")
    for i, b in enumerate(booking_list, start=1):
        charges = float(b.get('charges', b.get('Charges', 0)))
        paid    = float(b.get('paid',    b.get('Paid',    0)))
        due     = float(b.get('due',     charges - paid))

        print(f"\n Booking # {i}")
        print(f"Patient Name   : {b.get('Patient','Unknown')}")
        print(f"Contact Number : {b.get('Contact','Unknown')}")
        print(f"Date           : {b.get('Date','Unknown')}")
        print(f"Nurse Name     : {b.get('nurse',{}).get('name','Unknown')}")
        print(f"Speciality     : {b.get('nurse',{}).get('Speciality', 'Unknown')}")
        print(f"Charges        : $ {charges:.2f}")
        print(f"Hours          : {b.get('Hour')}")
        print(f"Paid           : $ {paid:.2f}")
        print(f"Due            : $ {due:.2f}")
        print(f"Status         : {'Paid' if due <= 0 else f'Due: ${due:.2f}'}\n")

        for p in b.get('payments', b.get('Payments', [])):
            print(f"  - {p.get('date','?')} | $ {float(p.get('amount',0)):.2f}\n")

def add_nurse():

    print("\n========== 👨‍⚕️🩺     Add Nurse     👨‍⚕️🩺 ==========\n")
    name = input("Enter Nurse Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    speciality = input("Enter  Nurse Speciality: ").strip()
    if not speciality:
        print("Speciality cannot be empty!")
        return
    try:
        charges = int(input("Enter Nurse Charges (numeric): ").strip())
        if charges <0:
            print("Charges must be a positive number!")
            return
    except ValueError:
        print("Invalid Charges. please enter a valid charges!")
        return
    avail_in = input("Nurse is available or not (Y,N) [Y]: ").lower()
    availablle = False if avail_in == 'n' else True

    new_id = (max((n ['id'] for n in nurses), default=2000)+1)

    new_nurses = {
        "name": name if name.lower().startswith("nurse") else f"Nurse {name}",
        "id": new_id,
        "Speciality": speciality,
        "charges": charges,
        "available": availablle
    }      
    nurses.append(new_nurses)
    print(f"\n Nurse Added: ID {new_id} | Name {new_nurses['name']} | {speciality} | $ {charges} | "
          f"{'Available' if availablle else not 'Available'}\n")
    
def update_payment():

    if  not booking_list: 
        print("\nNot Bookings Found. Book A Nurse First\n")
        return
    print("\n========== Update Payments ==========\n")
    try:
        nurse_id = int(input("Enter Nurse ID For Payment: ").strip())
    except ValueError:
        print("Invalid ID. Please enter valid ID\n")
        return

    related = [(idx +1, b) for idx, b in  enumerate(booking_list) if b["nurse"]["id"] == nurse_id]
    if not related:
        print(" ❌ Not Bookings Found!\n")
        return
    
    print("\nMatching Bookings\n")
    for show_idx, b in related:
        status = "Paid" if b["Due"] <=0 else f"Due: $ {b['Due']:.2f}"
        print(f"{show_idx}. Patient: {b['Patient']} | Date: {b['Date']} | Hours: {b['Hour']} | Nurse: {b['nurse']['name']} | {status} ")

        
    try:
        pick = int(input("\nSelect a booking number from the list above: ").strip())
    except ValueError:
        print("Invalid Number!\n")
        return
    if pick < 1 or pick > len(booking_list):
        print("Invalid Booking Number!\n")
        return
    
    booking = booking_list[pick -1]

    if booking["nurse"]["id"] != nurse_id:
        print("\nSelected Booking Does Not Match The Nurse ID.\n")
        return
    
    try:
        amount = float(input(f"Enter amount to pay (Due $ {booking['Due']:.2f}): ").strip())
    except ValueError:
        print("Invalid Amount!\n")
        return
    if amount < 0:
        print("Amount Must Be Positive!")
        return
    if amount >booking["Due"]:
        print(f"You entered more than due amount. Capping Amount is {booking['Due']:.2f}.")
        amount = booking["Due"]
        
    booking["Paid"] =  round(booking["Paid"] + amount, 2)
    booking["Due"] = round(booking["Due"] - amount, 2)
    booking["Payments"].append({
        "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        "amount": round(amount, 2)
    })   
    save_data()
    save_nurses()

    print("\n Payment Recorded\n")
    print(f"   Patient: {booking['Patient']}"
          f"   Nurse  : {booking['nurse']['name']}"
          f"   Paid   : ${booking['Paid']:.2f}"
          f"   Due    : ${booking['Due']:.2f}"
    ) 

    

def main():
    load_nurses()
    load_data()
    while True:
       print("1. View All Nurses 👨‍⚕️")
       print("2. View Available Nurses 👨‍⚕️")
       print("3. Book A Nurse 🗓️ 👩‍⚕️")
       print("4. generate Bill 🧾💳")
       print("5. Add Nurse 👨‍⚕️🩺")
       print("6. Update Payment 🧾💵")
       print("7. Exit ⬅️ 🚪\n")

       choice = (input("Enter Your Choice (1-6): "))

       if choice == '1':
           view_all_nurses()
       elif choice == '2':
           view_available_nurses()
       elif choice == '3':
           book_nurse()
       elif choice == '4':
           generate_bill()
       elif choice == '5':
              add_nurse()
       elif choice == '6':
           update_payment()
       elif choice == '7':
           save_data()
           save_nurses()
           print("👋 Exiting.... Thankyou ")
           break   
       else:
           print("\nInvalid Option. Try Again!\n")

if __name__ == "__main__":
    main()










