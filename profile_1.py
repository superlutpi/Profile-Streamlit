import streamlit as st
import base64

@st.dialog("Contact Me")
def go_to_contact():
    colx, coly, colz = st.columns((1, 1, 1),  vertical_alignment="center")
    with colx:
        st.image("./asset/whatsapp.png", width=70)
        st.markdown("[**Whatsapp**](https://wa.me/6281287986865)")
    with coly:
        st.image("./asset/instagram.png", width=70)
        st.markdown("[**Instagram**](https://www.instagram.com/irdzaghiffaryy/)")
    with colz:
        st.image("./asset/gmail.png", width=70)
        st.markdown("[**Email**](https://girdza248@gmail.com)")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./asset/cropped_image.png", width=250)
with col2:
    st.header("Irdza Ghiffary Lutfi", anchor=False)
    st.write("UI/UX Designer - Data Analyst - Mobile and Website Developer")
    if st.button("Contact Me"):
        go_to_contact()

# ---Profile---
st.write("I am a graduate from Gunadarma University majoring in Information Technology." 
         "I have advanced skills using Structured Query Language (SQL) and also have strong knowledge of DBMS and RDBMS."  
         "I have experience using SQL Procedure (e.g., Stored Procedure, Function Procedure)."
         "Proficient in using PostgreeSQL, MySQL, and also Microsoft SQL Server."
         "I have work experience at Suzuki Finance as an IT Asset Management for handling databases from collection divison."  
         "And also, I have experiences and strong knowledge of Python Programming."
         "I have deployed “Seaweed Detection” using Python Programming Language for my final thesis."
         "The experience has enabled me on how to use the Python Framework."
         "I’m currently following a program from RevoU as a Data Analytics to deepen my skill and knowledge in using tools (e.g., SQL, Python, Tableau, PowerBI).")
st.write("---")

# --- Education ----
st.write("\n")
st.subheader("Education")
st.write(" - **Information Technology, Gunadarma University**        (2020 - 2024)")
st.write("GPA : 3.66/4.00")
st.write("---")

# --- Experiences ---
st.write("\n")
st.subheader("Experience")
st.write(" - **Bangkit Academy by Google, GoTo, Traveloka**         (2023 - 2024)")
st.text("""
- Applied 4 mobile applications, handling from end-to-end in Android Studio using XML programming language (e.g., Android Compose) as front-end and Kotlin as back-end.
- Implemented fundamentals of the Android Application to be Mobile Application using Kotlin and XML in Android Studio
- Created Modal Jalan mobile application as a capstone project, covering the scope of work from design using Figma to mobile development using Kotlin and XML.
""")
st.write("---")

# --- Projects ----
st.write("\n")
st.subheader("Projects")

st.write(" - UI/UX Projects")
st.text("""
- Designed UI for website “Gundar Bakery”.
- Redesigned UI for the application of BMKG and make principle protection more stronger.
- Designed UI application of attendance.
- Created Wireframe, Design, and Prototype UI for website “Triple-Grow”.
- Designed UI for website of my profile.
- Created Wireframe, Design, and Prototype UI for application crypto exchange.
""")

st.write(" - Website Development")
st.text("""
- Created E-Learning website for three users login, there are as a student, as an admin, and as a teacher using PHP, HTML, CSS and SQL for manage database
- Implement from UI Design to website from “Gundar Bakery” using HTML and CSS.
""")

st.write(" - Android Development")
st.text("""
- Created mobile application “ModalJalan” using Kotlin Programming Language and XML.
""")

st.write(" - Machine Learning")
st.text("""
- Created Seaweed Detection using Python Programming Language and CNN for final thesis.
""")

st.write("---")

# --- Organization Experiences ---
st.write("\n")
st.subheader("Organization Experience")
st.write(" - Cartel Capital - Admin         (2023 - Now)")
st.text("""
Cartel Capital is a non-profit educational community platform for cryptocurrency enthusiasts that was built in 2023. This community was formed from the founder's interest in cryptocurrency and lack of people discussing this matter.
""")
st.write("---")

# --- Skill ---
st.subheader("Skill")
st.write("\n")

colm1, colm2, colm3 = st.columns((1,1,3))
with colm1:
    st.image("./asset/python.png", width=50)
with colm2:
    st.image("./asset/figma.png", width=50)
with colm3:
    st.image("./asset/php.png", width=50)
with colm1:
    st.image("./asset/html-5.png", width=50)
with colm2:
    st.image("./asset/css-3.png", width=50)
with colm3:
    st.image("./asset/Postgresql.png", width=50)
