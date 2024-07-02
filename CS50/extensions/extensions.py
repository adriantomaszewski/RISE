def main():
    inputvar = input("Enter a file name. ")
    inputvar = str(inputvar.lower())
    inputvar = inputvar.strip()
    while(inputvar.count(".")>1):
        inputvar=inputvar[inputvar.index(".")+1:len(inputvar)]
    if ("." in inputvar):
        if (inputvar[inputvar.index(".")+1:len(inputvar)]=="jpg"):
            print("image/jpeg")
        elif (inputvar[inputvar.index(".")+1:len(inputvar)]=="gif" or inputvar[inputvar.index(".")+1:len(inputvar)]=="jpeg" or inputvar[inputvar.index(".")+1:len(inputvar)]=="png"):
            print("image/"+inputvar[inputvar.index(".")+1:len(inputvar)])
        elif (inputvar[inputvar.index(".")+1:len(inputvar)]=="pdf" or inputvar[inputvar.index(".")+1:len(inputvar)]=="zip"):
            print("application/"+inputvar[inputvar.index(".")+1:len(inputvar)])
        elif (inputvar[inputvar.index(".")+1:len(inputvar)]=="txt"):
            print("text/"+inputvar[0:inputvar.index(".")])
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")
if __name__=='__main__':
    main()