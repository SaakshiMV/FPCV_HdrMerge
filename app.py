import streamlit as st
import cv2
import numpy as np
import os
from PIL import Image

st.set_page_config(page_title="HDR Image Merge", layout="wide")
st.title("📸 HDR Image Merge (Simulated Exposures)")

# ----------------------------
# Upload Base Image
# ----------------------------
uploaded_file = st.file_uploader("Upload a base image", type=["jpg","png","jpeg"])
if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file).convert('RGB'))
    img_base = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    st.subheader("Original Image")
    st.image(cv2.cvtColor(img_base, cv2.COLOR_BGR2RGB), use_column_width=True)

    # ----------------------------
    # Adjustable sliders for exposures
    # ----------------------------
    st.subheader("Adjust Exposure Factors")
    col1, col2, col3 = st.columns(3)
    factor1 = col1.slider("Dark Exposure", 0.1, 1.0, 0.5)
    factor2 = col2.slider("Mid Exposure", 0.1, 1.0, 0.8)
    factor3 = col3.slider("Bright Exposure", 0.1, 1.0, 1.0)
    exposure_factors = [factor1, factor2, factor3]

    # ----------------------------
    # Simulate exposures
    # ----------------------------
    images = [np.clip(img_base * f, 0, 255).astype('uint8') for f in exposure_factors]

    st.subheader("Simulated Exposures")
    cols = st.columns(len(images))
    for i, img in enumerate(images):
        with cols[i]:
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption=f"Exposure {i+1}", use_column_width=True)

    # ----------------------------
    # HDR Merge
    # ----------------------------
    exposure_times = np.array([1/30, 1/15, 1/8], dtype=np.float32)
    base_shape = images[0].shape[:2]
    images_resized = [cv2.resize(img, (base_shape[1], base_shape[0])) for img in images]
    merge_debevec = cv2.createMergeDebevec()
    hdr = merge_debevec.process(images_resized, times=exposure_times.copy())

    # ----------------------------
    # Gamma slider for tone mapping
    # ----------------------------
    st.subheader("Tone Mapping Settings")
    gamma = st.slider("Gamma", 0.5, 3.0, 2.2, 0.1)

    if hasattr(cv2, 'createTonemapDurand'):
        tonemap = cv2.createTonemapDurand(gamma=gamma)
        ldr = tonemap.process(hdr.copy())
        ldr = np.clip(ldr*255, 0, 255).astype('uint8')
        st.info("Used createTonemapDurand for tone mapping.")
    else:
        ldr = cv2.normalize(hdr, None, 0, 255, cv2.NORM_MINMAX)
        ldr = np.clip(ldr, 0, 255).astype('uint8')
        st.warning("TonemapDurand not available, used fallback normalization.")

    # ----------------------------
    # Display HDR output
    # ----------------------------
    st.subheader("HDR Tone-mapped Result")
    st.image(cv2.cvtColor(ldr, cv2.COLOR_BGR2RGB), use_column_width=True)

    # ----------------------------
    # Save and Download
    # ----------------------------
    output_dir = "output_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    hdr_file = os.path.join(output_dir, "hdr_tonemapped.jpg")
    cv2.imwrite(hdr_file, ldr)

    st.success("HDR Tone-mapped image saved!")

    st.download_button("Download HDR Tone-mapped Image", open(hdr_file, "rb"), file_name="hdr_tonemapped.jpg")
