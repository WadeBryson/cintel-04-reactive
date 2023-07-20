"""
Purpose: Provide user interaction options for Flights dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

See
Example date range at https://shinylive.io/py/examples/#date-range-input
Function ref at: https://shiny.rstudio.com/py/api/ui.update_date_range.html


"""
from datetime import date
from shiny import ui


def get_flights_inputs():
    return ui.panel_sidebar(
        ui.h2("Flights Interaction"),
        ui.tags.hr(),
        ui.input_date_range(
            "FLIGHTS_DATE_RANGE",
            "Enter Date Range",
            start=date(1949, 1, 1),
            end=date(1960, 12, 31),
        ),
        ui.input_slider(
            "FLIGHT_PASS_NUM",
            "Passengers Onboard",
            min=100,
            max=650,
            value=[100, 650],
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
