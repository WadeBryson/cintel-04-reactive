import pathlib

from shiny import render, reactive
import pandas as pd
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

p = pathlib.Path(__file__).parent.joinpath("data").joinpath("nuclear_explosions.csv")
# logger.info(f"Reading data from {p}")
df = pd.read_csv(p)
results = df.head(10)
# print(results)

# for col in df.columns:
    # print(col)

new_df = df[["WEAPON SOURCE COUNTRY"]]
results2 = new_df.head(10)
print(results2)