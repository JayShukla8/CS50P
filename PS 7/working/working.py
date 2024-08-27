import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)$",s):
        if int(match.group(1)) > 12 or int(match.group(4)) > 12:
            raise ValueError
        first = time(int(match.group(1)), match.group(2),match.group(3))
        second = time(int(match.group(4)), match.group(5), match.group(6))
        return first + " to " + second
    else:
        raise ValueError

def time(hours, minutes, ap):
    if ap == "AM":
        if hours == 12:
            hours = 0
    else:
        if hours == 12:
            hours = 12
        else:
            hours = hours + 12

    if minutes == None:
        minutes = ":00"
        return f"{hours:02}{minutes}"
    else:
        return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
