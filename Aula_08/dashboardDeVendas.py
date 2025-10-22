#import streamlit as st  # type: ignore
import pandas as pd # type: ignore

df = pd.read_csv("vendas_padaria.csv")

print(df)

print(df.head())
print(df.tail())
print(df.info())


#st.header("Dashboard de vendas", divider=True)

