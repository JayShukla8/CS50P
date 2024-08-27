import sys
import csv
from tabulate import tabulate

def main():
    table = []
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                title_row = reader.fieldnames
                table.append(title_row)
                for row in reader:
                    table.append(list(row.values()))
        except FileNotFoundError:
            sys.exit("File does not exist")
        print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
