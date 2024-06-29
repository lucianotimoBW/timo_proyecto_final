import streamlit as st
import textwrap
import google.generativeai as genai
import config  # Import the config module

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

context = ('Como experto en automóviles, necesito que cuando un usuario ingresa '
           'un modelo de automóvil, este reciba información sobre la marca, año '
           'de fabricación, motores disponibles y otras características relevantes '
           'del vehículo.')

def consulta(context, prompt):
    response = model.generate_content(context + " " + prompt)
    archivo = response.text
    with open('archivo.txt', 'w') as f:
        f.write(archivo)
    return archivo

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

st.title("AutoInfo - Información de Automóviles")
st.write("""
    ## Descripción
    AutoInfo es una aplicación que permite a los usuarios ingresar un modelo de automóvil 
    y recibir información detallada sobre el mismo. La aplicación utiliza IA para analizar el 
    modelo ingresado y proporcionar datos precisos sobre la marca, año de fabricación, 
    motores disponibles y otras características relevantes.
    """)
prompt = st.text_input('Ingresar un modelo de automóvil:')
if st.button('Consultar'):
    if prompt:
        result = consulta(context, prompt)
        st.markdown(to_markdown(result))
        st.download_button('Descargar información', data=result, file_name='archivo.txt')
    else:
        st.warning('Por favor, ingrese un modelo de automóvil.')

st.write("""
    ## ¿Cómo funciona?
    1. Ingrese el modelo del automóvil en el campo de texto.
    2. Haga clic en el botón "Consultar" para obtener la información.
    3. Los resultados se mostrarán en la pantalla y podrá descargarlos como un archivo de texto.
    """)
