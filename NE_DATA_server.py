# Purpose: Provide reactive output for the Nuclear Explosions Dataset.

import pathlib

from shiny import render, reactive
import pandas as pd
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

def get_NE_DATA_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("nuclear_explosions.csv")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_excel(p)
    total_count = len(original_df)

    # Create a reactive value to hold the filtered pandas dataframe
    reactive_df = reactive.Value()

    # Create a reactive effect to set the reactive value when inputs change
    # List all the inputs that should trigger this update

    @reactive.Effect
    @reactive.event(
        input.NE_Country_USA,
        input.NE_Country_USSR,
        input.NE_Country_FRANCE,
        input.NE_Country_UK,
        input.NE_Country_CHINA,
        input.NE_Country_PAKIS,
        input.NE_Country_INDIA,
        input.NE_YEAR_RANGE,
        input.NE_MIN_EXPLOSION
    )
    def _():
        """Reactive effect to update the filtered dataframe when inputs change.
        This is the only way to set a reactive value (after initialization).
        It doesn't need a name, because no one calls it directly."""

        df = original_df.copy()

        # Country Select Filter
        show_countries_list = []
        if input.NE_Country_USA():
            show_countries_list.append("USA")
        if input.NE_Country_USSR():
            show_countries_list.append("USSR")
        if input.NE_Country_FRANCE():
            show_countries_list.append("FRANCE")
        if input.NE_Country_UK():
            show_countries_list.append("UK")
        if input.NE_Country_CHINA():
            show_countries_list.append("CHINA")
        if input.NE_Country_PAKIS():
            show_countries_list.append("PAKIS")
        if input.NE_Country_INDIA():
            show_countries_list.append("INDIA")
        show_countries_list = show_countries_list or ["USA", "USSR", "FRANCE", "UK", "CHINA", "PAKIS", "INDIA"]
        country_filter = df["Weapon Source Country"].isin(show_countries_list)
        df = df[country_filter]

        # Year Select Filter
        input_range = input.NE_YEAR_RANGE()
        input_min = input_range[0]
        input_max = input_range[1]
        year_filter = (df["Date.Year"] >= input_min) & (df["Date.Year"] <= input_max)
        df = df[year_filter]

        # Minimum Explosion Yield Filter
        min_explosion_filter = df["Data.Yield.Upper"] >= input.NE_MIN_EXPLOSION()
        df = df[min_explosion_filter]

        reactive_df.set(df)

    @output
    @render.text
    def NE_DATA_record_count_string():
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        return message

    @output
    @render.table
    def NE_DATA_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df

    @output
    @render_widget
    def NE_DATA_output_widget1():
        df = reactive_df.get()
        plotly_plot = px.scatter(
            df,
            x="Date.Year",
            y="Data.Yield.Upper",
            color="Weapon Source Country",
            title="Nuclear Explosions Chart",
            labels={
                "Date.Year": "Year",
                "Data.Yield.Upper": "Kilotons of TNT",
            },
            #TODO Bigger?
            size_max=8,
        )

        return plotly_plot

    # return a list of function names for use in reactive outputs
    return [
        NE_DATA_record_count_string,
        NE_DATA_filtered_table,
        NE_DATA_output_widget1,
    ]