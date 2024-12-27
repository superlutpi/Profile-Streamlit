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
st.write("I am a fresh graduate from Gunadarma University majoring in Informatics Engineering." 
         "I have advanced skill in UI/UX Design for mobile application and website. Tools that I use for Wireframing, Designing, and Prototyping is Figma." 
         "I have experience created a mobile applications for Bangkit Academy 2023 By Google, GoTo, Traveloka using Figma, XML, and Kotlin."
         "Beside that, i also have advanced skill using SQL. I have strong knowledge about DBMS and RDBMS."
         "And then, i also learn about Investment and Trading Strategy." 
         "I'm using Fundamental Research and Technical Analysis for invest on the company and project that i choose."
         "For now, in the investment i deepen on Gold and Cryptocurrency.")
st.write("---")

# --- Education ----
st.write("\n")
st.subheader("Education")
st.write(" - **Information Technology, Gunadarma University**        (2020 - 2024)")
st.write("GPA : 3.65/4.00")
st.write("---")

# --- Experiences ---
st.write("\n")
st.subheader("Experience")
st.write(" - **Bangkit Academy by Google, GoTo, Traveloka**         (2023 - 2024)")
st.text("""
- Apply an application using XML in Andorid Studio.
- Designing and Prototyping final project using Figma and XML.
- Styling and Created application using Android Compose.
- Learn about fundamental of android application.
- Created simple android application using Kotlin programming language.
""")
st.write("---")

# --- Projects ----
st.write("\n")
st.subheader("Projects")

st.write(" - UI/UX Projects")
st.text("""
- Designing UI for website “Gundar Bakery”.
- Redesign UI for the application of BMKG and make principle protection more stronger.
- Designing UI application of attendance.
- Wireframing, Designing, and Prototyping UI for website “Triple-Grow”.
- Designing UI for website of my profile.
- Created Wireframe, Design, and Prototype UI for application crypto exchange.
""")

st.write(" - Website Development")
st.text("""
- Created E-Learning website for three users login, there are as a student, as an admin, and as a teacher using PHP, HTML, CSS and SQL for database
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
