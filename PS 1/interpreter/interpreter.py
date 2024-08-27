def main():
    str = input("Expression: ")
    [x, y, z] = str.split(" ")
    if y=="+":
        ans = int(x)+int(z)
    elif y=="-":
        ans = int(x)-int(z)
    elif y=="*":
        ans = int(x)*int(z)
    elif y=="/":
        ans = int(x)/int(z)
    else:
        print("enter valid operation")
    print(f"{ans:.1f}")

main()
