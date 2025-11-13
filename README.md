# Manejo de herramientas de OCR
La siguiente prueba tiene como objetivo evaluar el manejo de herramientas OCR para la extracción de datos.

## Estructura general
Se usará streamlit como una interfaz práctica para el usuario, además del servicio de despliegue.
La estructura general del proyecto, hasta la versión V.1.1.0 es:
```
prueba_OCR/
├── data/
|   └── instrucciones.txt
├── hocr/
|   ├── 1C_5.hocr
|   ├── 1E_1.hocr
|   └── 3T_4.hocr
├── recursos/
|   ├── 1C.pdf
|   ├── 1E.pdf
|   ├── 3T.pdf
|   ├── Prueba tecnica para desarrollador IA_ revisado.pdf
|   └── notas.txt
├── main.py
├── requirements.txt
└── README.md
```

### V.1.0.0
Se hace el principio de la interfaz y se monta el servicio de despliegue

### V.1.1.0
Se hace la estructura del proyecto en subcarpetas con recursos de apoyo como las vistas previas de PDF, las instrucciones revisadas, etc., además de los archivos .hocr y algunos datos como archivos de texto grandes que se leen en la interfaz, pero no están incrustados directamente en el código.

### V.1.2.2
La interfaz despliega los PDF de referencia y una tabla con los datos extraídos de cada documento, además de que la función que encuentra las líneas, lo guarda en DataFrames de cada documento

### V.1.2.?
No se logró con exito total el usar las etiquetas de ocr_carea como haders de los DataFrames para poder separar las líneas en una estructura distinta