from streamlit import *

page_link("pages/Habits.py",label="",icon="🔙")
bar_chart(session_state.df,x="Time of the Day",y="Hours",color="Habit",stack=False)












