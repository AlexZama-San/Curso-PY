archivo=open('palabras.txt',"r")
palabras= list(archivo)
archivo.close
s=0
while s < len(palabras):
    print(palabras[s].rstrip('\n'))
    s+=1