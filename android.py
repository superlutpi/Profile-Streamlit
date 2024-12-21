import streamlit as st

#---Modal Jalan---

st.title("ModalJalan Mobile Application")
st.write("""
**ModalJalan** is a final project when i'm joining Kampus Merdeka from Bangkit Academy.
Every team in final project consist of 3 role, there are Mobile Developer, Cloud Computing, and Machine Learning.
Every role have every own task. Machine Learning have to create feature and dataset for the Mobile Application using Python and SQL.
Cloud Computing have to create API to implement feature and dataset from Machine Learning. 
And Mobile Developer have to create Mobile Application and implement the API from Cloud Computing using Kotlin or Java.
""")
st.write("""
I'm as a Mobile Developer, first step to create the application i have to create Mock-up of the application.
This is Mock-up of ModalJalan Mobile Application. I'm using Figma to create Mock-up and Prototype of ModalJalan. 
""")

col1, col2, col3 = st.columns((1,1,1))
with col1:
    st.image("./asset/mockup1.png", width=300)
with col2:
    st.image("./asset/mockup2.png", width=300)
with col3:
    st.image("./asset/mockup3.png", width=300)

st.write("""
After finish create Mock-up of the application, I'm implement to be Mobile Application using XML and Kotlin. 
This is how i'm implement from UI Design to be Mobile Application using XML.
""")

col4, col5 = st.columns((1,1))
with col4:
    st.image("./asset/xml1.png")
with col5:
    st.image("./asset/xml2.png")
st.write("---")