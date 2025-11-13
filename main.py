###################################################
#                Lector de .hocr                  #
#                                                 #
# V.1.0.0 //12 11 2025//                          #
# V.1.1.0 //          //                          #
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
    for linea in sopa.find_all("span", class_="ocr_line"):
        text = linea.get_text(strip=True)

        data.append({"text": text})
    
    pd.DataFrame(data).to_csv(salida_csv, index=False)


def hocr_csv_estructurado(hocr_file, csv_output):

    with open(hocr_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    data = []
    careas = soup.find_all("span", class_="ocr_carea")

    for carea in careas:

        lines = carea.find_all("span", class_="ocr_line")

        if not lines:
            continue

        header = lines[0].get_text(strip=True)

        for line in lines[1:]:
            content = line.get_text(strip=True)
            if content:  # Evitar líneas vacías
                data.append({"header": header, "content": content})

    pd.DataFrame(data).to_csv(csv_output, index=False)
    print(f"CSV estructurado guardado en: {csv_output}")

# -------------------------------- Interfaz (MAIN)-------------------------------------
instrucciones()

# Uso:
#hocr_csv("hocr/1E_1.hocr", "salida_1E_1.csv")
hocr_csv_estructurado("hocr/1E_1.hocr", "salida_1E_1_estructurado_2.csv")