import streamlit as st
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
web_elearning = current_dir / "asset" / "e-learning.zip"
web_gundarbakery = current_dir / "asset" / "gundarbkry.zip"

#---E-Learning---
with open(web_elearning, "rb") as zip_file:
    ZIPbyteEL = zip_file.read()

st.title("E-Learning Website")
col1, col2 = st.columns((1,1))
with col1:
    st.image("./asset/web_pic2.png", width=400)
with col2:
    st.image("./asset/web_pic3.png", width=400)

st.write("""
I have created this E-Learning website for my thesis while i'm 3rd college in my University. 
This website build by PHP, HTML, CSS Programming Language.
I'm using Bootstrap framework for styling on CSS.
I'm also using SQL for managing database. This website have 3 role users, there are as an **Admin**, as a **Guru**, and as a **Siswa**.
""")
st.download_button(
    label="Download Zip File",
    data=ZIPbyteEL,
    file_name=web_elearning.name,   
)
st.write("---")

#---Gundar Bakery---
with open(web_gundarbakery, "rb") as zip_file:
    ZIPbyteGB = zip_file.read()

st.title("GundarBakery Website")
col1, col2 = st.columns((1,1))
with col1:
    st.image("./asset/web_pict4.png", width=400)
with col2:
    st.image("./asset/web_pict5.png", width=400)

st.write("""
I have implement this project from UI Design to be Website i'm 2nd college in my University. 
This is the final project of "Website Programming" while i'm 2nd college.
This website build by HTML and CSS. 
In the page of **Contact Us**, you can send message to my mail.
And beside that, at that page you can directed to my Whatsapp contact. 
""")
st.download_button(
    label="Download Zip File",
    data=ZIPbyteGB,
    file_name=web_gundarbakery.name,
    )
st.write("---")