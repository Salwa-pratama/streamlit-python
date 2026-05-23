import streamlit as st
import pandas as pd
import numpy as np
from components import read_data, line_chart, map_data, widgets_display, checkbox, layout, show_progress
from advanced import caching
# First read dataset with streamlit
df = read_data()

st.write("Here is Titanic dataset")
st.write(df)

# Draw a line chart
line_chart()

# plot a map
map_data()

# widgets
widgets_display()

# checkbox
checkbox(df)

# Layout
layout()
# Show proggres
show_progress()

# Caching
caching()
