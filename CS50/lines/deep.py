def main():
    inputvar = input("Enter something. ")
    inputvar = inputvar.lower()
    if ("42" in inputvar or inputvar == "forty-two" or inputvar == "forty two"):
        print("Yes")
    else:
        print("No")
if __name__=='__main__':
    main()