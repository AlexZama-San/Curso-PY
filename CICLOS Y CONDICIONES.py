def pareimpar(x,y):
    while x<=y:
        if (x%2)==0:
            print("%s es par"%x)
        else:
            print("%s es impar"%x)
        x+=1
x1= int(input("escriba el valor de inicio "))
y1=int(input("escriba el valor final "))
pareimpar(x1,y1)