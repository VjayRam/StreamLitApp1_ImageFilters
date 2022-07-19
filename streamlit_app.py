import cv2
import streamlit as st
import numpy as np
from PIL import Image


def artistic(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,5)
    edges=cv2.adaptiveThreshold(gray,255,
       cv2.ADAPTIVE_THRESH_MEAN_C,
       cv2.THRESH_BINARY,9,9)
    color=cv2.bilateralFilter(image,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)
    return cartoon

def greyscale(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return greyscale

def bright(img, beta_value ):
    img_bright = cv2.convertScaleAbs(img, beta=beta_value)
    return img_bright

def sharpen(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    img_sharpen = cv2.filter2D(img, -1, kernel)
    return img_sharpen

def pencil_sketch(img,color=0):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    if color==0:
        return  sk_gray
    else:
        return sk_color

def invert(img):
    inv = cv2.bitwise_not(img)
    return inv 


def main_loop():
    st.title("IMAGE FILTERS USING OPENCV")
    st.subheader("App to apply filters to beautify your image.")

    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    st.subheader("Original Image")
    st.image(original_image) 

    option = st.selectbox(
     'Select the filter to apply to the original image:',
     ('Artistic', 'Black and White', 'Brightness adjustment','Sharpen','Pencil Sketch (B&W)','Pencil Sketch (Color)','Invert Color'))

    if option == 'Artistic':
        processed_image = artistic(original_image)
        st.subheader("Artistic Image (Processed)")
        st.image(processed_image)
        result = Image.fromarray(processed_image)

        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Artistic Image",
            data=byte_im,
            file_name='artistic.jpeg',
            mime='image/jpeg',
        )
    if option == 'Black and White': 
        processed_image = greyscale(original_image)
        st.subheader("Black and White")
        st.image(processed_image)
        result = Image.fromarray(processed_image)

        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download B&W Image",
            data=byte_im,
            file_name='b&w.jpeg',
            mime='image/jpeg',
        )
    if option == 'Brightness adjustment':
        values = st.slider('Adjust brightness:',0, 100, 50)
        processed_image = bright(original_image,(values-50))
        st.subheader("Brightness adjusted image")
        st.image(processed_image)
        result = Image.fromarray(processed_image)

        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Adjusted Image",
            data=byte_im,
            file_name='light_adj.jpeg',
            mime='image/jpeg',
        )
    if option == 'Sharpen':
        processed_image = sharpen(original_image)
        st.subheader("Sharpened Image")
        st.image(processed_image)
        result = Image.fromarray(processed_image)

        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Sharpened Image",
            data=byte_im,
            file_name='sharp_img.jpeg',
            mime='image/jpeg',
        )
    if option == 'Pencil Sketch (B&W)':
        processed_image = pencil_sketch(original_image,0)
        st.subheader("Sketched Image")
        st.image(processed_image)
        result = Image.fromarray(processed_image)

        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Sketch Image",
            data=byte_im,
            file_name='sketch.jpeg',
            mime='image/jpeg',
        )
    if option == 'Pencil Sketch (Color)':
        processed_image = pencil_sketch(original_image,1)
        st.subheader("Sketched Image")
        st.image(processed_image)
        result = Image.fromarray(processed_image)

        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Sketch Image",
            data=byte_im,
            file_name='sketch_col.jpeg',
            mime='image/jpeg',
        )
    if option == 'Invert Color':
        processed_image = invert(original_image)
        st.subheader("Color Inverted Image")
        st.image(processed_image)
        result = Image.fromarray(processed_image)

        from io import BytesIO
        buf = BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Inverted Image",
            data=byte_im,
            file_name='inverted.jpeg',
            mime='image/jpeg',
        )
    

if __name__ == '__main__':
    main_loop()

# https://vjayram-streamlitapp1-streamlit-app-itk9iu.streamlitapp.com/
