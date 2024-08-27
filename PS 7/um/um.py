import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"^um$|^um[^\w]|([ ?]um[^\w])",s,re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
