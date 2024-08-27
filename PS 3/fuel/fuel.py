
def fuel_is(x,y):
    ans = (x/y)*100
    ans = round(ans)
    if(0<=ans<=1):
        print("E")
    elif(99<=ans<=100):
        print("F")
    else:
        print(f"{ans}%")

def main():
    while True:
        try:
            str = input("Fraction: ")               #reprompts only when
            [x, y] = str.split('/')                  #x and y not integers,
            x = int(x)                               #x greater than y, or
            y = int(y)                               #y == 0
            if(x<=y):
                fuel_is(x,y)
                break
        except (ValueError, ZeroDivisionError):
            continue

if __name__=="__main__":
    main()
