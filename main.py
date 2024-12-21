import streamlit as st

page_profile = st.Page(
    page="profile_1.py",
    title="About Me",
    icon=":material/smart_toy:"
)

uiux = st.Page(
    page="uiux.py",
    title="UI/UX Design"
)

web = st.Page(
    page="web.py",
    title="Website Development"
)

mbl = st.Page(
    page="android.py",
    title="Android Development"
)

ml = st.Page(
    page="machinelearning.py",
    title="Machine Learning"
)

skill = st.Page(
    page="skill.py",
    title="Skill"
)

certi = st.Page(
    page="certifications.py",
    title="Certifications"
)

pg = st.navigation({
    "Info" : [page_profile],
    "Portfolio and Projects" : [uiux, web, mbl, ml ],
    "More" : [certi]
})

pg.run()