import streamlit as st
from PIL import Image
import base64

# Configuración de la página
st.set_page_config(page_title="Inicio", page_icon="🏠", layout="wide")

# Función para cargar la imagen y convertirla a base64
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Ruta de la imagen
image_path = "imagen.png"  # Asegúrate de que esta ruta sea correcta

# Obtener la imagen en base64
image_base64 = get_image_as_base64(image_path)

# HTML y CSS para superponer el botón
st.markdown(
    f"""
    <style>
    .background {{
        position: relative;
        text-align: center;
    }}
    .background img {{
        width: 100%;
        height: auto;
    }}
    .button-overlay {{
        position: absolute;
        bottom: 50px; /* Ajusta esta distancia desde el fondo */
        left: 50%;
        transform: translateX(-50%);
    }}
    .button-overlay button {{
        padding: 15px 32px;
        font-size: 16px;
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }}
    .button-overlay button:hover {{
        background-color: #45a049;
    }}
    </style>

    <div class="background">
        <img src="data:image/png;base64,{image_base64}" alt="Background">
        <div class="button-overlay">
            <a href="/pages/Login" target="_self">
                <button>Continuar</button>
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
