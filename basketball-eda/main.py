import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src import load_data
from src.data import filedownload

st.title("NBA Player Statistics")

st.markdown(
    """
This application performs simple webscraping of NBA player statistics data from [Basketball-reference.com](https://www.basketball-reference.com)
"""
)

st.sidebar.header("User Inputs")

# Choose year for statistics of NBA players
selected_year = st.sidebar.selectbox("Year", list(reversed(range(1950, 2021))))

# Web Scraping of NBA player statistics
playerstats = load_data(selected_year)

# Sidebar - Team Selection
sorted_unique_team = sorted(playerstats["Tm"].unique())
selected_team = st.sidebar.multiselect(
    "Team", sorted_unique_team, sorted_unique_team
)  # Third argument shows the default value to show for the multiselect bar

# Sidebar - Postiion Selection
unique_pos = ["C", "PF", "SF", "PG", "SG"]
selected_pos = st.sidebar.multiselect("Position", unique_pos, unique_pos)

# Filtering Data
df_selected_team = playerstats[
    (playerstats["Tm"].isin(selected_team)) & (playerstats["Pos"].isin(selected_pos))
]

# Main Page Details
st.header("Player Statistics of Selected Team(s)")
st.write(
    "Data Dimension: "
    + str(df_selected_team.shape[0])
    + " rows and "
    + str(df_selected_team.shape[1])
    + " columns."
)
st.dataframe(df_selected_team)

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Creating Heatmap Visualization
# Heatmap
if st.button("Intercorrelation Heatmap"):
    st.header("Intercorrelation Matrix Heatmap")
    df_selected_team.to_csv("output.csv", index=False)
    df = pd.read_csv("output.csv")

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()
