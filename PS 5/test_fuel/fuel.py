def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit():
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    else:
        return round((int(x)/int(y))*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    while True:
        try:
            str = input("Fraction: ")
            percent = convert(str)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
