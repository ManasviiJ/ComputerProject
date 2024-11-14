from streamlit import *
page_link("Welcome_Page.py",label="",icon="🔙")

if 'task_list' not in session_state:
  session_state.task_list=[]
task=text_input("Enter new task")
session_state.task_list.append('task')
for i in session_state.task_list:
  if checkbox(i):
    balloons()
