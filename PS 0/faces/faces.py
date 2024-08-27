
def convert(str):
    str = str.replace(":)" , "🙂")
    str = str.replace(":(" , "🙁")
    return str

def main():
    prompt = "Enter your string: "
    str = input(prompt)
    str = convert(str)
    print(str)

main()
