def main():
    inputvar = input("Enter an expression. ")
    list = inputvar.split()
    if(list[1]=="+"):
       print(float(list[0])+float(list[2]))
    if(list[1]=="*"):
        print(float(list[0])*float(list[2]))
    if(list[1]=="-"):
        print(float(list[0])-float(list[2]))
    if(list[1]=="/"):
        print(float(list[0])/float(list[2]))
if __name__=='__main__':
    main()