
def main():


    edad = int(input("Ingresa tu edad:"))
    iden = str(input("¿Tiene su identificación oficial?"))
    iden == "s" or "n"

    if edad <18 or (iden == "n"):
       print("No cumples requisitos")
    elif edad >=18 and (iden ==  "s" ):
       print("Trámite de licencia concedido")  
    else: 
       print("Respuesta incorrecta")

 


main()