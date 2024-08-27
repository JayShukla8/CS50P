import inflect

p = inflect.engine()
#this line creates an instance of the engine class from the inflect module and assigns it to variable p
#engine class contains methods for performing various linguistic transformations and manipulations
#by creating an instance of this engine class, we can use the methods provided by the class such as joining words from a list, pluralising words, etc

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    line = p.join(names)
    print("\n"+"Adieu, adieu, to "+line)

if __name__ == "__main__":
    main()
