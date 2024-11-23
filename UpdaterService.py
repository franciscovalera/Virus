import os 
import requests
from PIL import Image
import time
import sys
import pygame

# URL de la imagen y del audio
url_imagen = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3mxDMPgcDS2wWQmtMVhBgx8eYAppd-k4OvQ&s"
url_audio = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=es&q=JA!JA!"

# Obtener el directorio del usuario y crear la rutas
directorio_usuario = os.path.expanduser("~")
ruta_ansel = os.path.join(directorio_usuario, "ansel")
ruta_imagen = os.path.join(ruta_ansel, "images.jpeg")
ruta_audio = os.path.join(ruta_ansel, "translate_tts.mp3")

# Función para descargar
def descargar(url, ruta_destino):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        with open(ruta_destino, 'wb') as archivo:
            archivo.write(response.content)
        print(f"Imagen descargada en {ruta_destino}")
    except requests.ConnectionError:
        print("Error de conexión.")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
    except FileNotFoundError as fnf_error:
        print(f"Error de archivo: {fnf_error}")
    except PermissionError:
        print("Error de permisos: No se puede escribir en la ruta de destino.")
    except OSError as os_error:
        print(f"Error del sistema operativo: {os_error}")
    except Exception as e:
        print(f"Otro error ocurrió: {e}")

# Función para reproducir el audio
def reproducir_audio():
    try:
        descargar(url_audio, ruta_audio)
        pygame.mixer.init()  
        pygame.mixer.music.load(ruta_audio)  
        pygame.mixer.music.play() 
    except Exception as e:
        print(f"Error al reproducir el audio: {e}")

# Función para mostrar la imagen repetidamente
def mostrar_imagen():
    try:
        descargar(url_imagen, ruta_imagen)          
        try:
            imagen = Image.open(ruta_imagen)
            imagen.show()
            time.sleep(3)
        except FileNotFoundError as fnf_error:
            print(f"Error: {fnf_error}")
        except Exception as e:
            print(f"Otro error ocurrió: {e}")
    except KeyboardInterrupt:
        print("Intento de interrupción manual bloqueado.")
        mostrar_imagen()

# Función para verificar si existe la "llave secreta" para detener el script
def verificar_llave_secreta():
    llave_secreta = os.path.join(directorio_usuario, "HESIDOHAKEADO.txt")
    if os.path.exists(llave_secreta):
        print("Llave secreta encontrada, deteniendo el programa...")
        sys.exit(0)  

# Bucle principal para mostrar imagen reproducir el audio y verificar la "llave secreta"
def hakear():
    while True:
        verificar_llave_secreta()
        reproducir_audio()
        mostrar_imagen()

# Iniciar el bucle principal
hakear()