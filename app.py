import streamlit as st
from fastai.vision.all import *
from PIL import Image
learn = load_learner('export.pkl')

def predict_image(image):
    img = PILImage.create(image)
    pred, pred_idx, probs = learn.predict(img)
    return pred, probs[pred_idx].item()


def main():
    st.title(" Gender Image Classifier")
    st.write("Upload an image to classify")

   
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("Classifying...")
        prediction, probability = predict_image(uploaded_file)
        st.write(f"Prediction: {prediction} ")
        st.write(f"Probability: {probability:.4f} ")

if __name__ == '__main__':
    main()
