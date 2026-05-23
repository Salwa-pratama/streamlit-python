
from PIL import Image
import streamlit as st


def caching():
    image = Image.open("./images/caching.png")
    st.markdown("# Caching visualization")
    st.image(image)

     # Caching
    @st.cache_data
    def long_running_function(param1, param2):
        return
