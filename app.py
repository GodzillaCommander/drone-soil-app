import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Drone Soil Analyzer", page_icon="🛸")
st.title("🛸 Drone Soil Analyzer")
st.write("Upload your J2 drone photos to check surface conditions.")

uploaded_files = st.file_uploader("Drop your drone photos here...", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

if uploaded_files:
    st.divider()
    st.subheader("📊 Analysis Results")
    for file in uploaded_files:
        image = Image.open(file)
        st.image(image, caption=f"Uploaded File: {file.name}", use_container_width=True)
        
        # Color profile scan: Wet soil is dark, dry soil is light
        img_gray = np.array(image.convert("L"))
        average_brightness = np.mean(img_gray)
        
        if average_brightness < 85:
            st.info(f"Status for {file.name}: 💧 Damp / Muddy Soil")
        elif 85 <= average_brightness <= 155:
            st.warning(f"Status for {file.name}: ⛅ Moderate Moisture Soil")
        else:
            st.success(f"Status for {file.name}: 🍂 Dry / Dusty Soil")
        st.divider()
