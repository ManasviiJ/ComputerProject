from streamlit import *

page_link("pages/Habits.py",label="",icon="🔙")
bar_chart(session_state.df,x="time of the day",y="number of hours",color="habits",stack=False)












