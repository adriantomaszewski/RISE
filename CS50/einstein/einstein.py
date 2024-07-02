def main():
    inputmass = input('What is the desired mass input that you would like to convert? ')
    print(masstoJoules(int(inputmass)))
def masstoJoules(mass):
    return mass*300000000**2    
if __name__=='__main__':
    main()