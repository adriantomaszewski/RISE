import math
def main():
    v = input("Input valence. ")
    ic = input("Input intracell conc. ")
    ec = input("Input extracell conc. ")
    print(nerst(int(v), int(ic), int(ec)))
def nerst(v, ic, ec):
    return (1000*8.314*298*math.log(ec/ic)/(v*96485.3))
if __name__=='__main__':
    main()