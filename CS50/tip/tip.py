def dollars_to_float(d):
    d = d[1:d.index(".")]
    return float(d)

def percent_to_float(p):
    p = p[0:2]
    return float(p)/100


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    
if __name__=='__main__':
    main()