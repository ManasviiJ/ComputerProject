from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")
balloons()

title(":violet[Dashboard]")
write()
col1,col2=columns(2)
with col1:
  subheader(":grey[Your existing habits:]")
  for habit,days in session_state.habits.items():
    write(habit,"for",days,"days")
with col2:
  subheader("Your To-DO List for the day")
  for task_not_done in session_state.tasks:
    if task_not_done['status']==False:
      write(task_not_done['task'])

