#!/usr/bin/env python3
import datetime
import os
import sys 

print("This is the name of the program:", sys.argv[0]) 
  
print("Argument List:", str(sys.argv)) 

ruta=os.path.dirname(__file__)
fichero=sys.argv[1] #Nombre del fichero que usamos
rutaConFichero=os.path.join(ruta,fichero)

formato = "%Y-%m-%d %H:%M:%S.%f"
#Llista de diccionaris amb la que treballa el programa
tasks = list()
try:
    if os.path.exists(rutaConFichero):
        archivo = open(rutaConFichero, "r")
    
        for x in archivo:
            tasca = x.split(",")
            task ={             
                    "title": tasca[0],
                    "date": datetime.datetime.strptime(tasca[1],formato),
                    "done": bool(eval(tasca[2]))
                }
            tasks.append(task)
    else:
            raise FileNotFoundError("El fitxer no existeix.")
except FileNotFoundError as error:
    print(error)
except:
    print("Error general en obrir el fitxer.")

sep = "\n------------"

opcio = None
final = 6




while opcio != final:

    print("\n1. Veure tasques")
    print("2. Crear tasca")
    print("3. Modificar tasca")
    print("4. Eliminar tasca")
    print("5. Desar i sortir")
    print("6. Sortir")


    try:
        opcio = int(input("\nIntrodueix una opciรณ: "))
    

    
        if opcio == 1:
            #######################################################
            # Mostrar dos llistats de tasques (fetes i no fetes) 
            #######################################################
            x = {
                "Fetes": [],
                "No fetes": []
            }
            for index, task in enumerate(tasks):
                if (task["done"]):
                    x["Fetes"].append(task)
                else: 
                    x["No fetes"].append(task)

            for key, list in x.items():
                print(f"{sep}\n{key} ({len(list)}){sep}")
                for index, task in enumerate(list):
                    title = task['title']
                    date = task['date'].strftime("%d/%m/%y %H:%M")
                    print(f"Tasca {index+1}. {title} - {date}")

        elif opcio == 2:
            #######################################################
            # Crear i afegir una tasca a la llista 
            #######################################################
            afegir= {

            }
            nom=input("Afegeix el nom desitjat")
            afegir["date"]=datetime.datetime.now()
            afegir["done"]= False
            afegir["title"]=nom
            tasks.append(afegir)

    
        elif opcio == 3:
            #######################################################
            # Marcar una tasca com feta o no feta
            #######################################################
            for i,x in enumerate(tasks):
                print(f'''{i+1}.  {x["title"]}''') 

           
            nom=int(input("Afegeix elnumero desitjat a modificar "))
            nom = nom - 1 
            
            

            try:   

                    for i,x in enumerate(tasks):
                        if nom == (i+1) : 

                            tascaFeta=input("Tasca feta? s/n ")

                            if tascaFeta == "s" or tascaFeta == "S":
                                print("Implementa-ho")
                                    
                                x["done"] = True
                            elif tascaFeta == "n" or tascaFeta == "N":
                                print("Implementa-ho")
                                    
                                x["done"] = False
                            else:
                                print("l'opcio no exiteix")
            except ValueError:
                    print("No es un numero")
            if nom > len(tasks ):
                raise NameError ("no existeix aquetsa ofpcio")
            
           
                

        elif opcio == 4:
            #######################################################
            # Eliminar una tasca de la llista
            #######################################################
            for x in tasks:
                print(x["title"])

            eliminarLlista= input("Introdueix el nom de la tasca ")
            for i,x in enumerate(tasks):
                if x["title"] == eliminarLlista:
                    tasks.pop(i)



    
        elif opcio == 5:
            #######################################################
            # Desar dades actuals en un fitxer
            #######################################################

            try:

                confirma = input("Estas segur que vols sobreescriure el contingut actual abans de sortir?(s/n)")
                if confirma in ['s','S']:
                    try:
                
                        fitxer = open(rutaConFichero, "w")

                        for tasca in tasks:
                            #fitxer.write(tasca['title']+","+str(tasca['date'])+","+str(tasca['done'])+",\n")
                            fitxer.write(f"{tasca['title']},{tasca['date']},{tasca['done']},\n")
                    except:
                        raise EOFError ("Error al carregar les dades.")
                    else:
                        opcio=final
                        print("Fins aviat!")
                    finally:
                        fitxer.close()
                elif confirma in ['n','N']:
                    continue
                else:
                    raise NameError("No has introduït ni 'S' ni 'N'")


            except PermissionError : 
                print("no es pot escriure")
            except FileNotFoundError:
                print("El fitxer no existeix")
        elif opcio == final:
            #######################################################
            # Tancar el programa
            #######################################################
            print("Fins aviat!")

        else:
            print("Opció incorrecte.")


    except ValueError:
        print("l'opcio no exsisteix ")