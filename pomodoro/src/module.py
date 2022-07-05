import streamlit as st


def local_css(file_name: str) -> None:
    with open(file_name) as file:
        st.markdown(f"<style>{file.read()}</style", unsafe_allow_html=True)

