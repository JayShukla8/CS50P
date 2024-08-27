
def main():
    str1 = input("Input: ")
    str2 = ""
    for ltr in str1:
        ltr2 = ltr.lower()
        if(ltr2 not in ["a", "e", "i", "o", "u"]):
            str2 = str2 + ltr
        else:
            continue
    print(f"Output: {str2}")

if __name__ == "__main__":
    main()
