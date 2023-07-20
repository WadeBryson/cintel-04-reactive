""" 
Purpose: Provide reactive output for Flights dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

This example uses dates - arguably the most complex UI input type.
 - Consider leap years, time changes, daylight savings, etc.
 - Working with dates is often challenging. 
 - This example is a good starting point - there are many examples online.

"""
import pathlib
from shiny import render, reactive
import pandas as pd
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_flights_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("flights.xlsx")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_excel(p)

    # create new field with year as a string and month together
    original_df["year-mon"] = (
        original_df["year"].astype(str) + "-" + original_df["month"]
    )
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(input.FLIGHTS_DATE_RANGE, input.FLIGHT_PASS_NUM)
    def _():
        """Reactive effect to update the filtered dataframe when inputs change.
        It doesn't need a name, because no one calls it directly."""

        # logger.info("UI inputs changed. Updating flights reactive df")

        df = original_df.copy()

        # first, drop the unnamed index column
        # axis=1 means drop a column, axis=0 means drop a row
        df = df.drop(df.columns[0], axis=1)

        # Create a new column using pd.to_datetime() method for filtering
        year_string = df["year"].astype(str)
        month_string = df["month"].astype(str)
        df["Date"] = pd.to_datetime(year_string + "-" + month_string)

        # Convert datetime to just the date, no time (datetime objects have both)
        df["Date"] = df["Date"].dt.date

        input_range = input.FLIGHTS_DATE_RANGE()
        input_min = input_range[0]
        input_max = input_range[1]
        df = df[(df["Date"] >= input_min) & (df["Date"] <= input_max)]

        # Passenger Count Filter
        input_range = input.FLIGHT_PASS_NUM()
        input_min = input_range[0]
        input_max = input_range[1]
        pass_count_filter = (df["passengers"] >= input_min) & (
            df["passengers"] <= input_max)
        df = df[pass_count_filter]

        # logger.debug(f"filtered flights df: {df}")
        reactive_df.set(df)

    @output
    @render.text
    def flights_record_count_string():
        # logger.debug("Triggered: flights_filter_record_count_string")
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message

    @output
    @render.table
    def flights_filtered_table():
        filtered_df = reactive_df.get()
        filtered_df.drop(columns=["Date"], inplace=True)
        return filtered_df

    @output
    @render_widget
    def flights_output_widget1():
        df = reactive_df.get()
        px_plot = px.scatter(
            df,
            x="year",
            y="passengers",
            title="Flights Scatter Chart (Plotly Express)",
            color="month",
        )
        return px_plot

    @output
    @render_widget
    def flights_output_widget2():
        df = reactive_df.get()

        px_plot = px.line(
            df,
            x="year-mon",
            y="passengers",
            title="Flights Line Chart (Plotly Express)",
            labels={"year-mon": "Year-Mon", "passengers": "Passengers"},
        )
        return px_plot

    # return a list of function names for use in reactive outputs
    return [
        flights_record_count_string,
        flights_filtered_table,
        flights_output_widget1,
        flights_output_widget2,
    ]
