def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                m, d, y = date.split("/")
            elif "," in date:
                m, y = date.split(", ")
                m, d = m.split(" ")
                m = (months.index(m))+1
            elif "," not in date:
                raise SyntaxError
            if int(m) < 0 or int(m) > 12 or int(d) > 31:
                raise ValueError
            print(f"{int(y)}-{int(m):02}-{int(d):02}")
            break
        except:
            continue

if __name__ == "__main__":
    main()
