import pathlib

from shiny import render, reactive
import pandas as pd
from shinywidgets import render_widget
import plotly.express as px

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

    def _():
        """Reactive effect to update the filtered dataframe when inputs change.
        This is the only way to set a reactive value (after initialization).
        It doesn't need a name, because no one calls it directly."""

        # logger.info("UI inputs changed. Updating penguins reactive df")

        df = original_df.copy()

        # Deleted Filter

        reactive_df.set(df)

    @output
    @render.text
    def NUKE_record_count_string():
        # logger.debug("Triggered: penguins_filter_record_count_string")
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message

    @output
    @render.table
    def NUKE_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df

    @output
    @render_widget
    def NUKE_output_widget1():
        df = reactive_df.get()
        plotly_plot = px.scatter(
            df,
            x="Date.Year",
            y="Data.Yeild.Upper",
            color="WEAPON SOURCE COUNTRY",
            title="Penguins Plot (Plotly Express))",
            labels={
                "Date.Year": "Year",
                "Data.Yeild.Upper": "Explosion Size (kilotons of TNT)",
            },
            size_max=8,
        )

        return plotly_plot

    # return a list of function names for use in reactive outputs
    return [
        NUKE_record_count_string,
        NUKE_filtered_table,
        NUKE_output_widget1,
    ]