
def main():
    d = {}
    while True:
        try:
            str = input()
            str = str.upper()
            if(str in d):
                d[str] = d[str]+1
            else:
                d[str] = 1
        except EOFError:
            break
    for item in sorted(d.keys()):
        print(d[item], item)


if __name__=="__main__":
    main()
