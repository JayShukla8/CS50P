
def main():
    str = input("Greeting: ")
    str = str.lower().strip()
    x = 0
    if(str.startswith("hello")):
        x = 0
    elif(str.startswith("h")):
        x = 20
    else:
        x = 100
    print(f"${x}")

main()
