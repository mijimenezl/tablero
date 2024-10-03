import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title='Tablero', layout='wide')
st.title('Reconocimiento dibujos a mano')


drawing_mode = drawing_mode
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = st.color_picker("Pick A Color", "#87CEEB")
bg_color = '#000000'

drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
)


canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=300,
    width=1300,
    key="canvas",
)
