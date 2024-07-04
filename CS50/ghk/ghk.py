import math
def main():
    v = 1
    icn = 15
    ecn = 145
    ick = 150
    eck = 4
    icc = 5
    ecc = 50
    print(nerst(int(v), int(icn), int(ecn), int(ick), int(eck), int(icc), int(ecc)))
def nerst(v, icn, ecn, ick, eck, icc, ecc):
    numerator = (ecn * 0.05 + eck * 1 + icc * 0.3)
    denominator = (icn * 0.05 + ick * 1 + ecc * 0.3)

    return (1000 * 298 * 8.314/96485.3 * math.log(numerator / denominator))
if __name__=='__main__':
    main()