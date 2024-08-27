import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1]) as file:
                count = 0
                for line in file:
                    line = line.lstrip()
                    if line.startswith("#") or not line.strip():
                        continue
                    else:
                        count = count+1
        except FileNotFoundError:
            sys.exit("File does not exist")
        print(count)


if __name__ == "__main__":
    main()
