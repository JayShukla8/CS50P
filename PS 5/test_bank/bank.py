def main():
    str = input("Greeting: ")
    str = str.lstrip()
    print(f"${value(str)}")


def value(greeting):
    g_lower = greeting.lower()
    if g_lower.startswith("hello"):
        return 0
    elif g_lower.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
