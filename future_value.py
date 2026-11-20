def futuevalue (present_value, monthly_rate, months):
    return present_value * (1 + monthly_rate) ** months

def main():
    present_value = float(input("Enter the present value:"))
    months = int(input("enter the amount of months"))
    interest =  float(input("Enter the interest rate"))

    fv = futuevalue(present_value,interest,months)
    print("future value:", fv)
    main()