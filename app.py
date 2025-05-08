import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# 🌈 Estilo personalizado minimalista con tonos cálidos
st.markdown("""
    <style>
    .stApp {
        background-color: #fff8f0;
        color: #2d2d2d;
        font-family: 'Segoe UI', sans-serif;
    }
    textarea, .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #222222;
        border: 1px solid #dddddd;
    }
    </style>
""", unsafe_allow_html=True)

# 🎨 Estética del sidebar distinta
st.markdown("""
    <style>
    .css-1d391kg {
        background-color: #fde9e0 !important;
    }
    .css-1v3fvcr, .css-1d391kg .sidebar-content {
        color: #8a2c2c !important;
    }
    </style>
""", unsafe_allow_html=True)

translator = Translator()

# 🧠 Encabezado
st.title("🧠 Análisis Emocional Exprés")
st.caption("Descubre la carga emocional de tu texto en segundos.")

# 📚 Panel lateral con otro tono
with st.sidebar:
    st.header("📈 Métricas del Texto")
    st.markdown("""
    <div style='color:#8a2c2c'>
    <b>Polaridad:</b> Desde -1 (muy negativo) hasta 1 (muy positivo).
    <br><br>
    <b>Subjetividad:</b> 0 indica objetividad, 1 indica subjetividad total.
    </div>
    """, unsafe_allow_html=True)

# 📋 Sección de entrada
with st.expander("📝 Escribe o pega un texto para analizar"):
    texto_input = st.text_area("Tu mensaje (en cualquier idioma):")

    if texto_input.strip():
        # Traducción y análisis
        traduccion = translator.translate(texto_input, src="auto", dest="en")
        texto_en = traduccion.text
        blob = TextBlob(texto_en)

        pol = round(blob.sentiment.polarity, 2)
        sub = round(blob.sentiment.subjectivity, 2)

        st.markdown("### 🔍 Resultados del análisis")
        st.write(f"**Polaridad:** `{pol}`")
        st.write(f"**Subjetividad:** `{sub}`")

        # Resultado emocional
        if pol >= 0.5:
            st.success("✅ Emoción dominante: Positiva")
        elif pol <= -0.5:
            st.error("❌ Emoción dominante: Negativa")
        else:
            st.info("➖ Emoción dominante: Neutra")

# 🪄 Pie de página
st.markdown("---")
st.caption("🧪 Aplicación demo de análisis emocional con Streamlit, TextBlob y Google Translate.")

