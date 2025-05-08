import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# 🎨 Estilos generales con alto contraste y diseño accesible
st.markdown("""
    <style>
    .stApp {
        background-color: #fdfdfd;
        color: #1a1a1a;
        font-family: 'Segoe UI', sans-serif;
    }
    textarea, .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #cccccc;
        padding: 0.5rem;
    }
    .stButton>button {
        background-color: #005f73;
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0a9396;
        color: #ffffff;
    }
    .st-expanderHeader {
        background-color: #e3f2f7;
        color: #003844;
        padding: 0.5rem;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎨 Sidebar con mejor contraste y tono profesional
st.markdown("""
    <style>
    .css-1d391kg {
        background-color: #e6f1f5 !important;
    }
    .css-1v3fvcr, .css-1d391kg .sidebar-content {
        color: #003844 !important;
    }
    </style>
""", unsafe_allow_html=True)

translator = Translator()

# 🧠 Encabezado principal
st.title("💬 Análisis Emocional Exprés")
st.caption("Explora la polaridad y subjetividad de tus textos con un solo clic.")

# 📊 Sidebar con explicaciones breves y claras
with st.sidebar:
    st.header("📈 Indicadores emocionales")
    st.markdown("""
    <div style='color:#003844'>
    <b>Polaridad:</b> Valor entre -1 y 1 que indica el tono emocional del texto. <br><br>
    <b>Subjetividad:</b> Rango de 0 (objetivo) a 1 (subjetivo), muestra si el texto es más racional o emocional.
    </div>
    """, unsafe_allow_html=True)

# ✍️ Entrada de texto
with st.expander("📝 Analizar texto"):
    texto_input = st.text_area("Introduce tu texto aquí (en español, inglés u otro idioma):")

    if texto_input.strip():
        # Traducción y análisis
        traduccion = translator.translate(texto_input, src="auto", dest="en")
        texto_en = traduccion.text
        blob = TextBlob(texto_en)

        pol = round(blob.sentiment.polarity, 2)
        sub = round(blob.sentiment.subjectivity, 2)

        st.markdown("### 📌 Resultados")
        st.write(f"**Polaridad:** `{pol}`")
        st.write(f"**Subjetividad:** `{sub}`")

        # Resultado emocional con mensajes contrastantes
        if pol >= 0.5:
            st.success("🔷 El texto transmite una emoción **positiva**.")
        elif pol <= -0.5:
            st.error("🔴 El texto expresa una emoción **negativa**.")
        else:
            st.info("🟡 El texto tiene un tono **neutral** o equilibrado.")

# 🧾 Pie de página
st.markdown("---")
st.caption("Desarrollado con Streamlit, TextBlob y Google Translate | Estilo accesible con contraste optimizado.")
