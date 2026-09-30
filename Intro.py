import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Clasificación de frutas")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("Aplicación interactiva que permite clasificar frutas según su peso, diámetro y dulzor, calculando la distancia entre sus características.") 
 url = "https://mipristeamlit-bxxi3a5mttnmt7p7hugn2w.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Preparación y Estructuración de Datos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("Interactúa con datos sintéticos de sensores IoT para explorar valores faltantes, datos atípicos y preparación de información.") 
 url = "https://datospreparacion-gyu56wk2gsu7thhuh7fydo.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Series de Tiempo")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("Analiza datos históricos de sensores IoT para identificar tendencias, estacionalidad y realizar pronósticos.") 
 url = "https://seriestiempo-nrqoiwiw7haqmd9scvdwgc.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Regresión Logística")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("Explora cómo un modelo de clasificación predice si lloverá mañana, analizando variables, umbrales y errores de predicción.") 
 url = "https://regresionlogistica-qe7blb7euan4ir6hjaypsp.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Descenso de Gradiente")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("Explora cómo la tasa de aprendizaje y el punto inicial afectan la convergencia del algoritmo de descenso de gradiente.") 
 url = "https://appgradient-ezaktaseymudwulglplebf.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Preparación de Datos Ambientales")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("Analiza mediciones de niveles de ríos y quebradas de CORNARE mediante estadísticas, gráficas y detección de valores atípicos.") 
 url = "https://appnivelcornare-edjpiaamjwxuberzumgqgd.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Predicción de la Calidad del Aire")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("Utiliza modelos de series de tiempo para analizar y predecir los niveles de contaminantes atmosféricos.") 
 url = "https://pronosticocornare-lp8jr5cyd7d58kmifzf5d6.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Clasificación de Fertilidad de Suelos con KNN")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("Aplica el algoritmo KNN para clasificar la fertilidad de los suelos en niveles bajo, medio o alto a partir de sus propiedades químicas.") 
 url = "https://aplicaci-nknn-2xmrwuhbkzndtn7qstw25j.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Detector de Anomalías")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("Compara la lógica tradicional con la vectorización usando NumPy, explorando alarmas, complejidad Big-O y rendimiento.") 
 url = "https://scriptbig0-9crttseksj2srcjaiggwar.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Regresión Lineal")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("Explora cómo construir y evaluar modelos de regresión para predecir valores numéricos usando datos de viviendas en California.") 
 url = "https://regresionlineal-23pbt8xzecrt5x4bu46evs.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Predicción de Sensación Térmica")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("Utiliza datos reales de temperatura y humedad capturados por sensores IoT para predecir la sensación térmica mediante regresión lineal.") 
 url = "https://sensasiontermicaiot-7mwswfsttmb4rcaeanrwpz.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


