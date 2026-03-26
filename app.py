import os
import shutil

# Configura la ruta que quieres limpiar (puedes usar "." para la carpeta actual)
directorio_a_organizar = "./archivos"


# Diccionario que define las extensiones y sus carpetas destino
EXTENSIONES = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Comprimidos": [".zip", ".rar"]
}

def organizar():
    # Crear el directorio si no existe (para pruebas)
    if not os.path.exists(directorio_a_organizar):
        os.makedirs(directorio_a_organizar)
        print(f"Creada carpeta de prueba: {directorio_a_organizar}")

    # Recorrer los archivos en la carpeta
    for archivo in os.listdir(directorio_a_organizar):
        ruta_archivo = os.path.join(directorio_a_organizar, archivo)

        # Saltar si es una carpeta
        if os.path.isdir(ruta_archivo):
            continue

        # Obtener la extensión del archivo
        nombre, extension = os.path.splitext(archivo)
        extension = extension.lower()

        # Mover el archivo según su extensión
        transferido = False
        for carpeta, lista_ext in EXTENSIONES.items():
            if extension in lista_ext:
                ruta_destino = os.path.join(directorio_a_organizar, carpeta)
                
                # Crear la subcarpeta si no existe
                if not os.path.exists(ruta_destino):
                    os.makedirs(ruta_destino)
                
                # Mover el archivo
                shutil.move(ruta_archivo, os.path.join(ruta_destino, archivo))
                print(f"🤠 transferido: {archivo} -> {carpeta}/")
                transferido = True
                break
        
        if not transferido and extension:
            print(f"ℹ️ Saltado (sin categoría): {archivo}")

if __name__ == "__main__":
    organizar()
    print("\n¡Automatización terminada!")