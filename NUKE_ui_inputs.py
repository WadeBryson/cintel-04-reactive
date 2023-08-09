from shiny import ui

def get_NUKE_inputs():
    return ui.panel_sidebar(
        ui.h2("Nuclear Explosives Interaction"),
        ui.tags.hr(),
        ui.input_radio_buttons(
            "Country",
            "Select Country Responsible",
            {"a": "All Countries", "b": "USA", "c": "USSR", "d": "UK", "e": "PAKIST", "f": "INDIA", "g": "FRANCE", "h": "CHINA"},
            selected = "a",),
        ui.input_numeric("NUKE_MIN_EXPLOSION", "Minumum Explosion (kilotons of TNT)):", value=0.0),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )