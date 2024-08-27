from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    dt = input("Date of Birth: ")
    try:
        year, month, day = check_date(dt)
        date_of_birth = date(int(year), int(month), int(day))
        today_date = date.today()
        difference = today_date - date_of_birth
        difference = int(difference.days)
        difference = convert(difference)
        print(difference,"minutes")
    except:
        sys.exit("Invalid Date")

def check_date(dt):
    if match := re.search(r"^([0-9][0-9][0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$",dt):
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        return year, month, day

def convert(d):
    minutes = d*24*60
    return p.number_to_words(minutes, andword="").capitalize()

if __name__=="__main__":
    main()
