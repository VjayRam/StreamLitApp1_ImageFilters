import cv2
import streamlit as st
import numpy as np
from PIL import Image


def cartoonify_image(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,5)
    edges=cv2.adaptiveThreshold(gray,255,
       cv2.ADAPTIVE_THRESH_MEAN_C,
       cv2.THRESH_BINARY,9,9)
#Cartoonization
    color=cv2.bilateralFilter(image,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)
    return cartoon


def main_loop():
    st.title("ARTISTIC FILTER")
    st.subheader("This app gives an artistic touch to your images!")
    st.text("We use OpenCV and Streamlit for this demo")

    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    processed_image = cartoonify_image(original_image)

    st.text("Original Image")
    st.image(original_image)

    st.text("Artistic Image (Processed)")
    st.image(processed_image)

    result = Image.fromarray(processed_image)

    from io import BytesIO
    buf = BytesIO()
    result.save(buf, format="JPEG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Cartoon Image",
        data=byte_im,
        file_name='cartoon.jpeg',
        mime='image/jpeg',
    )


if __name__ == '__main__':
    main_loop()
