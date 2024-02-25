import streamlit as st
import requests

st.title('Air Quality Predictor')
st.write('- Detects the Air and predicts the quality using a deep learning CNN model.')
st.write('Here are some sample images to try out the model:')

img = None
line = ""

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    eg1 = st.empty()
    if st.button('Try Example 1'):
        response = requests.get("sample/sample_1.jpg")
        img = response.content
        line = "good"
        eg1.image(img, caption='Example 1', use_column_width=True)

with col2:
    eg2 = st.empty()
    if st.button('Try Example 2'):
        response = requests.get("sample/sample_2.jpg")
        img = response.content
        line = "Moderate"
        eg2.image(img, caption='Example 2', use_column_width=True)

with col3:
    eg3 = st.empty()
    if st.button('Try Example 3'):
        response = requests.get("sample/sample_3.jpg")
        img = response.content
        line = "Unhealthy for Sensitive Groups"
        eg3.image(img, caption='Example 3', use_column_width=True)

with col4:
    eg4 = st.empty()
    if st.button('Try Example 4'):
        response = requests.get("sample/sample_4.jpg")
        img = response.content
        line = "Unhealthy"
        eg4.image(img, caption='Example 4', use_column_width=True)

with col5:
    eg5 = st.empty()
    if st.button('Try Example 5'):
        response = requests.get("sample/sample_5.jpg")
        img = response.content
        line = "Very Unhealthy"
        eg5.image(img, caption='Example 5', use_column_width=True)

with col6:
    eg6 = st.empty()
    if st.button('Try Example 6'):
        response = requests.get("sample/sample_6.jpg")
        img = response.content
        line = "Hazardous"
        eg6.image(img, caption='Example 6', use_column_width=True)

if img is not None:
    st.write('')
    st.subheader('Result:')
    st.image(img, caption='Uploaded Image', use_column_width=True)
    st.write(line)
