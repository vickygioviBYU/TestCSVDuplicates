# IMPORTS


import pandas as pd
import csv
import pytest


# GLOBAL VARIABLES


csvlist = []
csvlist_unicos = []
csvlist_duplicados = []


LOW = "low"


HIGH = "high"


csvlistfinal = []


"""


MATCHING SCORE


HIGH -> APELLIDO, CODIGO POSTAL, DIRECCION


LOW => APELLIDO


"""


# def ordenarPorNombre(df):


#     df_clean = df.drop_duplicates(subset=['name'])


#     print(df_clean)

# def ordenarPorCodigoPostal(df):


#     df_clean = df.drop_duplicates(subset=['postalZip'])


#     print(df_clean)

# def ordenarPorEmail(df):


#     df_clean = df.drop_duplicates(subset=['email'])


#     print(df_clean)

# def ordenarPorNombreYApellido(df):


#     df_clean = df.drop_duplicates(subset=['name', 'name1'])


#     print(df_clean)

# def ordenarPorAddress(df):


#     df_clean = df.drop_duplicates(subset=['address'])


#     print(df_clean)

# def duplicadosHighMatch():


#     # ABRIR
#     with open('duplicates.csv') as file:


#         # LEER
#         csv_reader = csv.reader(file, delimiter=',')

        
#         next(csv_reader)


#         for row in csv_reader:


#             csvlist.append([row[2], row[4], row[5]])


#     # RECORRER DICCIONARIO
#     for count, i in enumerate(csvlist):
            

#             if i not in csvlist_unicos:


#                 csvlist_unicos.append(i)


#             else:

                
#                 # SI ESTA, ES DUPLICADO
#                 # PRIMERA OCURRENCIA DEL ELEMENTO
#                 index = csvlist.index(i)


#                 # SI SON DIFERENTES LOS INDICES, ES DUPLICADO
#                 if index != count:
#                     csvlist_duplicados.append((index, count))


def output():


    outputList = []


    for duplicado in csvlist_duplicados:

        
        # count += 1

        
        duplicado_original = duplicado[0]


        duplicado_duplicado = duplicado[1]


        # print(csvlist)


        # CONTACTO ORIGINAL
        source = csvlistfinal[duplicado_original]


        # CONTACTO DUPLICADO
        match = csvlistfinal[duplicado_duplicado]


        # SI MATCHEA CON HIGH O LOW
        if source[2] == match[2] and source[4] == match[4] and source[5] == match[5]:
            

            outputList.append([duplicado_original, duplicado_duplicado, HIGH])
            print(duplicado_original, duplicado_duplicado, HIGH)


        elif source[2] == match[2]:


            outputList.append([duplicado_original, duplicado_duplicado, LOW])
            print(duplicado_original, duplicado_duplicado, LOW)


        # print("Source: " + source + ", Match: " + match)

    # print(count)


    return outputList


def duplicados():

    for key, value in enumerate(csvlist):
            

        if value not in csvlist_unicos:


            csvlist_unicos.append(value)


        else:


            index = csvlist.index(value)


            if index != key:


                csvlist_duplicados.append((index, key))


def duplicadosMatch():


    with open('duplicates.csv') as file:


        csv_reader = csv.reader(file, delimiter=',')
        

        next(csv_reader)


        for row in csv_reader:

            
            # MATCH MINIMO, APELLIDO
            csvlist.append(row[2])


            # LISTA DE CONTACTOS ENTERA
            csvlistfinal.append(row)


    
    

    # print(csvlist_duplicados)

    # count = 0

    


def main():


    print("Program started.")


    duplicadosMatch()


    duplicados()


    output()
                

    # print(csvlist)

    # print(csvlist_duplicados)
    
    


    # # df = pd.read_csv("duplicates.csv")


    # newnames = ['contactID', 'name', 'name1','email', 'postalZip','address']


    # df = pd.read_csv('duplicates.csv', names = newnames, header = 0, parse_dates=True, dayfirst=True)


    # df = df.loc[:,['contactID', 'name', 'name1', 'email','postalZip', 'address']]


    # ordenarPorAddress(df)


    # ordenarPorNombreYApellido(df)


    # ordenarPorEmail(df)


    # ordenarPorCodigoPostal(df)


    # ordenarPorNombre(df)


# Using the special variable 
# __name__


# TESTS


def test_output():


    csvlist_duplicados.clear()
    csvlist_duplicados.append((0, 1))
    csvlist_duplicados.append((2, 3))


    csvlistfinal.clear()
    csvlistfinal.append(['1', 'Ciara', 'French', 'mollis.lectus.pede@outlook.net', '39746', '449-6990 Tellus. Rd.'])
    csvlistfinal.append(['2', 'Charles', 'French', 'nulla.eget@protonmail.couk', '39746', '449-6990 Tellus. Rd.'])
    csvlistfinal.append(['3', 'Victor', 'Savage', 'orci@protonmail.net', '82025', 'P.O. Box 775, 8910 Arcu. Road'])
    csvlistfinal.append(['4', 'Paul', 'Savage', 'quis.diam@aol.couk', '95904', '735-3498 Magna. Street'])
    

    listaOutput = output()


    assert listaOutput == [[0, 1, 'high'], [2, 3, 'low']]


def test_duplicados():


    csvlist.clear()


    csvlist_unicos.clear()


    csvlist_duplicados.clear()


    duplicadosMatch()


    duplicados()


    long_csvlist = len(csvlist)


    long_unicos = len(csvlist_unicos)


    long_duplicados = len(csvlist_duplicados)


    print(long_csvlist)


    assert long_unicos + long_duplicados == long_csvlist



def test_duplicados_match():


    csvlist.clear()


    csvlistfinal.clear()


    with open('duplicates.csv') as file:


        csv_reader = csv.reader(file, delimiter=',')


        next(csv_reader)


        longitudCSV = 0

        for row in csv_reader:


            longitudCSV += 1

            
            # MATCH MINIMO, APELLIDO
            csvlist.append(row[2])


            # LISTA DE CONTACTOS ENTERA
            csvlistfinal.append(row)


        longitudcsvlist = len(csvlist)


        longitudcsvlistfinal = len(csvlistfinal)


    assert longitudCSV == longitudcsvlist

    
    assert longitudCSV == longitudcsvlistfinal





if __name__=="__main__":


    main()

    # test_duplicados_match()
    # test_duplicados()
    

    # test_output()