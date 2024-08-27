def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = len(s)
    #length problem
    if(n<2 or n>6):
        return False

    #start with atleast 2 letters or more problem
    s1 = s[0:2]
    for i in s1:
        if(not i.isalpha()):
            return False

    #first number used cannot be 0 problem
    i = 0
    while(i<n and s[i].isalpha()):
        i=i+1
    if(i<n and s[i]=="0"):
        return False

    #only letters and numbers allowed problem
    for i in s:
        if((not i.isalpha()) and (not i.isdigit())):
            return False

    #no alphabet at the end problem
    i = 0
    while(i<n and s[i].isalpha()):
        i=i+1
    while(i<n and s[i].isdigit()):
        i=i+1
    if(i<n):
        return False
    return True

if __name__ == "__main__":
    main()
