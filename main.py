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
import streamlit as st
from bs4 import BeautifulSoup

# --------------------------- Seteadores ----------------------------------------------
st.set_page_config(page_title="Lector de .hocr",
                   page_icon = "👁️",
                   layout="wide")
st.title("Lector de .hocr")