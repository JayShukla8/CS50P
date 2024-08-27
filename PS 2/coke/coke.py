
def main():
    due = 50
    coins = 0
    while(coins<50):
        while True:
            try:
                print(f"Amount Due: {due}")
                inp = int(input("Insert Coin: ")) # 5 5 50
                if (inp not in [5, 10, 25]):
                    continue
                else:
                    break
            except ValueError:
                continue
        coins = coins + inp # 5 10 60
        due = due - inp # 45 40 -10
        if due<0:
            due = 0 - due
    print(f"Change Owed: {due}")

if __name__ == "__main__":
    main()
