import sys
import csv

def main():
    table = []
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
            sys.exit("Not a csv file")
        else:
            try:
                with open(sys.argv[1]) as before:
                    reader = csv.DictReader(before)
                    for row in reader:
                        lastname, firstname = row["name"].split(", ")
                        table.append({"first": firstname, "last": lastname, "house": row["house"]})
                with open(sys.argv[2], "w") as after:
                    writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"])
                    writer.writeheader()
                    for i in range(len(table)):
                        writer.writerow({"first": table[i]["first"], "last": table[i]["last"], "house": table[i]["house"]})
            except FileNotFoundError:
                sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
