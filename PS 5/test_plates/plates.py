def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #checking the length restriction
    if len(s) < 2 or len(s) > 6:
        return False
    s_upper = s.upper()

    #checking that plate starts with 2 letters
    for el in s_upper[:2]:
        if not el.isalpha():
            return False

    #no periods, spaces, punctuations allowed
    for el in s_upper:
        if not el.isalnum():
            return False

    #checking that numbers come at the end only
    n = len(s_upper)
    i = 0
    while i<n and s_upper[i].isalpha():
        i=i+1

    if i==n:
        return True
    elif s_upper[i] == "0":
        return False
    else:
        while i<n and s_upper[i].isdigit():
            i=i+1
        if i==n:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
