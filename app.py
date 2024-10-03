import streamlit as st

st.set_page_config(page_title='Tablero', layout='wide')
st.title('Reconocimiento dibujos a mano')


drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = st.color_picker("Pick A Color", "#00f900")
bg_color = '#000000'

option = st.selectbox(
    "freedraw",
    ("line", "rect", "circle", "transform", "polygon", "point"),
)


