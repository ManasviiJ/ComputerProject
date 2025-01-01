from streamlit import *
from streamlit import segmented_control

page_link("Welcome_Page.py",label="",icon="🔙")

title(':green[Habits]')
subheader(':blue[What would you like to do today?]')

col1,col2=columns(2)
with col1:
    page_link("pages/progress.py",label="See your progress",icon="🚨")
with col2:
    page_link("pages/addhabit.py",label="add a new habit",icon="🔥")

subheader("Your current habits are:")

coli,colii,coliii=columns(3)
with coli:
    subheader('Morning')
    text_area('',"wake up at 8am")
with colii:
    subheader('Afternoon')
    text_area('',"drink tea at 4pm")
with coliii:
    subheader('Evening')
    text_area('',"eat dinner at 9pm")
