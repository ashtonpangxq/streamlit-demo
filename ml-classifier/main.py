# Import streamlit api
import streamlit as st
import pandas as pd

# Import helper functions
import helper_functions

# Import Visualization Modules
import matplotlib.pyplot as plt

# Import relevant libraries for Machine Learning Models and Auxiliary Libraries
from sklearn.model_selection import train_test_split
import numpy as np

# Feature Extraction Modules
from sklearn.decomposition import PCA

# Import Evaluation Metrics from SKLEARN
from sklearn.metrics import accuracy_score

# Side Bar Visual
st.sidebar.header("User Input Parameters")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine"))

st.sidebar.subheader("User Input Features")

# User Input Parameters
if dataset_name == "Iris":
    df = helper_functions.iris_input_features()

classifier_name = st.sidebar.selectbox(
    "Select Classifier", ("KNN", "SVM", "Random Forest")
)

# Data Preparation

data, X, y = helper_functions.get_dataset(dataset_name)
st.sidebar.subheader("Hyperparameter Tuning")
params = helper_functions.add_parameter_ui(classifier_name)
clf = helper_functions.get_classifier(classifier_name, params)

# Classification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)

# Generate predictions
if dataset_name == "Iris":
    prediction = clf.predict(df)
    prediction_proba = clf.predict_proba(df)
    df_prediction_proba = pd.DataFrame(
        prediction_proba,
        columns=[data.target_names[0], data.target_names[1], data.target_names[2]],
        index=["Probability"],
    )

# Main Body Visual
st.title("Comparing Machine Learning Classifier Models")

st.write(
    """
# Explore different classifier
Which one is the best?
"""
)

st.write(f"## {dataset_name} Dataset")
st.subheader("---------------------------")
st.subheader("Exploratory Data Analysis")
st.write("Shape of Dataset", X.shape)
st.write("Number of Classes", len(np.unique(y)))

# Plotting of Graphs
pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()

# Show Graphs
st.pyplot(fig)

# Classification Results
st.subheader("---------------------------")
st.subheader("Classification Results")
st.write(f"Classifier: {classifier_name}")
st.write(f"Accuracy: {acc}")

# Predictions Results
if dataset_name == "Iris":
    st.subheader("---------------------------")
    st.subheader("Prediction Probabilities")
    st.write(df_prediction_proba)
    st.write(f"Predicted: {''.join(data.target_names[prediction]).capitalize()}")
