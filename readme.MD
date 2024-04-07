# Cargar fichero
```
    ruta = os.path.dirname(__file__)
    fitxerL = "UF3NF1A4-poblacionsComarques.csv"     o lo que se introduzca
    rutaFitxerL = os.path.join(ruta,fitxerL)  
    fitxerL = open(rutaFitxerL, "r")

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
