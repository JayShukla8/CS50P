
def energy(m):
    c = 300000000
    e = (m*c)*c
    return e

def main():
    m = int(input("Enter mass: "))
    e = energy(m)
    print(e)

main()
