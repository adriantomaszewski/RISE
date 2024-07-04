def main():
    sensory = [0,0,1,0,0]*6
    motor = []
    conweight = 4
    effconweight = 4
    habrate = float(input("Enter a habrate: "))

    for sense in sensory:
        motor.append(calculateout(sense, effconweight))
        if(calculateout(sense, effconweight) != 0):
            effconweight = (1-habrate)*effconweight
    print(motor)
        
def calculateout(x,y):
    return x*y

if __name__=="__main__":
    main()