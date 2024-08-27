
def main():
    d = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.00
    while True:
        try:
            str = input("Item: ")
            str = str.title()
            if(str in d):
                total = total + d[str]
                print(f"Total: ${total:.2f}")
        except KeyError:
            continue
        except EOFError:
            break
    print("\n")

if __name__=="__main__":
    main()
