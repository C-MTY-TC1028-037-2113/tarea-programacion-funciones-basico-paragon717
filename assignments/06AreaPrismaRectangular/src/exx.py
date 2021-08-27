def area(base,altura):
    return base*altura

def main():
    b = float(input("Dame la base:"))
    a = float(input("Dame la altura:"))

    r = area(b,a)

    print("El área del rectangulo es:",r)

if __name__=='__main__':
    main()

