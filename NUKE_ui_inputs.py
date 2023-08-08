from shiny import ui

def get_NUKE_inputs():
    return ui.panel_sidebar(
        ui.h2("Nuclear Explosives Interaction"),
        ui.tags.hr(),
        ui.input_radio_buttons(
            "Country",
            "Select Country Responsible",
            {"a": "All Countries", "b": "USA", "c": "USSR", "d": "UK"},
            selected = "a",),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )