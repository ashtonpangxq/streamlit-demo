import streamlit as st
import time
import cv2
from src import local_css

# Import css styling
local_css("style.css")

# Create Empty Spaces
st.markdown("#")
st.markdown("#")
st.markdown("#")

# Create Timer Button & Centralize Button
col1, col2, col3, col4, col5 = st.beta_columns(5)

with col2:
    pass
with col3:
    pass
with col4:
    pass
with col5:
    pass
with col1:
    # Main body
    st.write(
        """
    # Pomodoro App
    Have a break, have a Kit Kat!
    """
    )
    button_clicked = st.button("kitkat")

# st.markdown(
#     "<h1 style='text-align: center; color: white;'>Pomodoro App</h1>",
#     unsafe_allow_html=True,
# )
# st.markdown(
#     "<h3 style='text-align: center; color: white;'>Have a break, have a KitKat!</h1",
#     unsafe_allow_html=True,
# )

# Create Timer Button
# button_clicked = st.button("Start")

# Working Time
t1 = 1500
# Resting Time
t2 = 300

if button_clicked:
    with st.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            t1 -= 1
            st.success("🔔 25 minutes is over! Time for a break!")

    with st.empty():
        while t2:
            # Start the break
            mins2, secs2 = divmod(t2, 60)
            timer2 = "{:02d}:{:02d}".format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            t2 -= 1
            st.error("⏰ 5 minute break is over!")
