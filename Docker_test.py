import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import os
import io

st.set_page_config(page_title="Docker-test", page_icon="🔥")

with open("styles/main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title('Test av Docker')
valgt_bronn = st.selectbox('Velg brønn',options=['B3_CH1','B3_CH2','B4','B5','B6'])

st.markdown('abc abc abc')
