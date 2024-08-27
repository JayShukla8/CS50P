def main():
    str1 = input("camelCase: ")
    str2 = ""
    for letter in str1:
        if(letter.isupper()):
            x = letter.lower()
            str2=str2+"_"
            str2=str2+x
        else:
            str2=str2+letter
    print(f"snake_case: {str2}")

if __name__ == "__main__":
    main()
