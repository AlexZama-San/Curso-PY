import random

archivo=open('palabras.txt','r')
palabras=list(archivo)
archivo.close
x=random.randint(0,len(palabras)-1)
palabsec=palabras[x]
palabsec=palabsec.strip('\n')
vida=3

while(vida>0):
    resp=input("tienes %s vidas, adivina la palabra: "%vida)
    if resp==palabsec:
        print('¡ganaste!, la palabra era %s'%palabsec)
        break
    else:
        vida-=1
        print("te equivocaste, te quedan %s vidas"%vida)
print("perdiste, la palabra correcta era %s"%palabsec)
        