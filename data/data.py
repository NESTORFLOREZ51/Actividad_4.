import pandas as pd

# Importar datos del csv
data_teorico = pd.read_csv(r"E:\Desktop\p2\data")

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): # se llaman los iguientes datos
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]']
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]']
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion


