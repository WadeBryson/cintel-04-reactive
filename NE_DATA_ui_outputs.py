# Purpose: Display output for Nuclear Explosions Dataset.

from shiny import ui
from shinywidgets import output_widget


def get_NE_DATA_outputs():
    return ui.panel_main(
        ui.h2("Nuclear Explosions Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Nuclear Explosions: Charts"),
            output_widget("NE_DATA_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Nuclear Explosions Table"),
            ui.output_text("NE_DATA_record_count_string"),
            ui.output_table("NE_DATA_filtered_table"),
            ui.tags.hr(),
        ),
    )