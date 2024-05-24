import os

##### Carpeta dataset #####
location = 'C:/Users/Limb/Desktop/Proyecto Parcial/Python/Dataset'

#### Validar si existe carpeta ####
if not os.path.exists(location): ##carpeta no existe
    ## creo la carpeta
    os.mkdir(location)
else: ##carpeta existe
    ##borrar contenido
    for root, dirs, files in os.walk(location,topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) #Eliminar archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) #Eliminar las carpetas

## importar libreria API Kaggle ###
from kaggle.api.kaggle_api_extended import KaggleApi

## Autenticarnos ##
api = KaggleApi()
api.authenticate()

### Descargar dataset ###
print(api.dataset_list(search=''))

#api.dataset_download_file('rahulvyasm/netflix-movies-and-tv-shows','SAT__College_Board__2010_School_Level_Results_20240506.csv',path=location,force=True,quiet=False) #Descarga el archivo comprimido y se selecciona la ruta cuando es un archivo , cuando no es el codigo de abajo
api.dataset_download_files('rahulvyasm/netflix-movies-and-tv-shows',path=location,force=True,quiet=False,unzip=True)