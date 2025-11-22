###################################################
#                Lector de .hocr                  #
#                                                 #
# V.1.0.0 //12 11 2025//                          #
# V.1.1.0 //          //                          #
# V.1.2.2 //          //                          #
# V.1.3.2 //21 11 2025//                          #
# Desplegado con streamlit                        #
# Desarrollador: Sergio Emiliano López Bautista   #
#                                                 #
###################################################

# ------------------------- Requerimientos y librerías -------------------------------
import os
import codecs
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

# --------------------------- Seteadores ----------------------------------------------
st.set_page_config(page_title="Lector de HOCR",
                   page_icon = "👁️",
                   layout="wide")
st.title("Lector de HOCR")
# --------------------------- Funciones -----------------------------------------------
def instrucciones():
    if not os.path.exists("data/instrucciones.txt"):
        raise FileNotFoundError(f"El archivo {"data/instrucciones.txt"} no existe.")

    with codecs.open("data/instrucciones.txt", "r", encoding="utf-8") as f:
        fi = f.read()
    file = fi.split('\n')

    for linea in file:
        st.markdown(linea)

def hocr_csv(ruta_hocr, salida_csv):
    
    # Leemos el archivo HOCR
    with open(ruta_hocr, "r", encoding="utf-8") as f:
        sopa = BeautifulSoup(f, "html.parser")
    
    # Extraemos la info de cada palabra
    data = []

    ## Primera iteración para el carea
    # Por cada elemento carea hacemos un bloque
    for a in soup.find_all("span", class_="ocr_carea"):

        # Dentro de cada bloque encontramos las líneas de texto
        lineas = a.find_all("span", class_="ocr_line")  
        
        #La Línea 0 es el header
        header = lineas[0].get_text(strip=True)
        ## Segunda iteración para las líneas dentro del bloque carea
        # Por cada línea, cachamos el texto
        for b in lineas[1:]:
            texto = b.get_text(strip=True)
            data.append({header: texto})
    return data

# -------------------------------- Interfaz (MAIN)-------------------------------------
#Ponemos las instrucciones
instrucciones()

#ejemplo 1
frame1 = pd.DataFrame(hocr_csv_estructurado("hocr/1C_5.hocr"))

st.markdown("# Ejemplo 1")
st.pdf("recursos/1C.PDF")
st.dataframe(frame1)
st.download_button(
    label = "1C - Descargar CSV",
    data = frame1.to_csv(index=False).encode('utf-8'),
    file_name = "1C_csv.csv",
    mime = "text/csv",
)

#ejemplo 2
frame2 = pd.DataFrame(hocr_csv_estructurado("hocr/1E_1.hocr"))

st.markdown("# Ejemplo 2")
st.pdf("recursos/1E.pdf")
st.dataframe(frame2)
st.download_button(
    label = "1E - Descargar CSV",
    data = frame2.to_csv(index=False).encode('utf-8'),
    file_name = "1E_csv.csv",
    mime = "text/csv",
)

#ejemplo 3
frame3 = pd.DataFrame(hocr_csv_estructurado("hocr/3T_4.hocr"))

st.markdown("# Ejemplo 3")
st.pdf("recursos/3T.pdf")
st.dataframe(frame3)
st.download_button(
    label = "3T - Descargar CSV",
    data = frame3.to_csv(index=False).encode('utf-8'),
    file_name = "3T_csv.csv",
    mime = "text/csv",
)