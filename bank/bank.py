def main():
    inputvar = input("Enter a file name. ")
    inputvar = str(inputvar.lower())
    inputvar = inputvar.strip()
    if inputvar[0:5] == "hello":
        print("$0")
    elif inputvar[0] == "h":
        print("$20") 
    else:
        print("$100")  
if __name__=='__main__':
    main()