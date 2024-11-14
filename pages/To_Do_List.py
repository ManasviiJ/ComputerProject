from streamlit import *
page_link("Welcome_Page.py",label="",icon="🔙")

title("To Do List")

if 'task_list' not in session_state:
  session_state.task_list=[]
  
task=text_input("Enter new task")
session_state.task_list.append(task)

genre = st.radio(
    "Your tasks:",
    session_state.task_list.append,
    index=None,
)

st.write("You selected:", genre)

for i in session_state.task_list:
  if radio(i):
    balloons()
