def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_without_dollar = d.replace("$","")
    #d_without_dollar_float = float(d_without_dollar)
    return float(d_without_dollar)

def percent_to_float(p):
    p_without_trailing  = p.replace("%","")
    string_with_leading_zero = (str(0) + "." + p_without_trailing)
    return float(string_with_leading_zero)

main()