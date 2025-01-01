from streamlit import *

page_link("pages/Habits.py",label="",icon="🔙")
toast('Hello there! Try adding completing habits to see your progress')

bar_chart(session_state.df,x="Time of Day",y="Hours",color="Habit",stack=False)












