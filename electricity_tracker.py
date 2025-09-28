print("==============================================")
print("           ELECTRICITY CALCULATOR")
print("==============================================")


def energy_from_power(power_watt, hours, quantity=1, duty=1.0):
    return (power_watt * hours * quantity * duty) / 1000
# Per-use appliances (energy per use in kWh, number of uses)
def energy_from_use(energy_per_use_kwh, uses_perday, quantity=1):
    return (energy_per_use_kwh * uses_perday * quantity)


def energy_from_fixed(energy_per_day, quantity=1):
    return energy_per_day * quantity

def energy_from_minutes(power_watt, minutes_per_use, uses_per_day, quantity=1, duty=1.0):
    """
    If you prefer minutes for an appliance (e.g., microwave):
    kWh = (W * (minutes/60) * uses * qty * duty) / 1000
    """
    hours_per_use = minutes_per_use / 60.0
    return (power_watt * hours_per_use * uses_per_day * quantity * duty) / 1000


def ceiling_fan():
    
    que =  int(input("Enter Quantity OF Fans: "))
    watt = int(input("Enter Wattage Of Each Fan: "))
    hour = float(input("Enter Fan Usage Per Day: "))
     
    kwh = energy_from_power(watt, hour, que)
    print(f"Fans: {kwh:.3f} kWh/day")
    return kwh

def led_bulb():
    que =  int(input("Enter Quantity OF Bulb: "))
    watt = int(input("Enter Wattage Of Each Bulb: "))
    hour = float(input("Enter Bulb Usage Per Day: "))

    kwh = energy_from_power(watt, hour, que)
    print(f"Led Bulb: {kwh:.3f} kWh/day")
    return kwh

def fridge():
    que =  int(input("Enter Quantity OF Fridge: "))
    watt = int(input("Enter Wattage Of Each Fridge [e.g, 150 watt]: "))
    hour = float(input("Enter Fridge Usage Per Day: "))
    duty = input("Duty cycle (0-1) [press Enter for default 0.4]: ").strip()
    duty = float(duty) if duty else 0.4
    kwh = energy_from_power(watt, hour, que, duty)
    print(f"Fridge: {kwh:.3f} kWh/day (duty = {duty})")
    return kwh

def iron():
    que =  int(input("Enter Quantity OF Iron: "))
    watt = int(input("Enter Wattage Of Each Iron [e.g, 1000 watt]: "))
    hour = float(input("Enter Fridge Usage Per Day: "))
    duty = input("Duty cycle (0-1) [press Enter for default 0.5]: ").strip()
    duty = float(duty) if duty else 0.5
    kwh = energy_from_power(watt, hour, que, duty)
    print(f"Iron: {kwh:.3f} kWh/day (duty = {duty})")
    return kwh

def washing_machine():
    que =  int(input("Enter Numbers Of Washing Machine: "))
    loads = int(input("Load Per Day Per Machine: "))
    default = 0.5
    avg_kwh = input(f"Average kWh per load [press Enter for default {default}]: ").strip()
    avg_kwh = float(avg_kwh) if avg_kwh else default

    kwh = energy_from_use(avg_kwh, loads, que)
    print(f"Washing Machine: {kwh:.3f} kWh/day")
    return kwh

def microwave_oven():
    print("Microwave Input Opton:")
    print("1) Enter Minute Per Use And Rated Watt (W)")
    print("2) Enter kWh Per Use Directly")
    choice = input("Enter Your Choice (1-2): ")
    if choice == '1':
        que = int(input("Enter Quantity Of Microwave: "))
        watt = float(input("Enter Rated Watt (w) [e.g, 1500]: "))
        uses = float(input("Enter Uses Per Day: "))
        minute = float(input("Enter Minutes Per Use: "))
        duty = input("Duty cycle (0-1) [press Enter for default 1.0]: ").strip()
        duty = float(duty) if duty else 1.0

        kwh = energy_from_minutes(watt, minute, uses, que, duty)
    else:
        que = int(input("Enter Quantity Of Microwave: "))    
        kwh_per_use = float(input("kWh per use (e.g., 0.02): "))
        uses = float(input("Enter Uses Per Day: "))

        kwh = energy_from_use(kwh_per_use, uses, que)
    print(f"Microwave: {kwh:.3f} kWh/day")
    return kwh    

def air_conditioner():
    que =  int(input("Enter Quantity OF AC: "))
    watt = int(input("Enter Wattage Of Each Ac [e.g, 1200-2500]: "))
    hour = float(input("Hours Of Usage Per Day: "))
    duty = input("Duty cycle (0-1) [press Enter for default 0.6]: ").strip()
    duty = float(duty) if duty else 0.6

    kwh = energy_from_power(watt, hour, que, duty)
    print(f"Air Conditioner: {kwh:.3f} kWh/day (duty = {duty})")
    return kwh

def calculate_bill_slap(units):
    
    # Slabs:
    #   1-100  -> 22.44
    #   101-200-> 28.91
    #   201-300-> 33.10
    #   301-400-> 37.99
    #   401-500-> 41.20
    #   501-600-> 41.62
    #   >600   -> 41.62  (continue last slab; change if your DISCO differs)
    
    u = float(units)
    if u<=0:
        return 0.0
    bill = 0.0

    tiers = [
        (100, 22.44),
        (100, 28.91),
        (100, 33.10),
        (100, 37.99),
        (100, 41.20),
        (100, 41.62),
    ]

    for cap, rate in tiers:
        take = min(u, cap)
        bill += take * rate
        u-= take
        if u<=0:
            return bill
    bill += u * 41.62
    return bill    

def calculate_price():
    try:
        total_units = float(input("Enter Total Units (kwh): ")) 
        amount = calculate_bill_slap(total_units)
        print(f"Total Bill: Rs {amount:.2f}")
    except ValueError:
        print("Invalid Number. Please Try Again!")       
 
     
    
def main():
    while True:
        print("\n===== Main Menu =====\n")
        print("1. Celing Fan\n")
        print("2. Led Bulb\n")
        print("3. Fridge\n")
        print("4. Iron\n")
        print("5. Washing Machine\n")
        print("6. Microwave Oven\n")
        print("7. Air Conditioner\n")
        print("8. Calculate Units\n")
        print("9. Exit\n")

        choice = input("Enter Your Choice (1-8): ")

        if choice == '1':
            ceiling_fan()
        elif choice == '2':
            led_bulb()
        elif choice == '3':
            fridge()
        elif choice == '4':
            iron()
        elif choice == '5':
            washing_machine()
        elif choice == '6':
            microwave_oven()
        elif choice == '7':
            air_conditioner()
        elif choice == '8':
            calculate_price()    
        elif choice == '9':
            print("Exiting...Thankyou")
            break
        else:
            print("Invalid Choice. please Try Again!\n")

if __name__ == "__main__":
    main()



    






