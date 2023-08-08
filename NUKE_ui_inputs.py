from shiny import ui

def get_NUKE_inputs():
    return ui.panel_sidebar(
        ui.h2("Nuclear Explosives Interaction"),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )