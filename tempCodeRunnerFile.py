#script para organizar carpetas al trabajar con proyectos de C# en subcarpetas
import os 


def main():
    #     como inicia la carpeta   a que carpeta va 
    #carpetas("_arrays_",       "arrays_hashmap")
    carpetas("_stack_", "stack")




def carpetas(prefijo, carpeta_name):

    try:

        #ruta de la carptea principal 
        ruta_dsa = os.path.join(os.path.expanduser("~"), "Desktop", "DSA")
        #ruta de destino que se iran creando
        ruta_destino = os.path.join(ruta_dsa, carpeta_name)

   

        if not os.path.exists(ruta_destino):
            os.mkdir(ruta_destino)
        else:
            print("Esa carpeta ya existe")


        #poner cada carpeta/proyecto en su lugar correspondiente
        with os.scandir(ruta_dsa) as directorio:
            for carpeta in directorio:
                if carpeta.is_dir() and carpeta.name.startswith(prefijo):
                    ruta_origen = carpeta.path
                    ruta_destino_carpeta = os.path.join(ruta_destino, carpeta.name)
                    os.rename(ruta_origen, ruta_destino_carpeta)
                    print(f"Carpeta {carpeta.name} movida a {ruta_destino_carpeta}, ya puedes hacer un PR en GitHub ✔🚀")
    except:
        print("error")   

    




if __name__ == "__main__":
    main()