import pathlib

from shiny import render, reactive
import pandas as pd
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

p = pathlib.Path(__file__).parent.joinpath("data").joinpath("nuclear.csv")
# logger.info(f"Reading data from {p}")
original_df = pd.read_csv(p)
total_count = len(original_df)

results = original_df.head(10)
print(results)
