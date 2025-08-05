import math
print("==========================================")
print("\n========== Scientific Calculator =========\n")
print("==========================================")

def acceleration():
    v = float(input("Enter Final Velocity: "))
    u = float(input("Enter Initial Velocity: "))
    t = float(input("Enter Time: "))
    a = ((v - u) / t)
    print(f"Acceleration = {a:.2f} ")


def final_velocity():
    u = float(input("Enter Initial Velocity: "))
    a = float(input("Enter Acceleration: "))
    t = float(input("Enter Time: "))
    v = (u + a * t)
    print(f"Final Velocity = {v:.2f} m/s")

def displacement():
    u = float(input("Enter Initial Velocity: "))
    t = float(input("Enter Time: "))
    a = float(input("Enter Acceleration: "))
    s = (u * t) + 0.5 * (a) * (t * t)
    print(f"Displacement = {s:.2f} meters")

def force():
    m = float(input("Enter Mass: "))
    a = float(input("Enter Acceleration: "))
    f = (m * a)
    print(f"Force = {f:.2f} newton")

def kinetic_energy():
    m = float(input("Enter Mass: "))
    v = float(input("Enter Final Velocity: "))
    ke = (0.5 * m * v * v)
    print(f"Kinetic Enerfy = {ke:.2f}")

def potential_energy():
    m = float(input("Enter Mass: "))
    h = float(input("Enter Height: "))
    g = float(input("Enter Gravitational Acceleration: "))
    pe = (m * h * g)
    print(f"Potential Energy = {pe:.2f}") 

def work():
    f = float(input("Enter Force: "))
    s = float(input("Enter Displacement: "))
    w = (f * s)
    print(f"Work = {w:.2f} joules")

def power():
    w = float(input("Enter Work: "))
    t = float(input("Enter Time: "))
    Po = (w / t)
    print(f"Power = {Po:.2f}")

def momentum():
    m = float(input("Enter Mass: "))
    v = float(input("Enter Final Velocity: "))
    p = (m * v)
    print(f"Momentum = {p:.2f} m/s")

def frequency():
    T = float(input("Enter Time Period: "))
    fre = (1 / T)
    print(f"Frequency = {fre:.4f} Hz")

def sin_theta():
    theta_degree = float(input("\nEnter Angle In Degrees: "))
    radian_degree = math.radians(theta_degree)

    Sintheta = math.sin(radian_degree)

    print(f"Sin {theta_degree}° = {Sintheta:.2f}")


def cos_theta():
    theta_degree = float(input("\nEnter Angle In Degrees: "))
    theta_rad = math.radians(theta_degree)
    Costheta = math.cos(theta_rad)
    print(f"{theta_degree}° = {Costheta:.2f}")

def tan_theta():
    deg_value = float(input("Enter Angle In Degrees: "))
    rad_value = math.radians(deg_value)
    Tantheta = math.tan(rad_value)
    print(f"{deg_value}° = {Tantheta:.2f}")

def expression():
    u = float(input("Enter Initial Velocity: "))
    a = float(input("Enter Acceleration: "))
    s = float(input("Enter Displacement: "))
    ex = (u * u) + ( 2 * a * s)
    eq = math.sqrt(ex)
    print(f" v^2 = u^2 + 2as ==> {eq:.2f}")

def main():
    while True:
        print("\n=== Main Menu ===\n")
        print("1. Acceleration\n")
        print("2. Final Velocity\n")
        print("3. Displacement\n")
        print("4. Force\n")
        print("5. Kinetic Energy\n")
        print("6. Potential Energy\n")
        print("7. Work\n")
        print("8. Power\n")
        print("9. Momentum\n")
        print("10. Frequency\n")
        print("11. Sin(theta)\n")
        print("12. Cos(theta)\n")
        print("13. Tan(theta)\n")
        print("14. Expression (v^2 = u^2 + 2as)\n")
        print("0. Exit\n")

        choice = input("Enter Your Choice (0 to Exit): ")

        if(choice == '1'):
            acceleration()
        elif(choice == '2'):
            final_velocity()
        elif(choice == '3'):
            displacement()
        elif(choice == '4'):
            force()
        elif(choice == '5'):
            kinetic_energy()
        elif(choice == '6'):
            potential_energy()
        elif(choice == '7'):
            work()
        elif(choice == '8'):
            power()
        elif(choice == '9'):
            momentum()
        elif(choice == '10'):
            frequency()
        elif(choice == '11'):
            sin_theta()
        elif(choice == '12'):
            cos_theta() 
        elif(choice == '13'):
            tan_theta()
        elif(choice == '14'):
            expression()                   
        elif(choice == '0'):
            print("\nExiting.... Thankyou!")
            break
        else:
            print("InvLid Option. Try Again!\n")  

if __name__ == "__main__":
    main()                          
