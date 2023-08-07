# Purpose: Provide user interaction options for the Nuclear Explostions Dataset.

from shiny import ui

def get_NE_DATA_inputs():
    return ui.panel_sidebar(
        ui.h2("Nuclear Explosions Data Interactions"),
        ui.tags.hr(),
        ui.h4("Country Select (Can choose multiple)"),
        ui.input_checkbox("NE_Country_USA", "USA", value=True),
        ui.input_checkbox("NE_Country_USSR", "USSR", value=True),
        ui.input_checkbox("NE_Country_FRANCE", "FRANCE", value=True),
        ui.input_checkbox("NE_Country_UK", "UK", value=True),
        ui.input_checkbox("NE_Country_USA", "CHINA", value=True),
        ui.input_checkbox("NE_Country_PAKIS", "PAKIS", value=True),
        ui.input_checkbox("NE_Country_INDIA", "INDIA", value=True),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )