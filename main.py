###################################################
#                Lector de .hocr                  #
#                                                 #
# V.1.0.0 //12 11 2025//                          #
# Desplegado con streamlit                        #
# Desarrollador: Sergio Emiliano López Bautista   #
#                                                 #
###################################################

# ------------------------- Requerimientos y librerías -------------------------------
import io
import os
import codecs
import streamlit as st
#from bs4 import BeautifulSoup

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

# -------------------------------- Interfaz (MAIN)-------------------------------------
instrucciones()