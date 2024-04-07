#!/usr/bin/env python3
import datetime
import os
import sys


#Aquest programa permet treballar tant amb un arxiu de pagines forani i un arxiu de categories forani o nomes l'arxiu de categories
#pero cal tenir en compte que per poder fer al treballar amb el metode sys.argv ho he programat per que s'hagi d' indicar primer el 
#arxiu de les categories i despres l'arxiu de les pagines 
#SINO NO FUNCIONARA

#l'arxiu de categories es creat per mi ja que al importar de csv i posa un \n i per separar-ho hi he afegit una coma al final
# de cada categoria



tasks = list()
#Llista de diccionaris amb la que treballa el programa

#########################
#Importacio de categories
#########################
if len(sys.argv) > 1 :
        fichero=sys.argv[1]
        ruta2=os.path.dirname(__file__)
        rutaConjunta2=os.path.join(ruta2,fichero)
        split = os.path.splitext(fichero)
        extensio = split[1] 
        fitxerCat = True
else:
        raise FileNotFoundError("Siusplau indica el fitxer de categories.")

#en cas de que es treballi amb un fitxer ja existent l'obrim amb lectura i comprovem que la direccio existeix
if fitxerCat:            
    if os.path.exists(rutaConjunta2) :
        archivo2 = open(rutaConjunta2, "r")
        print(f"Anem a treballar amb el fitxer {fichero}")
        
    else:
        raise FileNotFoundError("Error en obrir el fitxer de categories.")

    #importem les categories a una llista i tanquem l'arxiu
    try:   
        categories=[]
        
        for x in archivo2:
            categoria=x.split(",")
            categories.append(categoria[0])
    except:
            print("Error: no s'han pogut carregar les dades.")
    finally:
            archivo2.close()




#########################
#Importacio de dades web
#########
#proces per comprovar si es treballara amb un fitxer existent i si es aixi agafar la direcció del mateix
fitxerNou = False
if len(sys.argv)>2:
            fichero=sys.argv[2]
            ruta=os.path.dirname(__file__)
            rutaConjunta=os.path.join(ruta,fichero)
            split = os.path.splitext(fichero)
            extensio = split[1] 
            formato = "%Y-%m-%d %H:%M:%S.%f"
            print (fichero)            
else:
            fitxerNou = True

if fitxerNou == False: 
    #en cas de que es treballi amb un fitxer ja existent l'obrim amb lectura i comprovem que la direccio existeix
    if os.path.exists(rutaConjunta) :
                        archivo = open(rutaConjunta, "r")
                        print(f"Anem a treballar amb el fitxer {fichero}")
    else:
                    raise FileNotFoundError("Error en obrir el fitxer de les pagines.")
    

    try:   
    #en cas de que es treballi amb un fitxer ja existent convertim el fitxer .csv en una estructura per treballar al programa
                for x in archivo:
                    tasca = x.split(",")
                    task ={             
                                        "id": tasca[0],
                                        "url": tasca[1],
                                        "category": tasca[2],
                                        "data":datetime.datetime.strptime(tasca[3],formato)}
                    tasks.append(task)
    except:
                        print("Error: no s'han pogut carregar les dades.")

    finally:
            archivo.close()




      
            
            




sep = "\n------------"

opcio = None
final = 5




while opcio != final:

    print("\n1. Veure tasques")
    print("2. Crear tasca")
    print("3. Eliminar una tasca")
    print("4. Desar i sortir")
    print("5. Sortir")


    try:
        opcio = int(input("\nIntrodueix una opcio: "))
    
    
    
        if opcio == 1:
                #######################################################
                # Mostra les pagines ordenades per categoria 
                #######################################################
                for p in categories:
                    print(p)    
                    for x in tasks:
                        if x["category"] == p :
                            for j,i  in x.items() :
                                print (f"{j} , {i} ")
                            print("") 
                    print("")


        elif opcio == 2:
                #######################################################
                # Crear i afegir una tasca a la llista 
                #######################################################
                afegir= {
                }
                if len(tasks) == 0 :
                    posicio = 1  
                else   :  
                    diatanciallista = len(tasks)
                    posicio = tasks[diatanciallista - 1 ]["id"]
                    posicio = int(posicio)
                    posicio = posicio + 1  
                    posicio = str(posicio)

                #proces per introduir i controlar que l'url no existeixi previment
                urlC=True
                Coincidencies=0
                while urlC:
                    Coincidencies=0
                    url=input("Afegeix el url desitjat ")
                    for x in tasks:
                        if x["url"]==url:
                            print("Aquesta URL ja existeix. Tornau a intentar ")
                            Coincidencies+=1
                        
                    if Coincidencies == 0:
                        urlC=False

                #proces per cintroduir i controlar que la categoria exiteixi
                for  x in categories :
                    print(x)
                category=input("Afegeix la categoria desitjada: ")
                while category not in categories:
                    for  x in categories :
                        print(x)
                    category=input("Afegeix la categoria desitjada: ")
                    if category not in categories: 
                        print("La categoria no existeix torna a intentar-ho")

                #agregacio de la nova pagina a la llista
                afegir["id"]=posicio
                afegir["url"]=url
                afegir["category"]=category
                afegir["data"]=datetime.datetime.now()
                tasks.append(afegir)

        
        elif opcio == 3:
                #######################################################
                # Elimina una pagina
                #######################################################
                #Mostrem les llistes actuals per id
                if len(tasks)>0:
                    for i,x in enumerate(tasks):
                        print (f"{i+1}. ") 
                        for j,k  in x.items() :
                            print (f"{j} : {k} ")
                            
                        print("")   
                    
                    #Demanem el id a eliminar i comprovem que existeixi a la llista 
                    tascaElm = input("Introdueix el ID de la pagina a eliminar ")
                    if not any(d['id'] == tascaElm for d in tasks):
                        print("El id no existeix")
                    
                    #recorrem la llista en busca del id i la posicio per eliminarlo 
                    else:
                        for i,x in enumerate(tasks):
                            if x["id"] == tascaElm:
                                eliminacio=True
                                #Hi demanem confrmacio
                                while eliminacio:
                                        comprovacio = input(f"Estas segur d'eliminar la tasca amb id {tascaElm}? s/n")
                                
                                        if comprovacio == "S" or comprovacio == "s":
                                            tasks.pop(i)  
                                            eliminacio = False
                                            print("S'ha eliminar correctament")    
                                        elif comprovacio == "N" or comprovacio == "n":
                                            print("Eliminacio cancelada")
                                            eliminacio = False
                                        else :
                                            print("No has introduït ni 'S' ni 'N'")
                else:
                      print("La llista es buida")

                            

                
                



        
        elif opcio == 4:
                
                #######################################################
                # Desar dades actuals en un fitxer
                #######################################################
                
                    try:
                        #demanem confirmacio per guardar
                        comprovacio = input("Estas segur que vols guardar el contingut actual abans de sortir?(s/n)")
                        if comprovacio == "S" or comprovacio == "s":
                            try:
                                #depenent si el fitxer exiteix previament o no et demana un nom nou o reescriura l'actual
                                if fitxerNou == False:
                                    fitxer = open(rutaConjunta, "w")
                                else:
                                    nou=input("introdueix el nom del fitxer nou")
                                    fitxer = open(nou + ".csv", "w")
                                print("fet")
                                for tasca in tasks:
                                            fitxer.write(f"{tasca['id']},{tasca['url']},{tasca['category']},{tasca['data']},\n")
                            except:
                                raise EOFError ("Error al carregar les dades.")
                            else:
                                opcio=final
                                print("Fins aviat!")
                            finally:
                                fitxer.close()
                            
                        elif comprovacio == "n" or comprovacio == "N":
                            opcio = 5
                            continue
                            
                        else:
                            raise NameError("No has introduït ni 'S' ni 'N'")


                    except PermissionError : 
                        print("no es pot escriure")
                    except FileNotFoundError:
                        print("El fitxer no existeix")
        elif opcio == final:
                print("Fins aviat!")
        else :
            print("Aquest numero no existeix")
        

    except ValueError:
            print("Opció incorrecte. Prova un numero del menú")


  