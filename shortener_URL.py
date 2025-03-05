import pyshorteners
import streamlit as st
import validators

# Función para acortar la URL con manejo de errores
def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)
    except Exception as e:
        return f"Error: {e}"

# Configuración de la app en Streamlit
st.set_page_config(page_title="URL Shortener - Marour13", page_icon="✂", layout="centered")

# Encabezado con título e ícono
st.markdown("""
    <h1 style='text-align: center;'>✂ URL Shortener 📎</h1>
""", unsafe_allow_html=True)

st.image("icon.png", use_container_width=True)

# Entrada de la URL
url = st.text_input("Enter the URL you want to shorten:")

if st.button("Generate Shortened URL"):
    if url:
        if validators.url(url):
            short_url = shorten_url(url)
            st.success(f"**Shortened URL:** [🔗 {short_url}]({short_url})")
        else:
            st.error("Invalid URL. Please enter a valid URL.")
    else:
        st.error("Please enter a valid URL.")


#streamlit run shortener_URL.py