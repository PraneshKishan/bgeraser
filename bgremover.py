import rembg as rb
from PIL import Image
import streamlit as st
from io import BytesIO

st.title("Background remover")

with st.sidebar:
    st.write("About the developer")
    st.write("Pranesh kishan")
    st.caption("Follow me here↓")

    st.write("LinkedIn: [LinkedIn](https://www.linkedin.com/in/pranesh-online-b857322a1/)")
    st.write("Twitter: [Twitter](https://x.com/Pranesh_online?t=yoSYGsYCllvea74qZHjZ8g&s=09)")

img_inp = st.file_uploader("Upload your image here", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

def downloadable(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

if img_inp is not None:
    image = Image.open(img_inp)
    fixed = rb.remove(image)
    downloadable_image = downloadable(fixed)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Your uploaded image")
        st.image(image)
    with col2:
        st.header("Background removed Image")
        st.image(downloadable_image)

    st.download_button("Download BG removed Image", downloadable_image, key="download_button", file_name="bgremoved.png")
