def main():
    mass = int(input("Enter the mass as int in [kg]: ")) # [kg]
    result_enegy = calculate_general_relativity(mass)
    print("E", result_enegy)

def calculate_general_relativity(mass):
    c = 300000000 # m/s
    return mass*(c**2) # Joules

main()