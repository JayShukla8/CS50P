import sys
import json
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    while True:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            break
        except requests.RequestException:
            continue
    o = response.json()
    r = float(o["bpi"]["USD"]["rate_float"])
    ans = r*n
    print(f"${ans:,.4f}")


if __name__ == "__main__":
    main()
