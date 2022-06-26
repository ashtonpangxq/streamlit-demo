import streamlit as st
from sklearn import datasets


st.title("Streamlit example")

st.write(
    """
# Explore different classifier
Which one is the best?
"""
)

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine"))

classifier_name = st.sidebar.selectbox(
    "Select Classifier", ("KNN", "SVM", "Random Forest")
)

def get_dataset(dataset_name):
