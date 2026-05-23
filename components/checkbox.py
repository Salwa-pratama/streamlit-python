import streamlit as st
import numpy as np
import pandas as pd

def checkbox(df):
    st.write("Show and hide item with checkbox")
    if st.checkbox("Show dataframe"):
        st.write(df)
