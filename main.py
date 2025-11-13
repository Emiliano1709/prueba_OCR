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

def hocr_csv(ruta_hocr):
    # Leemos el archivo HOCR
    with open(ruta_hocr, "r", encoding="utf-8") as f:
        sopa = BeautifulSoup(f, "html.parser")
    
    # Extraemos la info de cada linea
    data = []
    for linea in sopa.find_all("span", class_="ocr_line"):
        lineas = linea.get_text(strip=True)

        data.append({"Lineas": lineas})
    
    return data

# -------------------------------- Interfaz (MAIN)-------------------------------------
#Ponemos las instrucciones
instrucciones()

# Mostramos los ejemplos (sin bucle, para que sea más claro por ahora y no haya confusión)
#ejemplo 1
st.markdown("# Ejemplo 1")
st.pdf("recursos/1C.PDF")
data1 = hocr_csv("hocr/1C_5.hocr")
frame1 = pd.DataFrame(data1)
des1 = frame1.to_csv(index=False).encode('utf-8')
st.dataframe(frame1)

st.download_button(
    label="1C - Descargar CSV",
    data=des1,
    file_name="1C_csv.csv",
    mime="text/csv",
)

#ejemplo 2
st.markdown("# Ejemplo 2")
st.pdf("recursos/1E.pdf")
data2 = hocr_csv("hocr/1E_1.hocr")
frame2 = pd.DataFrame(data2)
des2 = frame2.to_csv(index=False).encode('utf-8')
st.dataframe(frame2)

st.download_button(
    label="1E - Descargar CSV",
    data=des2,
    file_name="1E_csv.csv",
    mime="text/csv"
)

#ejemplo 3
st.markdown("# Ejemplo 3")
st.pdf("recursos/3T.pdf")
data3 = hocr_csv("hocr/3T_4.hocr")
frame3 = pd.DataFrame(data3)
des3 = frame3.to_csv(index=False).encode('utf-8')
st.dataframe(frame3)

st.download_button(
    label="3T - Descargar CSV",
    data=des3,
    file_name="3T_csv.csv",
    mime="text/csv",
)