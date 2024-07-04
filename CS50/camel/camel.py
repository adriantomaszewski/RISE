def convert(varname):
    returnvar = ""
    lastupperind=0
    for i, letter in enumerate(varname):
        if letter.isupper()==True:
            returnvar+=varname[lastupperind:i].lower()
            returnvar+="_"
            lastupperind=i
    returnvar+=varname[lastupperind:i+1].lower()
    lastupperind=i
    print(returnvar)

def main():
    inputvar = input("Enter a variable name. ")
    convert(inputvar)
if __name__=='__main__':
    main()