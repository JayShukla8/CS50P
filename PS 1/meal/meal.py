
def convert(time):
    [hours, mins] = time.split(":")
    ans = float(hours) + float(mins)/60
    return ans

def main():
    time = input("What time is it? ")
    if(len(time) <= 5):
        ans = convert(time)
        if(7.00 <= ans <= 8.00):
            print("breakfast time")
        elif(12.00 <= ans <= 13.00):
            print("lunch time")
        elif(18.00 <= ans <= 19.00):
            print("dinner time")
        else:
            print("")
    else:
        hours, y = time.split(":")
        mins, z = y.split(" ")
        t = float(hours) + float(mins)/60
        if((7.00 <= t <= 8.00) and (z=="a.m.")):
            print("breakfast time")
        elif(((t==12.00) or (0.00 <= t <= 1.00)) and (z=="p.m.")):
            print("lunch time")
        elif((6.00 <= t <= 7.00) and (z=="p.m.")):
            print("dinner time")
        else:
            print("")

if __name__ == "__main__":
    main()
