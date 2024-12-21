import streamlit as st

st.title("Seaweed Detection with Convolutional Neural Network Methodology")
st.write("""
When i was 4th college in my University, i have to create a final thesis. I got a Lecturer mentor who is making project about Seaweed.
My Lecturer mentor tell me to create model of Seaweed Detection using Convolutional Neural Network methodology with Python Programming Language.
The purpose of making the model is to be able to differentiate which is Seaweed and which is Ganggang.
""")
st.write("""
First step, i'm preparing data of Seaweed and Ganggang. I'm collect image of Seaweed and then i put to Google Drive. 
The seaweed that I collect is Eucheuma cottonii. I'm collect 100 pictures of Seaweed and 100 pictures of Ganggang.
""")

col1, col2 = st.columns((1,1))
with col1:
    st.image("./asset/seaweed_drive.png")
with col2:
    st.image("./asset/ganggang_drive.png")

st.write("""
After preparing data of Seaweed and Ganggang. I'm create detection model using Google Collab. 
This is the result of model of Seaweed Detection that i create.
""")

col3, col4 = st.columns((1,1))
with col3:
    st.image("./asset/cnn1.png")
with col4:
    st.image("./asset/cnn2.png")

col5, col6 = st.columns((1,1))
with col5:
    st.image("./asset/cnn3.png")
with col6:
    st.image("./asset/graph_model.png")