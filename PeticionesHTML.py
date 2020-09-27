import requests
if __name__ == '__main__':
    url='https://httpbin.org/anything'
    args ={"nombre": "Alex", "apellido": "Rojas", "Edad":"21"}


    res=requests.get(url, params=args)

    if res.status_code==200:
        contenido = res.content
        archivo=open('pruebadepeticion.json','wb')
        archivo.write(contenido)
        archivo.close
        #print(contenido)
    print (res)