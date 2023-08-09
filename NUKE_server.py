import pathlib

from shiny import render, reactive
import pandas as pd
from shinywidgets import render_widget
import plotly.express as px
from ipyleaflet import Map, basemaps, Marker

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_NUKE_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("nuclear.csv")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_csv(p)
    total_count = len(original_df)

    # Create a reactive value to hold the filtered pandas dataframe
    reactive_df = reactive.Value()

    # Deleted Reactive Event
    @reactive.Effect
    @reactive.event(
        input.Country,
        input.NUKE_MIN_Explosion
    )

    def _():
        """Reactive effect to update the filtered dataframe when inputs change.
        This is the only way to set a reactive value (after initialization).
        It doesn't need a name, because no one calls it directly."""

        # logger.info("UI inputs changed. Updating penguins reactive df")

        df = original_df.copy()

        # Country Filter
        input_country = input.Country()
        country_dict = {"a": "All Countries", "b": "USA", "c": "USSR", "d": "UK", "e": "PAKIST", "f": "INDIA", "g": "FRANCE", "h": "CHINA"}
        if input_country != "a":
            country_filter = df["Country"] == country_dict[input_country]
            df = df[country_filter]
        
        # Minimum Explosion Filter
        NUKE_EXPLOSION_filter = df["Explosion.(kilotons)"] >= input.NUKE_MIN_EXPLOSION()
        df = df[NUKE_EXPLOSION_filter]

        reactive_df.set(df)

    @output
    @render.text
    def NUKE_record_count_string():
        # logger.debug("Triggered: penguins_filter_record_count_string")
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message
    
    # @output
    # @render_widget
    # def NUKE_output_widget1():
        df = reactive_df.get()
        plotly_plot = Map(basemap=basemaps.OpenStreetMap.Mapnik, center=(25,0), zoom=2)
        for i in range(0, len(df)):
            marker = Marker(location= ([df.iloc[i]['Latitude'], df.iloc[i]['Longitude']]), draggable=False)
            plotly_plot.add_layer(marker)

        return plotly_plot

    @output
    @render.table
    def NUKE_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df

    # return a list of function names for use in reactive outputs
    return [
        NUKE_record_count_string,
        NUKE_filtered_table,
    ]