
import streamlit as st
import os

from PIL import Image

st.title('🌱 Weed Detection')
st.write('### This web app can detect whether a plant is a weed.')
st.write('carpetweeds crabgrass eclipta goosegrass morningglory nutsedge palmeramaranth pricklysida purslane ragweed sicklepod spottedspurge spurredanoda swinecress waterhemp')

st.write('#### Upload an image.')
uploaded_file = st.file_uploader('', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)
