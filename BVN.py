import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_excel('ONS-Acomph.xlsx', sheet_name= "Acomph")

st.title('BVN - Boletim de Vazões e Níveis do Complexo Belo Monte')
