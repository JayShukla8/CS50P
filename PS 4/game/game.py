import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if(n>0):
                break
        except ValueError:
            continue
    random_n = random.randint(1,n)
    while True:
        try:
            g = int(input("Guess: "))
            if g>0:
                if g>random_n:
                    print("Too large!")
                elif g<random_n:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            continue

if __name__=="__main__":
    main()
