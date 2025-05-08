import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# 🎨 Estilos vibrantes y combinados con tipografía elegante
st.markdown("""
    <style>
    .stApp {
        background-color: #fff9f0;
        color: #2e2e2e;
        font-family: 'Helvetica Neue', sans-serif;
    }
    textarea, .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #2e2e2e;
        border: 2px solid #fbbf24;
        border-radius: 8px;
        padding: 0.6rem;
    }
    .stButton>button {
        background-color: #f97316;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ea580c;
        color: #ffffff;
    }
    .st-expanderHeader {
        background-color: #fcd34d;
        color: #3f3f46;
        font-weight: 600;
        border-radius: 6px;
        padding: 0.5rem;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #e11d48;
    }
    </style>
""", unsafe_allow_html=True)

# 🎨 Sidebar con combinación armoniosa
st.markdown("""
    <style>
    .css-1d391kg {
        background-color: #ffe4e6 !important;
    }
    .css-1v3fvcr, .css-1d391kg .sidebar-content {
        color: #9f1239 !important;
    }
    </style>
""", unsafe_allow_html=True)

translator = Translator()

# 🧠 Encabezado principal vibrante
st.title("🌺 LENGUA EMOCIONAL")
st.caption("Descubre cómo se sienten tus palabras: emociones, percepción y más.")

# 📊 Sidebar explicativo con tonos rosados suaves
with st.sidebar:
    st.header("🎯 Indicadores emocionales")
    st.markdown("""
    <div style='color:#9f1239; font-size:16px;'>
    <b>Polaridad:</b> Un número entre -1 (negativo) y 1 (positivo). <br><br>
    <b>Subjetividad:</b> Va de 0 (objetivo) a 1 (subjetivo). Refleja cuánto del texto es emocional o personal.
    </div>
    """, unsafe_allow_html=True)

# ✍️ Área de texto y análisis
with st.expander("💬 Analizar emociones del texto"):
    texto_input = st.text_area("Escribe aquí tu texto en cualquier idioma:")

    if texto_input.strip():
        traduccion = translator.translate(texto_input, src="auto", dest="en")
        texto_en = traduccion.text
        blob = TextBlob(texto_en)

        pol = round(blob.sentiment.polarity, 2)
        sub = round(blob.sentiment.subjectivity, 2)

        st.markdown("### 🎨 Resultados de análisis")
        st.write(f"**🌈 Polaridad:** `{pol}`")
        st.write(f"**🧠 Subjetividad:** `{sub}`")

        if pol >= 0.5:
            st.success("💖 El texto refleja una emoción **positiva**.")
        elif pol <= -0.5:
            st.error("💔 El texto expresa una emoción **negativa**.")
        else:
            st.info("💬 El texto tiene un tono **neutral** o equilibrado.")

# ✨ Footer
st.markdown("---")
st.caption("🧪 Hecho con ❤️ usando Streamlit, TextBlob y Google Translate. Estilo vibrante y armónico.")
