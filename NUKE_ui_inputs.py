from shiny import ui

def get_NUKE_inputs():
    return ui.panel_sidebar(
        ui.h2("Nuclear Explosives Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "NUKE_YEAR_RANGE",
            "Nuclear Explosions Date Range (Year)",
            min=1940,
            max=2000,
            value=[1940, 2000],
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )