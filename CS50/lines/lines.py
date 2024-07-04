import sys

count = 0
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].startswith(".py", -3) == False:
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
            for line in lines:
                if line == "\n" or line.strip()=="" or line.strip().startswith("#") == True:
                    continue
                else:
                    count += 1
            print(count)
        except FileNotFoundError:
            sys.exit("FileNotFoundError")