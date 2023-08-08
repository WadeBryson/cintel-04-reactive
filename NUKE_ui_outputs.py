from shiny import ui
from shinywidgets import output_widget


def get_NUKE_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Nuclear Explosions: Charts"),
            output_widget("NUKE_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Nuclear Explosions Table"),
            ui.output_text("NUKE_record_count_string"),
            ui.output_table("NUKE_filtered_table"),
            ui.tags.hr(),
        ),
    )