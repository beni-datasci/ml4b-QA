import streamlit as st
import pandas as pd
import numpy as np
from datasets import load_dataset
dataset = load_dataset("squad_v2")

st.title('Question Answering')
 
with st.expander("Our Team & Mission"):
  st.write("Hello! Our team consists of Frenki Pushaj, Benjamin Rattanpal & Patrik Spindler.")
  st.write("Our mission consists of creating an app that answers all your questions regarding celebrities.")
  st.write("We strive to achieve this by utilizing Machine Learning :)")
  
