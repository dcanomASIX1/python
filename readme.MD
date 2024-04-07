# Cargar fichero
```
    ruta = os.path.dirname(__file__)
    fitxerL = "UF3NF1A4-poblacionsComarques.csv"     o lo que se introduzca/ Puedes poner una ubicacion sys si se pone
    rutaFitxerL = os.path.join(ruta,fitxerL)  
    fitxerL = open(rutaFitxerL, "r")

```
# Diferenciar si trabajas con fichero nuevo o diferente

```
if len(sys.argv)>2:
            fichero=sys.argv[2]
            ruta=os.path.dirname(__file__)
            rutaConjunta=os.path.join(ruta,fichero)
            split = os.path.splitext(fichero)
            extensio = split[1] 
            print (fichero)            
else:
            fitxerNou = True

```

# Guardar en estructura de diccionario

```
    try:
        fitxerL = open(rutaFitxerL, "r")
        try:
            linia=fitxerL.readline()
            poblacionsC={}
            while linia:
                dadesPoblacio=linia.rstrip().split(";")
                if dadesPoblacio[1] not in poblacionsC:
                    poblacionsC[dadesPoblacio[1]]={}
                poblacionsC[dadesPoblacio[1]][dadesPoblacio[0]]=dadesPoblacio[2]
                linia=fitxerL.readline()


        except:
            print("Error: no s'ha pogut llegir el fitxer de comarques.")

```
LAs posiciones dependen del archivo importado por lo tanto es importante saber como se ubican en este


**Tambien se puedo usar un for con el nombre del archivo**
```
                for x in archivo:
                    tasca = x.split(",")
                    task ={             
                                        "id": tasca[0],
                                        "url": tasca[1],
                                        "category": tasca[2],
                                        "data":datetime.datetime.strptime(tasca[3],formato)}
                    tasks.append(task)

```

# Guardar en otro archivo

```
 fitxerE = open(rutaFitxerE, "w")
    for x in poblacionsC[comarca]: 
        fitxerE.write(f"{x};{poblacionsC[comarca][x]}\n")


        finally:
            fitxerL.close()


```

## Possibles errorres

```
except:
     print("Error general al bucle")
# Fuera del bucle
 except:
     print("Error en obrir el fitxer d'escriptura.")

```


# Menu
```

sortir=False
opcio=1
  while not sortir:
                    try:
                        if not paramEntrada:
                            menu='''
                            1. Introduir Comarca
                            2. Sortir
                            Escull una opció: '''
                            opcio=int(input(menu))
                        if opcio==1:
```



