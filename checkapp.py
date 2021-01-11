import streamlit as st
st.title("CHECK APP")
st.write("It's just for checking")
st.file_uploader("Upload an image of jpg format",type="jpg")
import cv2
import PIL