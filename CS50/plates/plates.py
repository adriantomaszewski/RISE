def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def thirdisfine(s):
    count = 0
    for i, char in enumerate(s):
        if char=="0" and count == 0:
            return False
        elif char.isnumeric():
            count+=1
        if not (char.isalpha() or char.isnumeric()):
            return False
        if char.isnumeric():
            if i==len(s)-1 or s[i+1].isnumeric():
                return True
            else:
                return False
    return True
        

def is_valid(s):
    if len(s)<=2:
        return False
    if(s[0].isalpha() and s[1].isalpha() and len(s)>=2 and len(s)<=6 and thirdisfine(s)):
        return True
    else:
        return False


main()
