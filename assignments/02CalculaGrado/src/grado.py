def calcula_grado(x):
    #Score nota mayor a 0.9 A, mayor a 0.8 B, mayor a 0.7 C, mayor a 0.6 D, otro dentro del rango F
    if 1 > x > 0.9 
    x = A
        elif 0.9 > x > 0.8
        x = B
            elif 0.8 > x > 0.7
            x = C
                elif 0.7 > x > 0.6
                x = D
                    elif 0.6 > x > 0.0
                    x = F
     else:
     print ('score incorrecto')

def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
