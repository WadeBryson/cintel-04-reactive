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
# print(results2)

show_countries_list = []
show_countries_list.append("FRANCE")
show_countries_list.append("CHINA")

country_filter = df["WEAPON SOURCE COUNTRY"].isin(show_countries_list)
df3 = df[country_filter]
results3 = df3.head(10)
# print(results3)

plotly_plot = px.scatter(
            df,
            x="Date.Year",
            y="Data.Yeild.Upper",
            color="WEAPON SOURCE COUNTRY",
            title="Nuclear Explosions Chart",
            labels={
                "Date.Year": "Year",
                "Data.Yeild.Upper": "Kilotons of TNT",
            },
            #TODO Bigger?
            size_max=8,
        )
print(plotly_plot)