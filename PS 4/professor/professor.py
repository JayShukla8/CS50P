import random


def main():
    level = get_level()
    cnt = 0
    score = 10
    while(cnt!=10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3
        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != (x+y):
                    print("EEE")
                    tries = tries-1
                    if(tries==0):
                        score = score - 1
                        print(f"{x} + {y} = {x+y}")
                        break
                    raise ValueError
                else:
                    break
            except ValueError:
                continue
        cnt = cnt+1
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    try:
        if level not in [1,2,3]:
            raise ValueError
        if level == 1:
            return random.randint(0,9)
        elif level == 2:
            return random.randint(10,99)
        else:
            return random.randint(100,999)
    except ValueError:
        sys.exit("Level Invalid")


if __name__ == "__main__":
    main()
