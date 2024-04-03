
import streamlit as st
import os

from PIL import Image

st.title('🌱 Weed Detection')
st.write('### This web app can detect whether a plant is a crop or weed.')

st.write('#### Upload an image.')
uploaded_file = st.file_uploader('', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)
