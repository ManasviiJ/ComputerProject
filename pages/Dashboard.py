from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")

title(":violet[Dashboard]")
subheader(":blue[Your existing habits:]")

for habit,days in session_state.habits.items():
  write(habit,"for",days,"days")

divider()

subheader("Your To-DO List for the day")
