import streamlit as st
import numpy as np
import pandas as pd

def checkbox(df):
    st.write("Show and hide item with checkbox")
    if st.checkbox("Show dataframe"):
        st.write(df)

    # df = pd.DataFrame({
    # 'first column': [1, 2, 3, 4],
    # 'second column': [10, 20, 30, 40]
    # })

    option = st.selectbox(
        'Which number do you like best?',
        df['Sex'].unique())

    st.write('You selected: ', option)




