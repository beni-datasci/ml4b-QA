import streamlit as st
import pandas as pd
import numpy as np

st.title('Question Answering')
 
with st.expander("Our Team & Mission"):
  st.write("Hello! Our team consists of Frenki Pushaj, Benjamin Rattanpal & Patrik Spindler.")
  st.write("Our mission consists of creating an app that answers all your questions regarding celebrities.")
  st.write("We strive to achieve this by utilizing Machine Learning :)")
  
with st.expander("Which Dataset do we use?"):
  st.write("We use the Squad QA dataset provided by rajpurkar on huggingface.co . It`s regarded as one of the most popular Datasets for Question Answering.")
 
st.write("Examples from our Dataset")

with st.expander("In what city and state did Beyonce grow up?"):
  st.write("Houston, Texas")

  
