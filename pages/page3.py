import streamlit as st
import pandas as pd

df = pd.read_csv("./data/datautf-8.csv", index_col="月")
st.title("平均気温")
st.line_chart(df)
st.bar_chart(df["2021"])