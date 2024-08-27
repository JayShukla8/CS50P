def main():
    str = input("Input: ")
    str = shorten(str)
    print(f"Output: {str}")


def shorten(word):
    new_str = ""
    for ele in word:
        ele_lower = ele.lower()
        if ele_lower not in ["a","e","i","o","u"]:
            new_str = new_str + ele
    return new_str


if __name__ == "__main__":
    main()
