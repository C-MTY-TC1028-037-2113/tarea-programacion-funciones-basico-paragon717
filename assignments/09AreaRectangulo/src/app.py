
def main():
    X = int(input("Ingresa la medida del lado 1:"))
    Y = int(input("Ingresa la medida del lado 2:"))
    Z = int(input("Ingresa la medida del lado 3:"))

    if X+Y > Z and Y+Z > X and X+ Z > Y:
       if  X == Y and Y == Z :
           print("ES UN TRIANGULO EQUILATERO")
       elif (X ==Y and X!= Z)  or (Y == Z and Z!= X) or (X== Z and X!=Y):
            print("ES UN TRIANGULO ISOSCELES")
       elif (X!=Z and Y!=Z and X!=Y):
            print("ES UN TRIANGULO ESCALENO")