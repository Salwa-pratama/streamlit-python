import pandas as pd
import streamlit as st
import numpy as np

def line_chart():
    st.write("Here is line chart")
    chart_data= pd.DataFrame(
        np.random.randn(20,3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

    return chart_data

