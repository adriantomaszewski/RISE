fruits = [{"Name": "Apple", "Calories": "130"},
        {"Name": "Avocado", "Calories": "50"},
        {"Name": "Banana", "Calories": "110"},
        {"Name": "Cantaloupe", "Calories": "50"},
        {"Name": "Grapefruit", "Calories": "60"},
        {"Name": "Grapes", "Calories": "90"},
        {"Name": "Honeydew", "Calories": "50"},
        {"Name": "Kiwifruit", "Calories": "90"},
        {"Name": "Lemon", "Calories": "15"},
        {"Name": "Lime", "Calories": "20"},
        {"Name": "Nectarine", "Calories": "60"},
        {"Name": "Orange", "Calories": "80"},
        {"Name": "Peach", "Calories": "60"},
        {"Name": "Pear", "Calories": "100"},
        {"Name": "Pineapple", "Calories": "50"},
        {"Name": "Plums", "Calories": "70"},
        {"Name": "Strawberries", "Calories": "50"},
        {"Name": "Sweet", "Calories": "100"},
        {"Name": "Tangerine", "Calories": "50"},
        {"Name": "Watermelon", "Calories": "80"}]
def main():
    plate = input("Item: ")
    for fruit in fruits:
        vallist = list(fruit.values())
        if vallist[0]==plate:
            print(f"Calories: {fruit.get("Calories")}")
if __name__=='__main__':
    main()