#!/usr/bin/env python3
import os, sys

extensio = ".csv"

try:
    ruta = os.path.dirname(__file__)
    paramEntrada=False
    if len(sys.argv) > 1:
    # Fitxer d'escriptura
        comarca=sys.argv[1]
        fitxerE = comarca+extensio
        rutaFitxerE = os.path.join(ruta,fitxerE)
        paramEntrada=True
        
    # Fitxer de lectura     
    fitxerL = "UF3NF1A4-poblacionsComarques.csv"
    rutaFitxerL = os.path.join(ruta,fitxerL)   

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
        else:

        #Si tot ha anat bé, farem l'escriptura al fitxer de la comarca corresponent
            try:
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
                            if paramEntrada:
                                paramEntrada=False
                            else:
                                comarca=input("Introdueix la comarca: ")
                                fitxerE = comarca+extensio
                                rutaFitxerE = os.path.join(ruta,fitxerE)
                            if comarca not in poblacionsC:
                                raise ValueError(f"La comarca {comarca} no existeix")
                            try:
                                fitxerE = open(rutaFitxerE, "w")
                                for x in poblacionsC[comarca]: 
                                    fitxerE.write(f"{x};{poblacionsC[comarca][x]}\n")
            #                    fitxerE.write(txt)
                            except:
                                print("Error al guardar les dades.")
                            finally:
                                fitxerE.close()
                        elif opcio==2:
                            sortir=True
                        else:
                            raise ValueError("Opció incorrecta.")
                    except ValueError as i:
                        print(i)
                    except:
                        print("Error general al bucle")
            # Fuera del bucle
            except:
                print("Error en obrir el fitxer d'escriptura.")
        finally:
            fitxerL.close()

    except:
        print("Error en obrir el fitxer de comarques.")
except Exception as error:
    print(f"{error.args[0]} El programa finalitza.")
except:
    print("Error: El programa finalitza.")