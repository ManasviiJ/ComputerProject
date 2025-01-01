from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")

title(':green[Habits]')
subheader("What would you like to do today?")

col1,col2=columns(2)
with col1:
    page_link("pages/progress.py",label="See your progress",icon="🚨")
    page_link("pages/addhabit.py",label="add a new habit",icon="🔥")

