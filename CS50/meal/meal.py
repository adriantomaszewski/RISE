def convert(time):
    inputvar = time
    hour = float(inputvar[0:inputvar.index(":")])
    minutes = float(inputvar[inputvar.index(":")+1:len(inputvar)])
    hour+=minutes/60
    return hour

def main():
    inputvar = input("Enter a time. ")
    hour = convert(inputvar)
    if(hour<=8 and hour>=7):
        print("breakfast time")
    if(hour<=13 and hour>=12):
        print("lunch time")
    if(hour<=19 and hour>=18):
        print("dinner time")
if __name__=='__main__':
    main()