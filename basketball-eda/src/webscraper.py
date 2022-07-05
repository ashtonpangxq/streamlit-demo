import pandas as pd
import streamlit as st


@st.cache  # cache the data after downloaded for easy access
def load_data(year: int) -> pd.DataFrame:
    url = (
        "https://www.basketball-reference.com/leagues/NBA_"
        + str(year)
        + "_per_game.html"
    )
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == "Age"].index)  # deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(["Rk"], axis=1)

    return playerstats
