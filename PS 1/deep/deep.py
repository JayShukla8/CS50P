def answer(str):
    str = str.strip().lower()
    if(str=="42" or str=="forty two" or str=="forty-two"):
        return "Yes"
    return "No"

def main():
    str = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    str = answer(str)
    print(str)

main()
