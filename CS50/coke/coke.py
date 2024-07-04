def main():
    numlefttopay = 50
    while(numlefttopay>0):
        inputvar = int(input("Enter a coin value. "))
        if (inputvar==25 or inputvar==10 or inputvar==5):
            numlefttopay-=inputvar
            print(f"Amount Due: {numlefttopay}")
        else:
            print(f"Amount Due: {numlefttopay}")
    print(f"Change Owed: {numlefttopay*-1}")
if __name__=='__main__':
    main()