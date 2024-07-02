def main():
    string = "Hello :)\nGoodbye :(\nHello :) Goodbye :(\n"
    string = convert(string)
    print(string)
def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string
if __name__=='__main__':
    main()