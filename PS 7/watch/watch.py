import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    if matches := re.search(r'^.*src="https?://(?:www\.)?youtube\.com/embed/(.+)".*', s, re.IGNORECASE):
        code = matches.group(1)
        return ("https://youtu.be/"+code)
    return "None"

if __name__ == "__main__":
    main()
